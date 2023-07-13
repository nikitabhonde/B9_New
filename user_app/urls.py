from django.urls import path
from user_app import views as user_views            # 1st user_app mdhun all views import kel urls.py mdhe


urlpatterns = [
    # user_app urls
    path ('signup/', user_views.user_signup, name="user_signup"),
    path('login/', user_views.user_login, name="user_login" ),
    path('logout/', user_views.user_logout, name="user_logout")
]





# urls seprate
"""
Step 1) create urls.py file in your app then add path then import this 'from user_app import views as user_views' 
--> add below code
from django.urls import path
from user_app import views as user_views         # 1st user_app mdhun all views import kel urls.py mdhe

urlpatterns = [
    # user_app urls
    path ('signup/', user_views.user_signup, name="user_signup"),
    path('login/', user_views.user_login, name="user_login" ),
    path('logout/', user_views.user_logout, name="user_logout")
]

Step 2) Then go to main project's urls.py file & include app_urls.py file path there
--> add below code
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),

    # user app urls
    path('user/', include('user_app.urls'))
] 
"""