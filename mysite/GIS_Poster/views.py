from django.shortcuts import render
from .forms import PosterCreateForm
# Create your views here.
def poster_new(request):
	form = PosterCreateForm()
	return render(request, 'GIS_Poster/poster_create.html', {'form': form})