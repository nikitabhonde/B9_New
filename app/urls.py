from django.urls import path
from app import views as library_views      #  views as library_views --> means views ka name change krke usko library_views kr rhe hai


urlpatterns = [

    # book_app or library app urls
    path('home/', library_views.welcome_page, name="home_page"),    # name="home_page" is nick name for home/ agr jisko aaage operations mai use krenge
                                                                    # home/ this is link jo kbhi bhi change ho skti hai bt nick_name change nhi hoga 
                                                                    # nick_name ka use humne welcome.html file mai kiya hai
    path('show-books/', library_views.show_all_books, name="show_books"),
    path('show-single-book/<int:bid>/', library_views.show_single_book, name="show_single_book"),
    path('add-single-book/', library_views.add_single_book, name="add_single_book"),
    path('edit-single-book/<int:bid>/', library_views.edit_single_book, name="edit_single_book"),
    path('delete-single-book/<int:bid>/', library_views.delete_single_book, name="delete_single_book"),
    path('soft-delete-single-book/<int:bid>/',library_views.soft_delete_single_book, name="soft_delete_single_book"),
    path('In-active-book/', library_views.inactivebook, name="In_active_book" ),
    path('restore-single-book/<int:bid>/', library_views.restore_single_book, name="restore_single_book"),
    path('form-view/', library_views.form_view, name="form_view"),
    path('create-activebook-csv/', library_views.create_activebook_csv, name="create_activebook_csv"),
    path('create-inactivebook-csv/', library_views.create_inactivebook_csv, name="create_inactivebook_csv" ),
    path('create-activebook-excel/', library_views.create_activebook_excel, name="create_activebook_excel"),
    path('create-inactivebook-excel/', library_views.create_inactivebook_excel, name="create_inactivebook_excel"),
    path('upload-csv/', library_views.upload_csv, name="upload_csv"),
    path('upload-sample-csv', library_views.upload_sample_csv, name="upload_sample_csv")
    



] 







# from app.views import (add_single_book, delete_single_book, edit_single_book,
#                        form_view, show_all_books, show_single_book,
#                        soft_delete_single_book, welcome_page, In_active_book)
