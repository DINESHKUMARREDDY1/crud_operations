from django.shortcuts import render
from app.models import *
from django.db.models import Q


# Create your views here.
def insert_topic(request):
    tn=input('enter topic :')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    QSTO=topic.objects.all()
    d={'QSTO':QSTO }
    return render(request,'display_topic.html',d)

def display_topic(request):
    QSTO=topic.objects.all()
    QSTO=topic.objects.filter(topic_name='Cricket')
    QSTO=topic.objects.exclude(topic_name='Cricket')

    d={'QSTO':QSTO }
    return render(request,'display_topic.html',d)



def insert_webpage(request):
    tn=input('enter topic-name:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter URL : ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    to.save()
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO }
    return render(request,'display_webpage.html',d)


def display_webpage(request):
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(Q(topic_name='Cricket') | Q(name__contains='n'))
    QSWO=webpage.objects.filter(Q(topic_name='pro') | Q(name__contains='n'))
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(name='dinesh').update(url='https://dinu.com')
    QSWO=webpage.objects.filter(name='nani').update(name='kavita')
    QSWO=webpage.objects.filter(name='kavita').update(url='https://kavita.com')
    QSWO=webpage.objects.filter(name='sai').delete()
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO }
    return render(request,'display_webpage.html',d)

def update_webpage(request):
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(name='dinesh').update(url='https://dreddy.com')
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO }
    return render(request,'display_webpage.html',d)


def delete_webpage(request):
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(name='reddy').delete()
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO }
    return render(request,'display_webpage.html',d)












def insert_accessrecords(request):
    tn=input('enter topic-name:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter URL : ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    to.save()
    a=input('enter author :')
    d=input('enter date :')
    e=input('enter email :')
    ao=accessrecords.objects.get_or_create(name=wo,author=a,date=d,email=e)[0]
    ao.save()
    QSAR=accessrecords.objects.all()
    d={'QSAR':QSAR }
    return render(request,'display_webpage.html',d)

def display_accessrecords(request):
    QSAR=accessrecords.objects.all()
    d={'QSAR':QSAR }
    return render(request,'display_accessrecords.html',d)
