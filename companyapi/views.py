from django.http import HttpResponse
#function
def home_page(request):
    print("home page requested")
    return HttpResponse("this is home page")