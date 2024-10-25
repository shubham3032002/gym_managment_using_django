from django.shortcuts import render,redirect,get_object_or_404
from .models import  GYM_details
# Create your views here.


def home(request):
    
    return render(request,'home.html')


def register(request):
    
    if request.method =='POST':
         name=request.POST.get("name")
         m_number=request.POST.get("m_number")
         age=request.POST.get("age")
         height=request.POST.get("height")
         weight=request.POST.get("weight")
         plan=request.POST.get("plan")
         gender=request.POST.get("gender")
         
         print(name,m_number,age,height,weight,plan,gender)
         query=GYM_details(name=name,m_number=m_number,age=age,height=height,weight=weight,plan=plan,gender=gender)
         query.save()
    
    return render(request,'register.html')


def data(request):
    data=GYM_details.objects.all()
    context={"data":data}
    
    return render(request,'data.html',context)


def about_us(request):
    
    return render(request,'about.html')

def contact(request):
    
    return render(request,'contact.html')

def update(request, id):
    d = GYM_details.objects.get(id=id)
    
    if request.method == 'POST':
        d.name = request.POST.get("name")
        d.m_number = request.POST.get("m_number")
        d.age = request.POST.get("age")
        d.height = request.POST.get("height")
        d.weight = request.POST.get("weight")
        d.plan = request.POST.get("plan")
        d.gender = request.POST.get("gender")
        d.save()

        return redirect('data')  # Redirect to the data page after updating

    context = {"d": d}
    return render(request, 'update.html', context)

def delete(request, id):
    d = get_object_or_404(GYM_details, id=id)
    
    d.delete()  
    return redirect('data') 
