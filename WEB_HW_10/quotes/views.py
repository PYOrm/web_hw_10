from django.shortcuts import render
from django.views.generic import CreateView

from .forms import TagForm
from .models import Author, Tag, Quote
from django.core.paginator import Paginator


# Create your views here.

def index(request, page=1):
    quotes = Quote.objects.all()
    item_per_page = 10
    paginator = Paginator(list(quotes), item_per_page)
    quote_on_page = paginator.page(page)
    return render(request, template_name="quotes/index.html", context={"quotes": quote_on_page})


class CreateTagView(CreateView):
    model = Tag
    template_name = "quotes/createTag.html"
    form_class = TagForm
    success_url = "createTag"