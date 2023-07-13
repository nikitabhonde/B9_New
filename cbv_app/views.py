# step 3) In 'views.py' create your views
# https://adamj.eu/tech/2021/06/30/how-to-use-httpstatus-in-django/    (use this to know how to add status_code )

from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class NewView(View):
    # # This is for get request
    def get(self, request):             # server se get request es method kai pass aayegi (to write in FBV--if request.method == 'get') 
        print("In Get Method")
        return HttpResponse('Get Response')  

    # # This is for post request
    def post(self, request):           # server se post request es method kai pass aayegi
        print("In Post Request")
        return HttpResponse('Post Response')

    # def post(self, request):           # status code method mdhe ks add kraych tya sathi hai example ghetl aahe
    #     data = request.POST
    #     nm = data.get("name")
    #     age = data.get("age")
    #     print("In Post Request")
    #     return HttpResponse('Post Response', status=HTTPStatus.CREATED)


""" Use this site to know about this {https://www.tutorialspoint.com/http/http_status_codes.htm}"""
# get request   --- To get data  -- status code 200 -- OK
# post request  --- To Add/Create data -- status code 201 -- Data Created
# put request   --- To Update data (all data pass krna pdta hai chahe hum all data update kre ya na kre)
# patch request --- To Update Partial Data
# delete request --- To delete data -- status code 204

# -------------------------------------------------------------------------------------------------------------------------------------

""" To create data --- 1) write view(EmployeeCreate) only ha 5 lines cha code  2)Go to urls nd create url for this view
use this for CBV form -- {https://www.geeksforgeeks.org/createview-class-based-views-django/}
for form -- create 'templates' folder inside app -- create 'app_name' folder inside 'templates' folder -- create 'models.html' file inside 'app_name'folder """

""" https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/?ref=lbp  all about CBV"""

from cbv_app.models import Employee
from django.views.generic.edit import CreateView

#  create view :- create or add new entries in a table in the database. 
# 1) create class in 'views.py'   2) create url of that view in 'urls.py'  3)create employee_form.html for this url & view
class EmployeeCreate(CreateView):     # CBV mdhe ha tin line cha code sufficient asto data create krayla
    model = Employee
    fields = '__all__'
    success_url = "http://127.0.0.1:8000/cbv/emp-create/"    # success_url means jo run kiya vo successfully run ho gya ab dubara kaha jaana hai vo humne url diya

    def form_valid(self, form):             # override keli hi method 'CreateView' cha 'BaseView' mdhun
            """If the form is valid, save the associated model."""
            print("Saving the data in database")     # exctly ethe data/obj save hoto
            self.object = form.save()
            return super().form_valid(form)
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List view :- display multiple instances of a table in the database (model ka all data dekhne kai liye list view)
# 1) define class in views   2) Add url in urls.py  3)create 'employee_list.html' & add condn in .html 
from cbv_app.models import Employee
from django.views.generic.list import ListView


class EmployeeList(ListView):       # by default 'object_list' hota hai .html mai bt hum usko change kr skte hai
    model = Employee                # specify the model for list view(ex: Employee)
    context_object_name ="all_employees"
    ordering = "first_name"         # get objects in alpabetical order & to get objects in reverse order '-first_name' 
    # queryset = Employee.objects.filter(is_active=1)      # if model se only active emp_obj lena hai to

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Detail View :- display one instances of a table in the database (single_obj ki information dekhne kai liye)
# 1)create view in 'views.py'   2) add url in 'url.py'   3)create 'employee_detail.html' nd add condn in .html
from django.views.generic.detail import DetailView

class EmployeeDetailView(DetailView):
    model = Employee           # sql_query -- Employee.objects.get(id=1)
    context_object_name = "single_employee"

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.

        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            return "No Data"
        return obj
    # (get_object method override keli aahe bec ti 'get' method mdhe use kraychi hoti)

    # hi method 'DetailView' cha 'BaseDetailView' mdhun override keli aahe, hi ethe bhi lihili tri code properl run honar
    def get(self, request, *args, **kwargs):    # overridden method
            self.object = self.get_object()
            if type(self.object) == str:
                return HttpResponse("No Data Found")
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# update view :- To update a particular instance of a table from the database with some extra details.
# 1)create class in views.py  2) create url in urls.py  3) use 'employee_form.html' for update
from cbv_app.models import Employee
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ["first_name", "last_name", "mobile", "email"]      # konti fields nsel pahije tr ti list mdhun remove kru shkto
    success_url = reverse_lazy("employee_list")                  # here also we use 'employee_form.html'
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# delete view :- To delete a particular instance of a table from the database(this will do hard delete)
# to do soft delete inherit the 'def delete' from DeleteView--BaseView

from cbv_app.models import Employee
from django.http import HttpResponseRedirect
# For Soft delete :- we have to override method --from 'DeleteView' cha 'BaseView' mdhun 'def delete' hi method override keli
from django.views.generic.edit import DeleteView


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = "http://127.0.0.1:8000/cbv/emp-list/"

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        # self.object.delete()       # esse hard delete hoga -- direct obj delete ho jayega
        self.object.is_active = 0    # is_active status False ho jayega means soft delete
        self.object.save()
        return HttpResponseRedirect(success_url)
    
# end of 119 video