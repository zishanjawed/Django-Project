
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.people_form, name='people_insert'),   # GET and POST request for insert operations
    path('<int:id>/', views.people_form, name='people_update'),  # GET and POST request for update operations
    path('delete/<int:id>/', views.people_delete, name='people_delete'), # Delete entry from database 
    path('list/', views.people_list, name='people_list'), # GET request to retrive and display all records

]
