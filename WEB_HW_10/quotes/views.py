from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
from sqlalchemy import func, desc, create_engine, select
from sqlalchemy.orm import Session, sessionmaker


# Create your views here.
def index(request):
    authors_list = ""
    return HttpResponse(authors_list)
