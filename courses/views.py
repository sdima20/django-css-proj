from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from .models import Course

from .services import send_email

# Create your views here.

course_db = {
    1 : "Python Frameworks",
    2 : "SQL and Databases",
    3 : "Django Advanced Enterprise"
}

def home(request):
    # user_agent = request.headers.get('User-Agent')
    # print(user_agent)
    # return HttpResponse("Welcome to Django course platform!")
    return render(request, 'courses/home.html')

def course_detail(request, id):
    course_name = course_db.get(id, "Course not Found")
    return HttpResponse(f"Course: {course_name}")

def search(request):

    search_name = request.GET.get('name', 'Nothing Typed')

    return HttpResponse(f"Searching for: {search_name}")

def contact(request):

    if request.method == 'POST':
        print(request.POST)

        input_name = request.POST.get('username')

        return HttpResponse(f"Form processed! Hello {input_name}")

    return render(request, 'courses/contact.html')

def all_courses(request):
    courses = Course.objects.all()

    result = ''

    for course in courses:
        result += f'Title {course.title} - Price {course.price} <br>'
    
    return HttpResponse(result)

def create_course(request):

    if request.method == 'POST':

        send_email()

        title = request.POST.get('title')
        price = request.POST.get('price')

        Course.objects.create(title=title, price=price)
        return HttpResponse("Created")
    
    return render(request, 'courses/create_course.html')

def api_courses(request):
    courses = Course.objects.all()

    data = []

    for course in courses:
        data.append({'title' : course.title, 'price' : course.price})
    
    return JsonResponse(data, safe=False)