import random

from django.urls import reverse
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

from . import util

class newForm(forms.Form):
    search=forms.CharField(label='Search', max_length=50)

class newTextArea(forms.Form,forms.Textarea):
    title = forms.CharField(label='Title', max_length=50)
    content=forms.CharField(label="",widget=forms.Textarea(attrs={'cols':10}))



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
            "form": newForm(),
            "text": util.get_entry(title)
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
            dane=form.cleaned_data['search']
            return HttpResponseRedirect(f"wiki/{dane}")

    return HttpResponseRedirect(f"wiki/error")

def addPage(request):
    return render(request, "encyclopedia/addPage.html", {
        "form":newForm(),
        "textArea":newTextArea()
                  })

def addForm(request):
    '''
    function that creates new website
    '''
    if request.method == "POST":
        form = newTextArea(request.POST)
        if form.is_valid():
            content=form.cleaned_data['content']
            title = form.cleaned_data['title']
            util.save_entry(title,content)
            return HttpResponseRedirect(f"/wiki/{title}")
    return HttpResponseRedirect("/wiki/error}")

def edit(request, title):
    initial_data={
        'title':title,
        'content':util.get_entry(title)
    }
    form=newTextArea(initial_data)
    return render(request, "encyclopedia/editPage.html", {
        "form": newForm(),
        "textArea": form
    })

