from django.shortcuts import render, redirect
from . forms import PeopleForm
from .models import People
from django.core.paginator import Paginator

# Create your views here.

def people_list(request):
    user_list = People.objects.all().order_by('name')
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'people_register/people_list.html',{ 'users': users })



def people_form(request,id=0):
    # deal with insert and update oprations 
    if request.method == "GET":
        if id==0:
            form=PeopleForm()
        else:
            people=People.objects.get(pk=id)
            form=PeopleForm(instance=people)
        return render(request,'people_register/people_register.html',{'form':form}) 
    else:
        if id==0:
            form = PeopleForm(request.POST)
        else:
           people=People.objects.get(pk=id)
           form=PeopleForm(request.POST,instance=people) 
        x=form.is_valid()
        print(form.errors)
        if x:
            user = form.save()
            return redirect('/people/list/')
        else:
            return render(request,'people_register/people_register.html',{'form':form})


def people_delete(request,id):
    people=People.objects.get(pk=id)
    people.delete()
    return redirect('/people/list')

