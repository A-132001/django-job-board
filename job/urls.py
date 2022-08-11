from msilib.schema import ListView
from django.urls import path,include
from . import views
from .api import job_list_api,api_job_details,Applyers_List,Applyers_details,JobList,JobListDetails
app_name = 'job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_details,name='job_detail'),

    #views
    path('api/jobs',job_list_api,name='job_list_api'),
    path('api/jobs/<int:id>',api_job_details,name='api_job_details'),
    path('api/applyers/',Applyers_List,name='Applyers_List'),
    path('api/applyers/<int:id>',Applyers_details,name='Applyers_details'),

    #generic views
    path('api/v2/jobs',JobList.as_view(),name='job_list_api'),
    path('api/v2/jobs/<int:id>',JobListDetails.as_view(),name='job_list_details'),
    

]
