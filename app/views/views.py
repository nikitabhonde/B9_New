import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required  # add this to make login required to all the FBV
from django.shortcuts import HttpResponse, redirect, render

from app.models import Book

# Create your views here.
# FBV : Function Base Views

log = logging.getLogger("first")

@login_required
def welcome_page(request):
#    return HttpResponse("Welcome to Library Application")
    log.info("In Welcome Page")
    # messages.success(request, "Welcome To Our Application.")
    return render(request, "welcome.html")           # .html file mai jo bhi likha hai vo sb google mai show hoga 

import datetime


@login_required
def show_all_books(request):
    books = Book.objects.filter(is_active=True)          # get only active books records for database
    log.info("Showing All Books..!")
    return render(request, "showbooks.html", {"allbooks": books, "today": datetime.datetime.now()})    # {"allbooks": books} likhne se ye hua ki hum sb books showbooks.html m leke ja rhe 


@login_required
def show_single_book(request, bid):
    try:
        book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        log.error("Invalid Id Passed..!")
        return HttpResponse("Book does not exist...!")
    messages.info(request, f"{book_obj.name} showing this book..!")
    return render(request=request, template_name="bookdetail.html",context={"book":book_obj})






















""" Niche kai all code baki views mai seprate kiye hai"""

# def common_var(req):                # For Common methods 
#     final_dict = req.POST
#     book_name = final_dict.get("nm")
#     book_price = final_dict.get("prc")
#     book_qty = final_dict.get("qty")
#     book_is_pub = final_dict.get("ispub")
#     return book_name, book_price, book_qty, book_is_pub


# @login_required
# def add_single_book(request):
#     if request.method == "POST":                    # POST request page vr value lihay sathi
#         book_name, book_price, book_qty, book_is_pub = common_var(request)
#         if book_is_pub == "YES":
#             is_pub = True
#         else:
#             is_pub = False

#         Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_published=is_pub)
#         log.info("Book has been added successfully...!")
#         messages.success(request, "Book has been added successfully...!")        # this is django-msg jo humme book add hone kai baad dikhana hai to ye msg ka code showbooks.html mai likhna pdega
#         return redirect("show_books")
            
    
#         # print(request.POST)          # gives us QueryDict of all object
#         # print("In POST request")
#     elif request.method == "GET":             # GET request ti value page kdun data base mdhe ghay sathi
#         request.GET                           # to fetch query parameters(?)
#         return render(request, "addbook.html")


# @login_required
# def edit_single_book(request, bid):
#     book_obj = Book.objects.get(id=bid)
#     if request.method == "GET":
#         return render(request, "bookedit.html", {"single_book":book_obj})
#     elif request.method == "POST":
#         book_name, book_price, book_qty, book_is_pub = common_var(request)
#         if book_is_pub == "YES":
#             is_pub = True
#         else:
#             is_pub = False

#         # update data
#         book_obj.name = book_name
#         book_obj.price = book_price
#         book_obj.qty = book_qty
#         book_obj.is_published = is_pub
#         book_obj.save()
#         messages.success(request, f"Book: {book_obj.name} has been updated successfully...!")
#         return redirect("show_books")



# @login_required
# def delete_single_book(request, bid):        # delete POST request mai krna hai
#     book_obj = Book.objects.get(id=bid)
#     book_obj.delete()                        # hard delete (database se hi gayab ho jayega)
#     messages.success(request, f"Book: {book_obj.name} has been deleted succcessfully...!" )
#     return redirect("show_books")


# @login_required
# def soft_delete_single_book(request, bid):
#     book_obj = Book.objects.get(id=bid)
#     book_obj.is_active = False              # soft delete bss is_active status False(0) ho jayega
#     messages.success(request, f"Book: {book_obj.name} has been moved to inactive books...!" )
#     book_obj.save()         
#     return redirect("In_active_book")


# @login_required
# def In_active_book(request):
#     book_obj = Book.objects.filter(is_active=False)
#     return render(request, "Inactivebook.html", {"allbooks":book_obj, "today": datetime.datetime.now()} )


# @login_required
# def restore_single_book(request, bid):
#     book_obj = Book.objects.get(id=bid)
#     book_obj.is_active = True
#     messages.success(request, f"Book: {book_obj.name} has been restore succcessfully..!" )
#     book_obj.save()
#     return redirect("show_books")


# --------------- for forms -------------------- #
""" 3) crispy-forms"""
""" path('form_view/', form_view, name="form_view") eske liye bhi yhi url use kiya hai"""
# from .forms import AddressForm
# def form_view(request):
#     return render(request, "form_test.html", {"form": AddressForm})


# """ 2) forms.ModelForm """
# """ path('form_view/', form_view, name="form_view") eske liye bhi yhi url use kiya hai"""
# from app.forms import BookForm

# @login_required
# def form_view(request):
#     if request.method == "POST":
#         log.info("Inside Post reuest in book form")      # Just to check that which request is working, here we can also use print() 
#         data = request.POST
#         # print(data)                                    # Just to print data in cansole that we get from our website
#         form = BookForm(data)
#         if form.is_valid():
#             print("Inside form's if condition")
#             form.save()
#         messages.success(request, "Book added Successfully from 'form_view'.")
#         return redirect("show_books")
#     elif request.method == "GET":
#         print("Inside get request")                      # Use print() always to check that we are going inside this condition
#         log.info("Inside get request in book form")
#         return render(request, "book_form_test.html", {"bookform" : BookForm()}) 
   


# """ This for Explanation purpose only not related to our Library-Project """
# """ 1) forms.Form """
# """ path('form_view/', form_view, name="form_view") eske liye bhi yhi url use kiya hai"""
# # from .forms import Input_form
# # def form_view(request):               # FBV add kiya hai views.py mai for forms.py file

# # # # 2 ways to write Input_form
# # # 1st way
# #     print(Input_form())               # html code cmd mai create krke mila
# #     return render(request, "form_test.html", {"form": Input_form()})


# # # 2nd way
# #     # context = {}
# #     # context['form'] = Input_form()
# #     # return render(request, "form_test.html", context)     # context mai dict pass krna hota hai to FBV kai niche dict bnae nd return mai pass ki