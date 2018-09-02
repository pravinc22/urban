from django.shortcuts import render
from truecallapp.forms import true_sign,job_form
def formview(request):
        formg = true_sign()
        if request.method == 'POST':
            formg = true_sign(request.POST,request.FILES or None)
            if formg.is_valid():
                formg.save(commit=True)
                return home(request)
            else :
                return render(request,'form.html',{'form':"Enter Valid Deails"})
        else:
            return render(request,'form.html',{'form':formg})
def home(request):
    return render(request,'home.html')


def careerview(request):
    return render(request,'career.html')

def jobview(request):
    job=job_form()
    if request.method== 'POST' :
        job=job_form(request.POST,request.FILES or none)
        if job.is_valid():
            job.save(commit=True)
            return render(request,'job_bengluru.html',{'job':job,'message':'Applied Succesfully'})
        else :
            return render(request,'job_bengluru.html',{'job':job,'message':'Enter Valid Details'})
    return render(request,'job_bengluru.html',{'job':job})

# Create your views here.
