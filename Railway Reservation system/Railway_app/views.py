from django.shortcuts import render
from .models import Add_Train,Passenger

def home(request):
    return render(request,'Home.html')

def about(request):
    return render(request, 'About.html')

def homepage(request):
    return render(request, 'Home.html')

def contact_us(request):
    return render(request,'contact.html')

def user_page(request):
    return render(request, 'user.html')

def trainuser(request):
    trains = Add_Train.objects.all()  
    context = {'trains': trains}  
    return render(request, 'trainuser.html', context)  

def booking(request):
    return render(request,'booking.html')

def saveenquiry(request):
    if request.method=='POST':
        name=request.POST.get('fname')
        age1=request.POST.get('Age')
        trainname=request.POST.get('Trainname')
        trainno=request.POST.get('Trainnumber')
        cardno=request.POST.get('cardno')
        cardname=request.POST.get('cardholder')
        gender=request.POST.get('gender')
        data=booking('full_name=name','age=age1','gender=gender','train_no_id=trainno','card_holder_name=cardname','card_number=cardno','train_name=trainname')
        data.save()
    return render(request,"booking.html")

def payment(request):
    return render(request,'payment.html')


def train_shedule(request):
    trains = Add_Train.objects.all()  
    context = {'trains': trains} 
    return render(request, 'train_shedule.html', context)  

def success(request):
    return render(request,'successful.html')