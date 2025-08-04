from django.shortcuts import render, redirect
from .utils import spin_reels, calculate_payout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.



@login_required
def play(request):
    profile = request.user.profile

    BET_OPTIONS = [1, 2, 5, 10, 20]
    try:
        bet = int(request.GET.get('bet', 1))
    except ValueError:
        bet = 1
    if bet not in BET_OPTIONS:
        bet = 1
    if profile.balance < bet:
        return render(request, 'slot/play.html', {
            'error': "Insufficient balance. Please deposit more credits.",
            'balance': profile.balance,
            'bet': bet,
            'bets': BET_OPTIONS,
        })

    profile.balance -= bet  # cost per spin

    result = spin_reels()
    single_payout = calculate_payout(result)      # e.g. 0 for losing spin, 2 for a 1x win
    payout = single_payout * bet


    profile.balance += payout
    profile.save()

    is_win = payout > 0
    return render(request, 'slot/play.html', {
        'reels': result,
        'payout': payout,
        'is_win': payout > 0,
        'balance': profile.balance,
        'bet': bet,
        'bets': BET_OPTIONS,
    })
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('play')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_every_which_way(request):
    logout(request)
    return redirect('play')

