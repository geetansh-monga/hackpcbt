from django.shortcuts import render

def website_view(request):
    return render(request,'website/index.html')