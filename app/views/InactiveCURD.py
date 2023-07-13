import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required     # add this to make login required to all the FBV
from django.shortcuts import HttpResponse, redirect, render

from app.models import Book

log = logging.getLogger("first")

import datetime

@login_required
def inactivebook(request):
    book_obj = Book.objects.filter(is_active=False)
    return render(request, "Inactivebook.html", {"allbooks":book_obj, "today": datetime.datetime.now()} )


@login_required
def restore_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.is_active = True
    messages.success(request, f"Book: {book_obj.name} has been restore succcessfully..!" )
    book_obj.save()
    return redirect("show_books")




