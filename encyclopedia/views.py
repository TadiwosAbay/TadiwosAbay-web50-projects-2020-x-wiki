from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2

import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries":util.list_entries()
    })

def title(request,title):
    entries=util.list_entries()
    name=""
    for entry in entries:
        if title.lower()==entry.lower():
            name=entry

    if name=="":
        return render(request,"encyclopedia/EntryError.html")

    else:
        return render(request, "encyclopedia/title.html", {
           "title":name, "content": markdown2.markdown(util.get_entry(title))
        })

def get_entry(request):

    if request.method=="POST":
        entries=util.list_entries()
        title=request.POST["q"].lower()
        search_list=[]
        if util.get_entry(title):
            return HttpResponseRedirect(reverse('title',args=(title,)))
        for entry in entries:
           if title in entry.lower():
                search_list.append(entry)
        if search_list:
            return render(request,"encyclopedia/search.html",{
            "entries":search_list
           })
        else:
            return render(request,"encyclopedia/error.html"
            )

def newpage(request):
    if request.method=="POST":
        title=request.POST["title"]
        content=request.POST["Content"]
        if util.get_entry(title):
            return render(request,"encyclopedia/error.html")
        else:
            util.save_entry(title,content)
            return HttpResponseRedirect(reverse('created',args=(title,content,)))
    else:
        return render(request,"encyclopedia/newpage.html")
        

def saveNewPage(request,title,content):
    return render(request,"encyclopedia/title.html",{
    "title":title,"content":markdown2.markdown(content)
    })

def editpage(request,entry):
    return render(request,"encyclopedia/edit.html",{
         "title":entry,"content":util.get_entry(entry)
          })
def editedpage(request,title):
    if request.method=="POST":
        content=request.POST["Content"]
        util.save_entry(title,content)
        return HttpResponseRedirect(reverse('title',args=(title,)))
def randompage(request):
    entries=util.list_entries()
    selected_page=random.choice(entries)
    return render(request,"encyclopedia/title.html",{
        "title":selected_page, "content":markdowwn2.markdown(util.get_entry(selected_page))
    })
