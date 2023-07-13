import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required     # add this to make login required to all the FBV
from django.shortcuts import HttpResponse, redirect, render

from app.models import Book

log = logging.getLogger("first")

def common_var(req):                # For Common methods 
    final_dict = req.POST
    book_name = final_dict.get("nm")
    book_author = final_dict.get("aur")
    book_price = final_dict.get("prc")
    book_qty = final_dict.get("qty")
    book_publication_date = final_dict.get("pdate")
    book_is_pub = final_dict.get("ispub")
    return book_name, book_author, book_price, book_qty, book_publication_date, book_is_pub


@login_required
def add_single_book(request):
    if request.method == "POST":                    # POST request page vr value lihay sathi
        book_name, book_author, book_price, book_qty, book_publication_date, book_is_pub = common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False

        Book.objects.create(name=book_name, author=book_author, price=book_price, qty=book_qty, publication_date=book_publication_date, is_published=is_pub)
        log.info("Book has been added successfully...!")
        messages.success(request, "Book has been added successfully...!")        # this is django-msg jo humme book add hone kai baad dikhana hai to ye msg ka code showbooks.html mai likhna pdega
        return redirect("show_books")
            
    
        # print(request.POST)                 # gives us QueryDict of all object
        # print("In POST request")
    elif request.method == "GET":             # GET request ti value page kdun data base mdhe ghay sathi
        request.GET                           # to fetch query parameters(?)
        return render(request, "addbook.html")


@login_required
def edit_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    if request.method == "GET":
        return render(request, "bookedit.html", {"single_book":book_obj})
    elif request.method == "POST":
        book_name,book_author, book_price, book_qty,book_publication_date, book_is_pub = common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False

        # update data
        book_obj.name = book_name
        book_obj.author = book_author
        book_obj.price = book_price
        book_obj.qty = book_qty
        book_obj.publication_date = book_publication_date
        book_obj.is_published = is_pub
        book_obj.save()
        messages.success(request, f"Book: {book_obj.name} has been updated successfully...!")
        return redirect("show_books")



@login_required
def delete_single_book(request, bid):        # delete POST request mai krna hai
    book_obj = Book.objects.get(id=bid)
    book_obj.delete()                        # hard delete (database se hi gayab ho jayega)
    messages.success(request, f"Book: {book_obj.name} has been deleted succcessfully...!" )
    return redirect("show_books")


@login_required
def soft_delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.is_active = False              # soft delete bss is_active status False(0) ho jayega
    messages.success(request, f"Book: {book_obj.name} has been moved to inactive books...!" )
    book_obj.save()         
    return redirect("In_active_book")