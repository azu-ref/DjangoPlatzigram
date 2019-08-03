#Platzigram urls module
from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path('sorted/', views.sort_numbers),
    path('hi/<str:name>/<int:age>', views.say_hi)
]
