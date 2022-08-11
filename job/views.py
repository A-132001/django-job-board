from django.core.paginator import Paginator # pagination library
from django.shortcuts import redirect, render
from django.urls import is_valid_path ,reverse
from .models import Job
from .form import Applyers_form , Job_form
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.


def job_list(request):
    my_job_list = Job.objects.all()
    myfilter = JobFilter(request.GET,queryset=my_job_list)
    my_job_list=myfilter.qs

    paginator = Paginator(my_job_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj,'job_object':my_job_list,'myfilter':myfilter}

    return render(request,'job\job_list.html',context)



def job_details(request,slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = Applyers_form(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = Applyers_form
    context = {'job':job_detail,'form':form}
    return render(request,'job\job_details.html',context)
    
@login_required
def add_job(request):
    if request.method == 'POST':
        form = Job_form(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse("jobs:job_list"))
    else:
        form = Job_form
    return render(request,'job/add_job.html',{'form':form})