from django.shortcuts import render, redirect
from .forms import TicketingUserForm
# Create your views here.


def HomeView(request):
    return render(request,'user/main.html')

def indexView(request):
    form = TicketingUserForm()
    if request.method == "POST":
        print(request.POST)
        form = TicketingUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'user/index.html', context)