from django.shortcuts import render

def console(request):
    return render(request, "ecom_console/console.html")
