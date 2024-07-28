from django.shortcuts import render

# Create your views here.
#creating a view for just testing the initiation FEEL FREE TO ERASE IT 

def testing(request):
    return render(request, 'handleData/index.html', {'message':"hello world"})