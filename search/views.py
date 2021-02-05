from django.shortcuts import render
from core.objects.stock import Stock

# Create your views here.

# main view
def search(request):
    # Initializing empty dictionary
    data = {}

    if request.method == 'POST':
        output = Stock(request.POST.get("symbol"))
        # since output json is in format of list we need to convert it
        # to dictionary and append it
        data = output.all_data('1mo')

    return render(request,'search/search.html',context=data)

# other views
