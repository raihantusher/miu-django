from django.shortcuts import render
#models
from .models import Sett,Question,Answer

#forms
from . import forms

from django.contrib.auth.decorators import login_required

# Create your views here.


def join(request):

    context={
        "form":forms.NameForm,
        
    }

    if "set_uuid" in request.POST:
        set_uuid=request.POST["set_uuid"]

        user=request.user
        print("hello")
        print(user.is_superuser)
        sett=Sett.objects.filter(uuid__exact=set_uuid)[0]
        
        
        sett.users.add(user)
        
       


        context.update({'name':set_uuid})
    else:
       
        context.update({'name':"yahoo"})

    return render(request,"vaseline/student/join.html",context)



def setlist(request):
    context={
        "sets":Sett.objects.filter(users__id__exact=request.user.id),
    }
    return render(request,"vaseline/student/setlist.html",context)



def set(request,id):
    context={
        "id":id,
        "questions":Question.objects.filter(sett_id__exact=id),
    }
    return render(request,'vaseline/student/set.html',context)


def question(request,id):
    q=Question.objects.filter(id=id).get()
    if request.POST:
        ans=Answer(ans="hello")
        ans.user=request.user
        ans.right=False
        ans.question=q
        ans.save()

    context={
        "id":id,
        "question":Question.objects.filter(id__exact=id).get()
    }
    return render(request,'vaseline/student/question.html',context)