from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import PosterCreateForm, CourseForm, PosterEditForm, PosterSearchForm
from .models import Course, Poster
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
import json
from django.core.exceptions import ValidationError

"""takes in a semester as a string and a year and returns the school-year
range as a string"""
def get_years(semester, year):
    if(semester == 'Spring'):
        prev_year = int(year) - 1
        return str(prev_year) + '-' + str(year)
    else:
        next_year = int(year) + 1
        return str(year) + '-' + str(next_year)

class Poster_add():

    def poster_new(request):
        if request.method == "POST":
            form = PosterCreateForm(request.POST, request.FILES)
            if form.is_valid():
          
                poster = form.save(commit=False)
                """before saving the poster to the Django database, we extract
                the fields necessary to use when forming the SDrivePathway
                and the thumbnail name/path."""
                semester = request.POST.get('Semester')
                year = request.POST.get('Year')
                course = request.POST.get('Course_name')
                course_code = course.split('_')[0]
                dept_code = course.split('_')[1]
                f_name = request.POST.get('first_name')
                l_name = request.POST.get('last_name')
                both_names = l_name + '_' + f_name
                poster.StudentName = both_names

                school_years = get_years(semester, year)

                pdf_name = both_names + '_' + course_code + '_' + year
                
                print (str(school_years))
                poster.SDrivePathway =  'S:/Posters/GIS Posters/' +'/' + str(school_years) + '/' + 'PostersComplete' + semester + year + '/' + course + '/' + pdf_name
                poster.ThumbnailName = pdf_name + '_' + 'thumbnail'
                poster.PosterPath = pdf_name
                
                poster.Dept_code = dept_code
                poster.Course_code = course_code
                poster.Year_range = school_years
                poster.save()
                messages.success(request, 'Poster added successfully')
                return render_to_response('GIS_Poster/new_post.html')
            else:
                print (form.errors)
        else:
            form = PosterCreateForm()
        return render(request, 'GIS_Poster/poster_create.html', {'form': form})

class Course_add():
    @login_required
    def course_new(request):
        if request.method == "POST":
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                course = form.save(commit=False)
                name = request.POST.get('Course_code')
                dept = request.POST.get('Dept_code')
                
                course.Course_Dept = name + "_" + dept
                course.save()
                messages.success(request, 'Poster added successfully')
                return render_to_response('GIS_Poster/new_course.html')
        else:
            form = CourseForm()
        return render(request, 'GIS_Poster/course_create.html', {'form': form})

class PosterSearch():
    @login_required
    def poster_search(request):
        if request.method == "POST":
            form = PosterSearchForm(request.POST, request.FILES)
            if form.is_valid():
                pos_name = request.POST.get('poster_name')
                # try:
                poster_pk = Poster.objects.get(FullPosterTitle=pos_name).pk
                return redirect('/poster/update/' + str(poster_pk))
        #         except:
                    
        #             #raise ValidationError(('Invalid value'),code='invalid')
        # #            render(request, 'GIS_Poster/poster_search', {'form':form})

        else:
            form = PosterSearchForm()
        return render(request, 'GIS_Poster/poster_search.html', {'form': form})


class PosterUpdate(UpdateView):
    model = Poster
    #fields = '__all__'
    # form_class = PosterCreateForm
    template_name = 'GIS_Poster/poster_update_form.html'
    form_class = PosterEditForm
     
    #success_url = ('<h1>No Page Here</h1>') 
    success_url = ('/poster/success')

class PosterSuccess():
    @login_required
    def poster_success(request):
        return render_to_response('GIS_Poster/new_post.html')
