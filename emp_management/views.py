from django.shortcuts import render, redirect

# from django.http import HttpResponse
from .models import Employee, Testimonial, Feedback
from .forms import FeedbackForm


# Create your views here.
def employee_home(request):
    emps = Employee.objects.all()
    # return HttpResponse("Employee Home Page")
    return render(request, "employee/home.html", {"emps": emps})


def add_employee(request):
    if request.method == "POST":
        # print("data is coming...")

        # data fetch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        # validate

        # create model object and set data
        emp = Employee()
        emp.name = emp_name
        emp.emp_id = emp_id
        emp.phone = emp_phone
        emp.address = emp_address
        emp.department = emp_department
        if emp_working is None:
            emp.working = False
        else:
            emp.working = True

        # save the object
        emp.save()

        # prepare message
        # msg = "Data is Saved"

        return redirect("/")
    return render(request, "employee/add_emp.html",{})


# update interface
def update_employee(request, emp_id):
    emp = Employee.objects.get(pk=emp_id)
    return render(request, "employee/update_emp.html", {"emp": emp})


# update handler
def do_update_employee(request, emp_id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        emp = Employee.objects.get(pk=emp_id)
        emp.name = emp_name
        emp.emp_id = emp_id
        emp.phone = emp_phone
        emp.address = emp_address
        emp.department = emp_department
        if emp_working is None:
            emp.working = False
        else:
            emp.working = True

        emp.save()
    return redirect("/")


def delete_employee(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    emp.delete()
    return redirect("/")


def testimonials(request):
    testi = Testimonial.objects.all()
    return render(request, "employee/testimonials.html", {"testi": testi})


def feedback(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])
            print(form.cleaned_data["feedback"])

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            feedback = form.cleaned_data["feedback"]

            formData = Feedback()

            formData.name = name
            formData.email = email
            formData.feedback = feedback

            formData.save()

            print("Data Saved...")

            return redirect("/")
        else:
            return render(request, "employee/feedback.html", {"form": form})

    else:
        form = FeedbackForm()  # create new form obj and render via template
        return render(request, "employee/feedback.html", {"form": form})
