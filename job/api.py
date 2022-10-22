from dataclasses import dataclass
import imp
from multiprocessing.spawn import import_main_path
from turtle import Turtle
from .models import Job , Applyers
from .serializers import SerializerModel,SerializerApplyersModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

#views

@api_view(["Get"])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data  = SerializerModel(all_jobs,many=True).data
    return Response({'data':data})


@api_view(["Get"])
def api_job_details(request,id):
    job_detail = Job.objects.get(id=id)
    data  = SerializerModel(job_detail).data
    return Response({'data':data})

@api_view(["Get"])
def Applyers_List(request):
    Applyer = Applyers.objects.all()
    data  = SerializerApplyersModel(Applyer,many=True).data
    return Response({'data':data})

@api_view(["Get"])
def Applyers_details(request,id):
    applyer_details = Applyers.objects.get(id=id)
    data  = SerializerApplyersModel(applyer_details).data
    return Response({'data':data})

#generic views
class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = SerializerModel

class JobListDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializerModel
    queryset = Job.objects.all()
    lookup_field = 'id'
    


