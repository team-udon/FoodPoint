from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'foodpointMain.html')

def signIn(request):
    return render(request, 'signIn.html')

def introduce(request):
    return render(request, 'introduce.html')

def register(request):
    return render(request, 'registerStore-signUp.html')

def search(request):
    return render(request, 'searchResult.html')