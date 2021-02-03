from django.shortcuts import render
from .utils import search_symbol

# Create your views here.

# main view
def search(request):
    # Initializing empty dictionary
    data = {}

    if request.method == 'POST':
        output = search_symbol(request.POST.get("symbol"))
        # since output json is in format of list we need to convert it
        # to dictionary and append it
        data['result'] = output

    return render(request,'search/search.html',context=data)

# other views
