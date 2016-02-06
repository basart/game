from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Players, PlayersForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage
from .forms import XpForm, SearchForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from game.settings import PAGE_SIZE
# Create your views here.


def home(request):
    args = {'user': auth.get_user(request)}
    return render(request, 'home.html', args)


@login_required(login_url="/auth/login/")
def show_players(request, page_number=1):
    players = Players.objects.all()
    args = {}
    current_page = Paginator(players, PAGE_SIZE)
    args['user'] = auth.get_user(request)
    try:
        args['players'] = current_page.page(page_number)
        return render(request, 'players.html', args)
    except EmptyPage:
        messages.error(request, 'Page {} does not exist! You are on the last page.'.format(page_number))
        return redirect('/players/page/{}/'.format(current_page.num_pages))


@login_required(login_url="/auth/login/")
def show_player_form(request, player_id):
    try:
        player = Players.objects.get(id=player_id)
        form = PlayersForm(instance=player)
        args = {}
        if request.method == 'POST':
            form = PlayersForm(request.POST, instance=player)
            form.save()
            return redirect('/players/')
        else:
            args.update(csrf(request))
            args['user'] = auth.get_user(request)
            args['form'] = form
            args['player'] = player
        return render(request, 'player_form.html', args)
    except ObjectDoesNotExist:
        messages.error(request, 'Player does not exist!')
        return redirect('/players/')


@login_required(login_url="/auth/login/")
def search_player(request):
    args = {}
    args['user'] = auth.get_user(request)
    if request.method == 'GET':
        if request.GET['email']:
            email = request.GET['email']
            args['email'] = email
            try:
                args['player'] = Players.objects.get(email=email)
                return render(request, 'player.html', args)
            except ObjectDoesNotExist:
                args['email'] = email
                messages.error(request, 'Player does not exist!')
                return redirect('/players/')
        else:
            return redirect('/players/')
    return redirect('/players/')


@login_required(login_url="/auth/login/")
def change_xp(request, player_id):
    args = {}
    try:
        player = Players.objects.get(id=player_id)
        args['user'] = auth.get_user(request)
        args['player'] = player
        args['form'] = XpForm()
        args.update(csrf(request))
        if request.method == 'POST':
            form = XpForm(request.POST)
            if form.is_valid():
                xp_form = form.cleaned_data
                try:
                    xp = int(xp_form['xp'])
                    player.xp += xp
                    player.save()
                    args['player'] = player
                    if xp > 0:
                        messages.success(request, 'You added {} xp to the player {}.'.format(xp, player.nickname))
                    elif xp < 0:
                        messages.success(request, 'You written off {} xp to the player {}.'.format(abs(xp), player.nickname))
                    else:
                        messages.success(request, 'Trying added or written off {} xp for {}.'.format(abs(xp), player.nickname))
                        return render(request, 'change_xp.html', args)
                    return redirect('/players/')
                except ValueError:
                        messages.error(request, 'Value error! Trying added or written off {} xp for {}.'.format(xp_form['xp'], player.nickname))
                        return render(request, 'change_xp.html', args)
            return render(request, 'change_xp.html', args)
        else:
            return render(request, 'change_xp.html', args)
    except ObjectDoesNotExist:
        messages.error(request, 'Player does not exist!')
        return redirect('/players/')




