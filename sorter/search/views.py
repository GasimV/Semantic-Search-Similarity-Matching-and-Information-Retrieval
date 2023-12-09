import sys
import os
sys.path.append(os.path.dirname(os.path.abspath("_faiss.py")))

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .other._faiss import sorted_data

class Doccument_sorted(TemplateView):
    template_name = "index.html"

def search_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', "")
        data = sorted_data(search_query)
    return render(request, 'search.html', context={"data":data})
