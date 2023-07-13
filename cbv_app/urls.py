#  step 4) create 'urls.py' file inside your app nd creter view for the class that we created in 'models.py' & give url for that view in 'url.py' file 
# step 5) include that url in main_app urls.py file

from django.urls import path
from cbv_app.views import NewView, EmployeeCreate, EmployeeList, EmployeeDetailView,EmployeeUpdateView,EmployeeDeleteView

urlpatterns = [
    path('new-cview/', NewView.as_view()),
    path('emp-create/', EmployeeCreate.as_view(), name="employee_create" ),
    path('emp-list/', EmployeeList.as_view(), name="employee_list" ),
    path('emp-view/<pk>/', EmployeeDetailView.as_view(), name="employee_view"),   # <pk> is identification for id field,
    path('emp-update-view/<pk>/', EmployeeUpdateView.as_view(), name="employee_update_view"),   # <pk> is identification for id field,
    path('emp-delete-view/<pk>/', EmployeeDeleteView.as_view(), name="employee_delete_view"),    # <pk> is identification for id field,

]

# http://127.0.0.1:8000/cbv/new-cview/
# http://127.0.0.1:8000/cbv/emp-create/
# http://127.0.0.1:8000/cbv/emp-list/
# http://127.0.0.1:8000/cbv/emp-view/1/    # <pk> means primery key
# http://127.0.0.1:8000/cbv/emp-update-view/<pk>/
# http://127.0.0.1:8000/cbv/emp-delete-view/<pk>/





