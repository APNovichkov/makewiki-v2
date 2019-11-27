from django import forms
from wiki.models import Page


class PageForm(forms.ModelForm):
    """Render and process a form based on the Page model."""

    class Meta:
        """Meta class to specify form."""

        model = Page
        exclude = ('author', 'slug', 'modified', 'created')
        # fields = ('title', 'content')

#    def __init___(self, *args, **kwargs):

#        print("\nI am in INIT in PageForm\n")

#        self.author = kwargs.pop('author')
        # self.modified = kwargs.pop('modified')
#        self.created = kwargs.pop('created')

#        print("Author in page_form: {}".format(self.author))
#        print("Created in page_form: {}".format(self.created))

#        super(PageForm, self).__init__(*args, **kwargs)

#    def clean_title(self):
#        title = self.cleaned_data['title']
#        if Page.objects.filter(author=self.author, title=title).exists():
#            raise forms.ValidationError("You have already written a book with same title.")

#        return title


    # title = forms.CharField(label="Your name", max_length=200)
    # content = forms.CharField(help_text="Write the content of your page here.")

class FriendlyForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
