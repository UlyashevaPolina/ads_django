from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ads.models import *
from django.contrib.auth import logout, authenticate, login
from django.utils import timezone
from itertools import chain



def index(request,name = '',cat='', search = ''):
    user = ''
    my_ads = ''
    category = Category.objects.all()
    if name == '' and cat == '':
        ads = Ad.objects.all()
    elif cat == '':
        us = User.objects.get(username=name)
        ads = Ad.objects.filter(User = us)
    elif name == '':
        category_f = Category.objects.get(Name=cat)
        ads = Ad.objects.filter(Category = category_f)
    if request.method == 'POST':
        search = request.POST.get('search')
        ads = Ad.objects.filter(Title__iregex = search) or Ad.objects.filter(Description__iregex = search)
    
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        my_ads = Ad.objects.filter(User = user)
    return render(request,"index.html",{'user': user,'ads':ads, 'name': name, 'category':category, 'my_ads': my_ads})

def auth(request):
    if request.method == 'POST':
        u = request.POST.get('login')
        p = request.POST.get('psw')
        us = User.objects.get(username=u)
        if us.check_password(p):
            user = authenticate(username = u, password = p)
            login(request,user)
            return HttpResponseRedirect('/')
    return render(request, 'login.html')


def u_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        psw1 = request.POST.get('psw1')
        psw2 = request.POST.get('psw2')
        email = request.POST.get('email')
        user1 = User.objects.filter(username = username).first()
        user2 = User.objects.filter(email = email).first()
        if user1 and user2:
            error = 'Такой Email и логин уже существуют'
            return render(request, 'register.html',{'error': error})
        if user1:
            error = 'Такой логин уже существует'
            return render(request, 'register.html',{'error': error})
        if user2:
            error = 'Такой Email уже зарегистрирован'
            return render(request, 'register.html',{'error': error})
        if not psw1 == psw2:
            error = 'Пароли не совпадают'
            return render(request, 'register.html',{'error': error})
        user = User.objects.create_user(
                username=username,
                email=email,
                password=psw2,
                is_staff = True
                )
        return HttpResponseRedirect('/')
    return render(request, 'register.html')

def add_ads(request):
    user = User.objects.get(id = request.user.id)
    category = Category.objects.all()
    if request.method == 'POST':
        category = Category.objects.get(id = (request.POST.get('category')))
        title= request.POST.get('title')
        description = request.POST.get('description')
        condition = request.POST.get('condition')
        date = timezone.now()
        user = user
        ads = Ad.objects.create(
                Title = title,
                Description = description,
                Category = category,
                Сreated_at = date,
                Сondition=condition,
                User = user
                )
        ads.save()
        return HttpResponseRedirect('/')
    return render(request,'add_ads.html', {'category': category})

def edit_ads(request,id):
    user = ''
    ads=None
    try:
        if request.user.is_authenticated:
            user = User.objects.get(id = request.user.id)
            ads = Ad.objects.get(id=id,User=user)
            cat = Category.objects.exclude(id=ads.Category.id)
        if request.method=='POST':
            ads.Category_id = Category.objects.get(id = (request.POST.get('category')))
            ads.Title = request.POST.get('title')
            ads.Сondition = request.POST.get('condition')
            ads.Description=request.POST.get('description')
            ads.save()        
            return HttpResponseRedirect('/')
        return render(request,'edit_ads.html',{'ads':ads,'cat':cat})
    except:
        return HttpResponseRedirect('/')
    
def del_ads(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
    ads = Ad.objects.get(id=id)
    ads.delete()
    return HttpResponseRedirect('/')

def create_exchange(request, senderAdId, receiverAdId):
    ads_sender = Ad.objects.get(id=senderAdId)
    ads_receiver = Ad.objects.get(id=receiverAdId)
    date = timezone.now()
    if ExchangeProposal.objects.filter(ad_sender_id=senderAdId,ad_receiver_id=receiverAdId) == None:
        exchange = ExchangeProposal.objects.create(
                    ad_sender_id = ads_sender,
                    ad_receiver_id = ads_receiver,
                    status = Status.objects.get(id=1),
                    comment = '',
                    сreated_at = date
                    )
        exchange.save()
    return HttpResponseRedirect('/')

def exchange(request):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
    ads_user = Ad.objects.filter(User=user)
    offers=[]
    for ad in ads_user:
        offers.append(ExchangeProposal.objects.filter(ad_sender_id = ad))
        offers.append(ExchangeProposal.objects.filter(ad_receiver_id = ad))
    return render(request, 'exchange.html',{'offers':[f for f in offers], 'ads_user': [a.id for a in ads_user]})

def acceptOffer(request, id):
    offer = ExchangeProposal.objects.get(id = id)
    offer.status = Status.objects.get(id=2)
    offer.save()
    return HttpResponseRedirect('/exchange/')

def declineOffer(request, id):
    offer = ExchangeProposal.objects.get(id = id)
    offer.status = Status.objects.get(id=3)
    offer.save()
    return HttpResponseRedirect('/exchange/')
 





