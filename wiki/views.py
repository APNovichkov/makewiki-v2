from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse_lazy


from wiki.models import Page
from wiki.forms import PageForm


class PageListView(ListView):
    """Render a list of all Pages."""

    model = Page

    def get(self, request):
        """GET a list of Pages."""

        pages = self.get_queryset().all()
        return render(request, 'list.html', {
            'pages': pages
        })

class PageDetailView(DetailView):
    """Render a specific page based on it's slug."""

    model = Page

    def get(self, request, slug):
        """Return a specific wiki page by slug."""

        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
            'page': page
        })


class PageCreateView(CreateView):
    template_name = 'newpage.html'
    form_class = PageForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.created = timezone.now()
        self.object.modified = timezone.now()
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('wiki-list-page'))

    def get_form_kwargs(self, *args, **kwargs):
        print("\nI am in get_form_kwargs in PageCreateView\n")

        kwargs = super(PageCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['author'] = self.request.user
        kwargs['created'] = timezone.now()

        print("kwargs -> author: {}".format(kwargs['author']))
        print("kwargs -> created: {}".format(kwargs['created']))

        return kwargs



class PageCreateView_(CreateView):
    """Process create new_page logic."""

    def get(self, request, *args, **kwargs):
        context = {'form': PageForm}
        return render(request, 'newpage.html', context)

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        print("Form: {}".format(form))

        if form.is_valid():
            print("Form is valid")
            page = form.save(commit=False)
            page.author = request.user
            page.created = timezone.now()
            page.modified = timezone.now()
            page.save()
            return HttpResponseRedirect(reverse_lazy('wiki-list-page'))

        return render(request, 'newpage.html', {'form': form})
