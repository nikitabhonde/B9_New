"""
URL configuration for B9__Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # book_app or library app urls
    path('book/', include('app.urls')),          # app_name.urls

    # user app urls
    path('user/', include('user_app.urls')),     # app_name.urls

    # cbv_app urls
    path('cbv/', include('cbv_app.urls'))       # app_name.urls


] 



# Patterns/url patterns/urls/endpoint ---
# http://127.0.0.1:8000/admin/

# # ----->> book_app or book urls <<------ #
# http://127.0.0.1:8000/book/home/
# http://127.0.0.1:8000/book/show-books/
# http://127.0.0.1:8000/book/show-single_book/1/   ---> 1 means id yenar
# http://127.0.0.1:8000/book/add-single-book/
# http://127.0.0.1:8000/book/edit-single-book/1/
# http://127.0.0.1:8000/book/delete-single-book/1/
# http://127.0.0.1:8000/book/soft-delete-single-book/1/
# http://127.0.0.1:8000/book/form-view/


# # ------->> user_app urls <<---------- #
# http://127.0.0.1:8000/user/signup/
# http://127.0.0.1:8000/user/login/
# http://127.0.0.1:8000/user/logout/


# # ------->> cbv_app urls <<---------- #
# http://127.0.0.1:8000/cbv/new-cview/

