from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import AuthForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if request.POST.get('next') != '':
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/players/')
            else:
                args['login_error'] = "User not found"
                args['form'] = AuthForm()
                return render(request, 'login.html', args)
        else:
            args['login_error'] = "error"
            args['form'] = AuthForm()
            return render(request, 'login.html', args)
    else:
        args['form'] = AuthForm()
        return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")
