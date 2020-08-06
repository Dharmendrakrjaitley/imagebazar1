from django.http import HttpResponse
from django.shortcuts import render,redirect
# from django.contrib import messages
from myapp.models import *
from django.db.models import Q
from myapp.forms import *
# from django.shortcuts import render_to_response


def show_about_page(request):
    print("from view")
    return render(request,'about.html')
    #return HttpResponse("hello sir")


def show_home_page(request):

    cats=Category.objects.all()
    images = Image.objects.all()

    data = {'images': images,'cats':cats}

    return render(request,'home.html',data)    



def show_category_page(request, cid):
    #print(cid)
    category=Category.objects.get(pk=cid) #it will give category name
    #print(category)

    cats=Category.objects.all()
    images = Image.objects.filter(cat=category)

    data = {'images': images,'cats':cats}

    return render(request,'home.html',data)    



def home(request):
    return redirect('/home')


def searchresult(request):
    search_string=request.GET.get('search_string')

    cats=Category.objects.all()
    #images=Image.objects.filter(Q(title__icontains=search_string) | Q(description__icontains=search_string))
    images = Image.objects.filter(title__icontains=search_string) | Image.objects.filter(description__icontains=search_string )
    if images:
        data = {'images': images,'cats':cats,'search_string':search_string}
    else:
        images=Image.objects.all()    
        data = {'images': images,'cats':cats,'search_string':search_string}

    return render(request,'search_results.html',data)



# def upload_image(request):
#     return render(request,'upload.html')   

def uploadTo(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            message="Uploaded Successfully!"
            # return render_to_response('upload.html',message="Uploaded Successfully!")
            form=ImageForm();
            context={'message':message,'form':form}
            return render(request,'upload.html',context)
    else:
        form=ImageForm();

    return render(request,'upload.html',{'form':form})            
