# (117) csv(download & upload) & excel(download) file handling
import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render
from app.models import Book

log = logging.getLogger("first")


"""  To read website data & convert to CSV file, Excel file """
#  ---> If we want all book --> Book.objects.all() --> use this

import csv 

@login_required
def create_activebook_csv(request): 
    try:                                            
        response = HttpResponse(content_type='text/csv')                            # this will create csv file bt sys mai download nhi hoga
        response['Content-Disposition'] = 'attachment; filename="Activebook.csv"'         
    
        writer = csv.writer(response)
        writer.writerow(['Name', 'Price', 'Qty', 'Is_published', 'Is_active'])      # To create headers in csv-file

        # Book.objects.filter(is_active=True) this condition will give all active_books
        books = Book.objects.filter(is_active=True).values_list('name', 'price', 'qty', 'is_published', 'is_active')
        for book in books:
            writer.writerow(book)
        log.info("Active Book CSV file created Successfully..!")
    except Exception as e:
        print(e)
    return response
    


@login_required
def create_inactivebook_csv(request):
    try:
        response = HttpResponse(content_type='text/csv')                            # this will create csv file bt sys mai download nhi hoga
        response['Content-Disposition'] = 'attachment; filename="In_Activebook.csv"' 
            
        writer = csv.writer(response)
        writer.writerow(['Name', 'Price', 'Qty', 'Is_published', 'Is_active'])      # To create headers in csv-file
        
        # Book.objects.filter(is_active=False) this condition will give all Inactive_books
        books = Book.objects.filter(is_active=False).values_list('name', 'price', 'qty', 'is_published', 'is_active')
        for book in books:
            writer.writerow(book)
        log.info("In Active Book CSV file created Successfully..!")
    except Exception as e:
        print(e)
    return response



import xlwt
@login_required 
def create_activebook_excel(request):
    try:
        response = HttpResponse(content_type='application/ms-excel')                   # to create Excel_file
        response['Content-Disposition'] = 'attachment; filename="Active_Books.xls"'
     
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Active_book')                                                # to give sheet_name

        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['Name', 'Price', 'Qty', 'Is_Published', 'Is_active', ]               # to create headers
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        # Book.objects.filter(is_active=True) this condition will give all active_books
        book = Book.objects.filter(is_active=True).values_list('name', 'price', 'qty', 'is_published', 'is_active')
        for row in book:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        log.info("Active Book Excel file created Successfully..!")
    except Exception as e:
        print(e)
    else: 
        wb.save(response)
        messages.success(request, "Active Book Excel file Downloaded Successfully..!")
    return response



@login_required 
def create_inactivebook_excel(request):
    try:
        response = HttpResponse(content_type='application/ms-excel')                       # to create Excel_file
        response['Content-Disposition'] = 'attachment; filename="InActive_Books.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('In_Active_book')                                                 # to give sheet_name

        # Sheet header, first row
        row_num = 0
        columns = ['Name', 'Price', 'Qty', 'Is_Published', 'Is_active', ]                   # to create headers

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num])

        # Condition to get inactive_books --> Book.objects.filter(is_active=False)
        book = Book.objects.filter(is_active=False).values_list('name', 'price', 'qty', 'is_published', 'is_active')
        for row in book:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num])
        log.info("In Active Book Excel file created Successfully..!")
    except Exception as e:
        print(e)
    else:
        wb.save(response)
    return response


#  raw query --- using objects.raw (select * from books;) -- csv mai dalna hai


""" https://stackoverflow.com/questions/24704630/how-to-upload-and-read-csv-file-in-django-using-csv-dictreader"""
# when we get data from site it's in the from of string we want to convert it to True,False that's why we use line(135,136,137,138,139)
@login_required
def upload_csv(request):
    try:
        file = request.FILES["csv_file"]
        data = file.read().decode('utf-8').splitlines()
    # To check website & csv file che headers match hotat ki nhi
        expected_header_list = ["name", "price", "qty", "is_published"]
        expected_header_list.sort()
        actual_header_list = data[0].lower().split(",")             # data mdhe all csv print houn midel bt we want header only-- thats why[0] & then split headers "split(",")"
        actual_header_list.sort()
        print(expected_header_list, actual_header_list)
        if expected_header_list != actual_header_list:
            log.error("actual_headers & expected_headers are not equal")
            return HttpResponse("Error Occures... Headers are not equal...! ")
        
        # print(data)                           # To print CSV-file data in our cmd/cansole
        reader = csv.DictReader(data)           # This will give CSV data in the form of dict ""Always use DictReader""
        lst = []
        for ele in reader:
            is_pub = ele.get("Is_Published")    # Use this to check that Book-- Is_Published status
            if is_pub == "TRUE":
                is_pub = True
            else:
                is_pub = False
            lst.append(Book(name=ele.get("Name"), price=ele.get("Price"), qty=ele.get("Qty"), is_published=is_pub))
    except Exception as e:
        print(e)
    else:
        Book.objects.bulk_create(lst)
        messages.success(request, "CSV File Uploded Successfully..!")
        log.info("CSV File Uploded Successfully..!")
    return redirect("show_books")


@login_required
def upload_sample_csv(request):
    return HttpResponse("Not complete")
    # https://pythoncircle.com/post/30/how-to-upload-and-process-the-csv-file-in-django/