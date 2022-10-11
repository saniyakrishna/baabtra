from django.shortcuts import render

# Create your views here.
def baabtra_home(request):
    return render(request,'baabtrasample_template/home.html')

def baabtra_courses(request):
    return render(request,'baabtrasample_template/courses.html')

def baabtra_internship(request):
    return render(request,'baabtrasample_template/internship.html')

def baabtra_details(request):
    return render(request,'baabtrasample_template/details.html')

def baabtra_about(request):
    return render(request,'baabtrasample_template/about.html')