from django.contrib import admin
from .models import Employee, Testimonial, Feedback

# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ("name", "working", "emp_id", "phone", "address", "department")
    list_editable = ("working", "emp_id")
    search_fields = ("name", "phone")
    list_filter = ("working",)


admin.site.register(Employee, EmpAdmin)
admin.site.register(Testimonial)
admin.site.register(Feedback)
