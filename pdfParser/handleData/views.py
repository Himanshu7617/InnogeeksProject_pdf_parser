from django.shortcuts import render

# Create your views here.
#creating a view for just testing the initiation FEEL FREE TO ERASE IT 

def homePage(request):
    return  render(request,"index.html")