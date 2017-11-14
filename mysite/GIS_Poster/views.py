from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from .forms import PosterCreateForm, CourseForm
from .models import Course
# Create your views here.
def poster_new(request):
    print("This is at beginning post method")
    if request.method == "POST":
        print("This is post method")
        form = PosterCreateForm(request.POST, request.FILES)
        #print(form.errors)
        if form.is_valid():
            print("Form is valid")
            poster = form.save(commit=False)

            semester = request.POST.get('Semester')
            year = request.POST.get('Year')

            course = request.POST.get('Course_name')
            course_code = get_course_code(course)
            dept_code = get_dept(course)
            f_name = request.POST.get('first_name')
            l_name = request.POST.get('last_name')
            both_names = l_name + '_' + f_name
            poster.StudentName = both_names

            school_years = get_years(semester, year)

            pdf_name = both_names + '_' + course_code + '_' + year
            poster.SDrivePathway = 'S:/Posters/GIS Posters/' + school_years + '/' + 'PostersComplete' + semester + year + '/' + course_code + '_' + dept_code + '/' + pdf_name
            poster.ThumbnailName = pdf_name + '_' + 'thumbnail'
            #poster.ThumbnailPath = request.POST.get('first_name', '')
            poster.PosterPath = pdf_name
            
            # course = request.POST.get('Course_name')
            poster.Dept_code = dept_code
            poster.Course_code = course_code
            poster.save()
            print("saved form")
            messages.success(request, 'Poster added successfully')
            return render_to_response('GIS_Poster/new_post.html')
        else:
            print ('ERROR')
            print (form.errors)
    else:
        form = PosterCreateForm()
    return render(request, 'GIS_Poster/poster_create.html', {'form': form})

def get_dept(course_num):
    course_obj = Course.objects.filter(pk=course_num)
    dc_list = course_obj.values_list('Dept_code', flat=True)
    return dc_list[0]

def get_course_code(course_num):
    course_obj = Course.objects.filter(pk=course_num)
    cc_list = course_obj.values_list('Course_code', flat=True)
    return cc_list[0]

def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Poster added successfully')
            return render_to_response('GIS_Poster/new_post.html')
    else:
        form = CourseForm()
    return render(request, 'GIS_Poster/course_create.html', {'form': form})

def get_years(semester, year):
    if(semester == 'Fall'):
        next_year = int(year) + 1
        return year + '-' + str(next_year)
    else:
        prev_year = int(year) - 1
        return str(prev_year) + '-' + year