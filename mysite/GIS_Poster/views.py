from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from .forms import PosterCreateForm, CourseForm, PosterEditForm
from .models import Course, Poster
from django.views.generic.edit import UpdateView

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
                print ('ERROR')
                print (form.errors)
        else:
            form = PosterCreateForm()
        return render(request, 'GIS_Poster/poster_create.html', {'form': form})

class Course_add():
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
                return render_to_response('GIS_Poster/new_post.html')
        else:
            form = CourseForm()
        return render(request, 'GIS_Poster/course_create.html', {'form': form})

class Poster_update():
    def edit_poster(request):
        #pass poster model record name to poster_create which could be able to create and update existing record
        #print ("METHOD IS POST" + request)
        form = PosterEditForm(request.POST, request.FILES)
        print (request.POST.get('first'))
        poster = Poster.objects.filter(StudentName=request.POST.get('first'))
        print (poster)
        #print ("METHOD IS POST")

        if request.method == "POST":
             print ("METHOD IS POST")
             if form.is_valid():
                 form.save()
                 return render(request, 'GIS_Poster/poster_create.html', {'form': poster})
                 #return render_to_response('GIS_Poster/new_post.html')
        else:
             form = PosterEditForm()
             print ("REQUEST>POST IS :" + request.POST.get('first'))
        #print (request.POST)
        return render(request, 'GIS_Poster/poster_create.html', {'form': form})
        # if request.is_ajax():
        #     data = serializers.serialize('json', posters)
        #     return HttpResponse(data, 'json')
        # else:
        #     return render_to_response('GIS_Poster/poster_update_form.html', {'first_name':posters}, context=RequestContext(request))
        # if request.method == "POST":
        #     form = PosterEditForm(request.POST)
        #     print (request.POST.get('first'))
        #     if form.is_valid:
        #         return HttpResponseRedirect('GIS_Poster/new_post.html')
        
        # return render(request, 'GIS_Poster/poster_update_form.html', {'form': form})
        # model = Poster
    # fields = ['first_name']
    # template_name_suffix = '_update_form'

    # def get_object(self, *args, **kwargs):
    #     poster = get_object_or_404(first_name, pk=self.kwargs['pk'])

    #     # We can also get user object using self.request.user  but that doesnt work
    #     # for other models.

    #     return poster

    # def get_success_url(self, *args, **kwargs):
    #     return reverse("poster/new")
  