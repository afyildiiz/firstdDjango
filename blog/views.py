from django.shortcuts import render
from .models import Category,Movies

# category_list=["Macera","Aksiyon","Dram"]
# basliklar=["Film Adi","Aciklama","Resim"]
# movies_list=[
#     {
#         'id':1,
#         'film_adi':'Zindan Adasi',
#         'film_aciklama':'aciklama',
#         'film_img':"1.jpg",
#         'anasayfada':True
#     },
#         {
#         'id':2,
#         'film_adi':'Maskeli Besler',
#         'film_aciklama':'aciklama',
#         'film_img':'2.jpg',
#         'anasayfada':False
        
#     },
#     {
#         'id':3,
#         'film_adi':'Babam ve Oglum',
#         'film_aciklama':'aciklama',
#         'film_img':'3.jpg',
#         'anasayfada':True
#     },
#     {
#         'id':4,
#         'film_adi':'Piyanist',
#         'film_aciklama':'aciklama',
#         'film_img':'4.jpg',
#         'anasayfada':False
#     }
             
#              ]


def home(request):
    data = {
        "movies":Movies.objects.all(),
        "categories":Category.objects.all()
    }
    return render(request,"index.html",data)

def about(request):
    data={
        "movies":Movies.objects.all(),
        "categories":Category.objects.all()
    }
    return render(request,'about.html',data)

def movieDetails(request,id):
    data = {
        'movies':Movies.objects.get(id=id)
    }
    return render(request,'details.html',data)