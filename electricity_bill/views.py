from django.shortcuts import render
from electricity_bill.forms import ElectricityBillForm
# Create your views here.

def index(request):
    form = ElectricityBillForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        print(request.POST)
        print('é valido?:',form.is_valid())
        if request.POST['leitura_anterior'] != [''] or request.POST['leitura_atual'] != ['']:
            leitura_anterior = float(request.POST['leitura_anterior'])
            leitura_atual = float(request.POST['leitura_atual'])
            consumo = leitura_atual - leitura_anterior
            if consumo < 0:
                error = 'Você errou as leituras!'
                context['error'] = error
                return render(request,'electricity_bill/index.html',context)
        elif request.POST['consumo'] != [''] :
            consumo = float(request.POST['consumo'])
        else:
            error = {'error':'Erro desconhecido!'}
            context['error'] = error
            return render(request,'electricity_bill/index.html',context)
        fatura = consumo*0.45
        context['consumo'] = consumo
        context['fatura'] = fatura
        
        
    return render(request,'electricity_bill/index.html',context)