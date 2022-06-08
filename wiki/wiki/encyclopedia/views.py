from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

from . import util

class newForm(forms.Form):
    search=forms.CharField(label='Szukaj tematu ', max_length=50)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form":newForm()
    })

def wiki(request , title):
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

def wikiForm(request):
    if request.method == "POST":
        form = newForm(request.POST)
        if form.is_valid():
            dane=form.cleaned_data['search'];
            if(util.get_entry(dane)!=None):
                return HttpResponseRedirect(f"wiki/{dane}")

    return HttpResponseRedirect(f"wiki/error")


