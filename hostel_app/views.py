from django.shortcuts import render


# Create your views here.
def new(request):
    return render(request, "index.html")

def admn(request):
    return render(request, "index_admin.html")