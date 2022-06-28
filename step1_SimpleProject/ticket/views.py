from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import TicketAdminForm
from .models import TicketModel
# Create your views here.


def HomeView(request):
    tickets = TicketModel.objects.all()
    print(tickets)
    context = { 'tickets': tickets}
    return render(request,'ticket/main.html', context=context)

def ticketView(request):
    form = TicketAdminForm()
    if request.method == "POST":
        print(request.POST)
        form = TicketAdminForm(request.POST ,  request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("Form is not valid ")

    context = {'form': form}
    return render(request, 'ticket/createticket.html', context)