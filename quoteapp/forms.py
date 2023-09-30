from django import forms
from quoteapp.models import Tag, Quote, Author

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']