from django.shortcuts import render

# Create your views here.
def sec(request):
     d={'name':'usernot defined'}
     return render(request,'sec.html',context=d)


