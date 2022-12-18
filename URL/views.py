from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import LongtoShort
# Create your views here.
def helloworld(request):
    return HttpResponse("Hello")

def task(request):
    context={"year":"2022",
    "name":"rohan",
    "alp":["a", "b", "c"]}
    return render(request, "task.html", context)

def proj(request):
    print(request.method)
    context={
        "submitted": False, 
        "error":False 
        }  #error for checking if the alias name is already taken
    if request.method=="POST":
        print(request.POST)
        data=request.POST
        try:
            longurl=data['longurl']
            customname=data['custom_name']
            context["long_url"]=longurl
            context["submitted"]=True #a url submitted by the user
            context["custom_name"]=request.build_absolute_uri() + customname  #to build url
            print(longurl, customname)
            obj=LongtoShort(long_url=longurl, custom_name=customname)  #add data in db
            obj.save()
            context["date"]=obj.created_date
            context["clicks"]=obj.vist_count
        except:
            context["error"]=True 
    else:
        print("Not submitted")
    return render(request, "index.html", context)

def redirect_to(request, customname):
    row=LongtoShort.objects.filter(custom_name=customname)
    print(row)
    if len(row)==0:
        return HttpResponse("This endpoint is not defined yet!!!")
    obj=row[0]
    longurl=obj.long_url
    obj.vist_count+=1
    obj.save()
    return redirect(longurl)

def anal_ytics(request):
    rows=LongtoShort.objects.all()
    context={
        "rows":rows
    }
    return render(request, "analytics.html", context)