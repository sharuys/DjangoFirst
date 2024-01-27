from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
#from views import home


urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('', include('polls.urls'))
]
def home(request):
    return render(request, 'home.html')
