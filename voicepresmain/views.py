from django.shortcuts import render,redirect
from .models import Register,Patient_Details,Doctor_Table
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def logout(request):
    messages.success(request,"Succesfully Logout")
    return render(request,"index.html")

def unsucessful(request):
    return render(request,"index.html")

def login(request):
    if(request.method == "POST"):
        name=request.POST['user_name']
        password=request.POST['pwd']
        obj=Register.objects.all()
        flag=1
        for j in obj:
            if(j.name==name and j.password==password):
                #login successful
                flag=0
                dt=Doctor_Table.objects.filter(name=j.name)
                return render(request,"landingpage.html",{'ob':j.name,'dt':dt})
        if(flag==1):
            #login unsucessful
            messages.error(request,"Invalid Credentials")
            return redirect('/')
def register(request):
    if(request.method == "POST"):
        name=request.POST['reg_name']
        password=request.POST['reg_pwd']
        retype_pass=request.POST['reg_retype']
        if(password!=retype_pass):
            messages.error(request,"Password Mismatch")
            return redirect('/')
        else:
            s=Register(name=name,password=password)
            s.save()
            messages.success(request,"SignUp Successful/Login to Continue")
            return redirect('/')

def patient_register(request):
    if(request.method == "POST"):
        r=Patient_Details.objects.all().exists()
        rm=Patient_Details.objects.all()
        if(r==False):
            case_id="PID_1"
        else:
            for i in rm:
                case_id=i.case_id
            num=int(case_id[4:len(case_id)])+1
            case_id='PID_'+str(num)
        name=request.POST['name']
        email=request.POST['email']
        symptoms=request.POST['subject']
        description=request.POST['message']
        d=Patient_Details(case_id=case_id,name=name,email=email,Symptoms=symptoms,problem=description,case_status="Pending")
        d.save()
        return redirect('/')
        