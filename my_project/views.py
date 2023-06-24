from django.http import HttpResponse
from django.shortcuts import render
import datetime 

def test(request):
    now = datetime.datetime.now()
    print(str(now))
    print("test function is called from view")
    return render(request, 'test.html',{'date': now})

def home(request):
    isActive = True

    if request.method == 'POST':
        # check = request.POST['check'] #  we get exception when we don't get any value
        check = request.POST.get('check') #  we get none when we don't get any value
        print(check)

        if check is None : isActive = False

    now = datetime.datetime.now()
    name = "LearnWithBuddy"
    list_of_programs = ["WAP to check even or odd.",
                        "WAP to check prime number.",
                        "WAP to print all prime numbers from 1 to 100.",
                        "WAP to print pascal triangles."]
    student = {
        "student_name" : "Dharmit",
        "student_college": "SAL Engineering and Technical Institute",
        "student_city" : "Ahmedabad"
    }

    data = {
       "date" : now,
       "status" : isActive,
       "name" : name,
       "list_of_programs" : list_of_programs,
       "student" : student
    }
    
    # return HttpResponse("<h2> This is Home Page</h1>")
    return render(request, 'home.html', data)

def about(request):
    # return HttpResponse("<h2> This is About Page</h1>")
    return render(request, 'about.html', {})


def services(request):
    # return HttpResponse("<h2> This is Services Page</h1>")
    return render(request, 'services.html', {})

