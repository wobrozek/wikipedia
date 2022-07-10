import random

from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

from . import util

class newForm(forms.Form):
    search=forms.CharField(label='Szukaj tematu ', max_length=50)

def index(request):
    '''
    show all websites (entries)
    '''
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form":newForm()
    })

def wiki(request , title):
    '''
        if page entries exist show it else display error page
    '''
    if(util.get_entry(title))!=None:
        return render(request, "encyclopedia/wiki.html", {
            "title": title,
            "form": newForm()
                      })
    else:
        return render(request, "encyclopedia/wiki.html", {
            "title": "Page not found",
            "form":newForm()
    })

def randomWiki(request):
    '''
    function that select random page from a list of entries
    '''
    list=util.list_entries()
    wikiIndex=random.randint(0,len(list)-1)
    return HttpResponseRedirect(f"wiki/{list[wikiIndex]}")


def wikiForm(request):
    '''
    function that gives form data to function wiki
    '''
    if request.method == "POST":
        form = newForm(request.POST)
        if form.is_valid():
            dane=form.cleaned_data['search'];
            return HttpResponseRedirect(f"wiki/{dane}")

    return HttpResponseRedirect(f"wiki/error")


