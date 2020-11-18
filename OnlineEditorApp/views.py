from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, request
from django.contrib import messages
import csv
from .models import *
import pandas as pd
from django.db.models import Q



# Create your views here.

def base(request):
    print(request.method)
    a = "Welcome To Code Practice"

    return HttpResponse(a)


def home(request):

    return render(request,'home.html')

def arrays(request):

    return render(request, 'arrays.html')

def arrayTraverse(request):
    return render(request, 'arrayTraverse.html')

def arrayInsert(request):
    return render(request, 'arrayInsertion.html')

def arrayDelete(request):
    return render(request, 'arrayDeletion.html')

def arraySearch(request):
    return render(request, 'arraySearch.html')

def arrayUpdate(request):
    return render(request, 'arrayUpdate.html')

def arrayIQuestions(request):
    return render(request, 'array_IQuestions.html')