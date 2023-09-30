from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from quoteapp.forms import AuthorForm, QuoteForm, TagForm
from  quoteapp.models import Author, Quote, Tag
# Create your views here.
def main(request):
    return render(request, 'quoteapp/index.html')

@login_required
def create_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author = author_form.save()
            return redirect('quoteapp:authors_list')
    else:
        author_form = AuthorForm()

    return render(request, 'quoteapp/create_author.html', {'author_form': author_form})

@login_required
def create_tag(request):
    if request.method == 'POST':
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag = tag_form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect('quoteapp:tags_list')
    else:
        tag_form = TagForm()

    return render(request, 'quoteapp/create_tag.html', {'tag_form': tag_form})

@login_required
def create_quote(request):
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            quote = quote_form.save()
            return redirect('quoteapp:quotes_list')
    else:
        quote_form = QuoteForm()

    return render(request, 'quoteapp/create_quote.html', {'quote_form': quote_form})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'quoteapp/authors_list.html', {'authors': authors})

def quotes_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quoteapp/quotes_list.html', {'quotes': quotes})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'quoteapp/tags_list.html', {'tags': tags})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'quoteapp/author_detail.html', {'author': author})

def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'quoteapp/tag_detail.html', {'tag': tag})

def quote_detail(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    return render(request, 'quoteapp/quote_detail.html', {'quote': quote})