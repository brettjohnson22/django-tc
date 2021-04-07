from django.shortcuts import redirect, render


def group_redirect(request):
    if request.user.groups.filter(name="Customers").exists():
        return redirect('/customers/')
    elif request.user.groups.filter(name="Employees").exists():
        return redirect('/employees/')
    else:
        return render(request, 'home.html')