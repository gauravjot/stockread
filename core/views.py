from django.shortcuts import render

# Create your views here.

# main view
def core(request, *args,**kwargs):
    return render(request, 'core/core.html', {})

# other views
