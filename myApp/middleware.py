from django.shortcuts import redirect

def auth(function):
    def wrapper(request):
        if request.user.is_authenticated == False:
            return redirect("login")
        return function(request)
    return wrapper


def guest(function):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect("index")
        return function(request)
    return wrapper