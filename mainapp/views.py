from django.shortcuts import render
from .models import category,altcategory,product,creator
# Create your views here.

def mainpage(request):
    giyimaltkategoriler=altcategory.objects.filter(category=category.objects.get(categoryname="giyim"))
    çantaaltkategoriler=altcategory.objects.filter(category=category.objects.get(categoryname="çanta"))
    aksesuaraltkategoriler=altcategory.objects.filter(category=category.objects.get(categoryname="aksesuar"))
    hediyelikaltkategoriler=altcategory.objects.filter(category=category.objects.get(categoryname="hediyelik"))
    content={"giyimaltkategori":giyimaltkategoriler,
            "çantaaltkategori":çantaaltkategoriler,
            "aksesuaraltkategori":aksesuaraltkategoriler,
            "hediyelikaltkategori":hediyelikaltkategoriler}
    return render(request,"index.html",content)
