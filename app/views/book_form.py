import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required  # add this to make login required to all the FBV
from django.shortcuts import HttpResponse, redirect, render

from app.models import Book

# Create your views here.
# FBV : Function Base Views

log = logging.getLogger("first")

""" 2) forms.ModelForm """
""" path('form_view/', form_view, name="form_view") eske liye bhi yhi url use kiya hai"""
from app.forms import BookForm


@login_required
def form_view(request):
    if request.method == "POST":
        log.info("Inside Post reuest in book form")      # Just to check that which request is working, here we can also use print() 
        data = request.POST
        # print(data)                                    # Just to print data in cansole that we get from our website
        form = BookForm(data)
        if form.is_valid():
            print("Inside form's if condition")
            form.save()
        messages.success(request, "Book added Successfully from 'form_view'.")
        return redirect("show_books")
    elif request.method == "GET":
        print("Inside get request")                      # Use print() always to check that we are going inside this condition
        log.info("Inside get request in book form")
        return render(request, "book_form_test.html", {"bookform" : BookForm()}) 
   













""" This for Explanation purpose only not related to our Library-Project """
""" 1) forms.Form """
""" path('form_view/', form_view, name="form_view") eske liye bhi yhi url use kiya hai"""
# from .forms import Input_form
# def form_view(request):               # FBV add kiya hai views.py mai for forms.py file

# # # 2 ways to write Input_form
# # 1st way
#     print(Input_form())               # html code cmd mai create krke mila
#     return render(request, "form_test.html", {"form": Input_form()})


# # 2nd way
#     # context = {}
#     # context['form'] = Input_form()
#     # return render(request, "form_test.html", context)     # context mai dict pass krna hota hai to FBV kai niche dict bnae nd return mai pass ki