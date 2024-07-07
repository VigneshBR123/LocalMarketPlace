import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import userdetails,freelancer_register_page
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    profession_s=professionals.objects.filter(Status=1)
    profess_ions=Profession.objects.filter(Emergant_freelancer=1)
    return render(request,'index.html', {"profession_s":profession_s,"profess_ions":profess_ions})

def registeration(request):
    form_details=userdetails()
    if request.method=='POST':
        form_details=userdetails(request.POST)
        if form_details.is_valid():
            form_details.save()
            messages.success(request,'Account created successfully. Please SignIn')
            return redirect('/signin')
    return render(request,'registeration_page.html',{'form_details':form_details})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=name,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request,'Invalid username or password')
                return redirect('/signin')
        return render(request,'login_page.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out successfully')
        return redirect('/')

def freelancer_register_form(request):
    frm=freelancer_register_page()
    return render(request,'freelancer_register_2.html',{'frm':frm})

def freelancer_register_form2(request):
    if request.user.is_authenticated:
        return render(request,'freelancer_register_page.html')
    else:
        messages.warning(request,"Please SignIn To Create New Profile.")
        return redirect('/signin')

def professional(request):
    profession=Profession.objects.filter(Status=1)
    return render(request,'professionals.html',{"profession":profession})

def specalists(request):
    if request.user.is_authenticated:
        specalists=specialist.objects.filter(user=request.user)
        return render(request,'specalists.html',{"specalists":specalists})
    else:
        messages.warning(request,"Please SignIn To Access Specialist Page.")
        return redirect('/signin')

def remove_specalist(request,sid):
    spec_pro=specialist.objects.get(id=sid)
    spec_pro.delete()
    return redirect('/specalists')

def professionals_2(request,Profession_category):
    if(Profession.objects.filter(Profession_category=Profession_category,Status=1)):
        profiles=professionals.objects.filter(Profession__Profession_category=Profession_category)
        return render(request,'profiles.html',{"profiles":profiles,"Profession_category":Profession_category})
    else:
        messages.warning(request,"No such professionals in our platform.")
        return redirect('/professionals')

def pro_details(request,cname,proname):
        if(Profession.objects.filter(Profession_category=cname,Status=1)):
            if(professionals.objects.filter(Name=proname,Status=1)):
                if request.user.is_authenticated:
                    pro_details=professionals.objects.filter(Name=proname,Status=1)
                    return render(request,'pro_details.html',{'pro_details':pro_details})
                else:
                    messages.warning(request,"Please SignIn To Continue.")
                    return redirect('/signin')
            else:
                messages.warning(request,"No Such Professionals In Our Platform.")
                return redirect('/professionals')

        else:
            messages.warning(request,"No Such Professionals In Our Platform.")
            return redirect('/professionals')

def add_to_specialist(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            professional_id=data['pid']
            #print(request.user.id)
            profile_status=professionals.objects.get(id=professional_id)
            if profile_status:
                if specialist.objects.filter(user=request.user.id,profession_id=professional_id):
                    return JsonResponse({'status':'Professional Already in Specalist'},status=200)
                else:
                    specialist.objects.create(user=request.user,profession_id=professional_id)
                    return JsonResponse({'status':'Professional Added to Specalist'},status=200)
        else:
            return JsonResponse({'status':'Please Login To Continue'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
