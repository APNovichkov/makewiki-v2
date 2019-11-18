from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect


from wiki.models import Page
from wiki.forms import PageForm


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })


def get_page(request):
    if request.method == 'POST':
        f = PageForm(request.POST)

        print("Form: {}".format(f))

        if form.is_valid():
            print("form is valid")
            return HttpResponseRedirect("/")
        else:
            print("form is invalid")

    else:
        form = PageForm()

    return render(request, 'newpage.html', {'form': form})
