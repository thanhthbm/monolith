from django.shortcuts import redirect

def home(request):
    if request.session.get("customer_id"):
        return redirect("/books/")
    return redirect("/accounts/login/")
