from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = print(request.POST["username"])
        password = print(request.POST["password"])
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증 실패")

        
    return render(request,"users/login.html")    

def logout_view(request):
    logout(request)
    return redirect("user:login")