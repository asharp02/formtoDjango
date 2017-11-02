from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from .forms import PosterCreateForm
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
            both_names = request.POST.get('first_name') + '_' + request.POST.get('last_name')
            poster.StudentName = both_names
            s_years = get_years(request.POST.get('Semester'), request.POST.get('Year'))
            path = both_names + '_' + request.POST.get('Course') + '_' + request.POST.get('Year')
            #poster.SDrivePathway = #'S:/Posters/GIS Posters/' + s_years + 'PostersComplete' + request.POST.get('Semester') + request.POST.get('Year') + '/' # + add course path here, add new model field first
            poster.ThumbnailName = path + '_' + 'thumbnail'
            #poster.ThumbnailPath = request.POST.get('first_name', '')
            poster.PosterPath = path
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

def get_years(semester, year):
    if(semester == 'Fall'):
        return str(year) + '-' + str(year+1)
    else:
        return str(year-1) + '-' + str(year)

