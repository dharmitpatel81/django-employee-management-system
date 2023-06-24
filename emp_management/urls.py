from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", employee_home),
    path("add-employee/", add_employee),
    path("update-employee/<int:emp_id>", update_employee),
    path("delete-employee/<int:emp_id>", delete_employee),
    path("do-update-employee/<int:emp_id>", do_update_employee),
    path("testimonials/", testimonials),
    path("feedback/", feedback),
]
