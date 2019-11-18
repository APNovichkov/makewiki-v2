from django import forms
from wiki.models import Page


class PageForm(forms.Form):
    """ Render and process a form based on the Page model. """

    title = forms.CharField(label="Your name", max_length=200)
    content = forms.CharField(help_text="Write the content of your page here.")
