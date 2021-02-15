"""views for app pynilha."""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404
from django.template import loader
import json

# Create your views here.

from .models import Receitas, Despesas, Aplicacoes

# É possível trocar 'get' por 'get_object_or_404'
# -> get_object_or_404(Receitas,mes_receitas='janeiro')
# ou pesquisar sobre 'get_list_or_404()' que usa 'filter' no lugar de get

jsonReceitas = [
    ['Salário', 0],
    ['Aluguel AP', 0],
    ['Outras Receitas', 0],
    ['Saldo Anterior', 0],
]
jsonDespesas = [
    ['Aluguel', 0],
    ['Cagece', 0],
    ['Enel', 0],
    ['Internet', 0],
    ['Plano de Saúde', 0],
    ['Supermercado', 0],
    ['Combustível', 0],
    ['Educação', 0],
    ['Saques-Débito', 0],
    ['Financiamento AP', 0],
    ['Auxílio Mãe', 0],
    ['Filhos', 0],
    ['Cartão Crédito', 0],
    ['Netflix', 0],
    ['Outras Despesas', 0],
]
jsonAplicacoes = [
    ['Previdência', 0],
    ['Fundo Reserva', 0],
    ['Investimentos', 0],
    ['Compras Futuras', 0],
    ['Amortização AP', 0],
    ['Outras Aplicações', 0],
]

context = {
    'lista_receitas': '',
    'lista_despesas': '',
    'lista_aplicações': '',
    'saldo_parcial': '',
    'saldo_final': '',
    'readonly': True,
    'errorMessage': '',
    'mes_visualizado': '',
}


def mes_com_acentos(mes_a_mudar):
    """Retorna Mês com Maiúsculas e Acentos."""
    meses_a_exibir = {
        'janeiro': 'Janeiro',
        'fevereiro': 'Fevereiro',
        'marco': 'Março',
        'abril': 'Abril',
        'maio': 'Maio',
        'junho': 'Junho',
        'julho': 'Julho',
        'agosto': 'Agosto',
        'setembro': 'Setembro',
        'outubro': 'Outubro',
        'novembro': 'Novembro',
        'dezembro': 'Dezembro',
    }
    return meses_a_exibir[mes_a_mudar]


def index(request):
    """Return Index pynilha."""
    return render(request, 'pynilhaapp/page_pynilha.html')


def mes(request):
    """Return Mes atual."""
    return render(request, 'pynilhaapp/page_month.html', context)


def mes_detalhado(request, mes_a_detalhar):
    """Return Mes atual."""
    """Buscando Receitas Database"""
    try:
        lista_receitas_db = Receitas.objects.get(mes_receitas=mes_a_detalhar)
        lista_receita_decode = json.loads(lista_receitas_db.list_salario)
    except Receitas.DoesNotExist:
        lista_receita_decode = jsonReceitas.copy()
    somaTotalReceitas = 0
    for k in range(0, len(lista_receita_decode)):
        somaTotalReceitas += float(lista_receita_decode[k][1])
    lista_receita_decode.append(['TOTAL RECEITAS',
                                f'{somaTotalReceitas:.2f}'])
    for k in range(0, len(lista_receita_decode)):
        lista_receita_decode[k][1] = \
            f'{float(lista_receita_decode[k][1]):.2f}'

    """Buscando Despesas Database"""
    try:
        lista_despesas_db = Despesas.objects.get(mes_despesas=mes_a_detalhar)
        lista_despesa_decode = json.loads(lista_despesas_db.list_despesas)
    except Despesas.DoesNotExist:
        lista_despesa_decode = jsonDespesas.copy()
    somaTotaDespesas = 0
    for k in range(0, len(lista_despesa_decode)):
        somaTotaDespesas += float(lista_despesa_decode[k][1])
    lista_despesa_decode.append(['TOTAL DESPESAS',
                                f'{somaTotaDespesas:.2f}'])
    for k in range(0, len(lista_despesa_decode)):
        lista_despesa_decode[k][1] = \
            f'{float(lista_despesa_decode[k][1]):.2f}'

    """Buscando Aplicaçoes Database"""
    try:
        lista_aplicacoes_db = \
            Aplicacoes.objects.get(mes_aplicacoes=mes_a_detalhar)
        lista_aplicacao_decode = json.loads(
            lista_aplicacoes_db.list_aplicacoes)
    except Aplicacoes.DoesNotExist:
        lista_aplicacao_decode = jsonAplicacoes.copy()
    somaTotaAplicacoes = 0
    for k in range(0, len(lista_aplicacao_decode)):
        somaTotaAplicacoes += float(lista_aplicacao_decode[k][1])
    lista_aplicacao_decode.append(['TOTAL APLICAÇÕES',
                                  f'{somaTotaAplicacoes:.2f}'])
    for k in range(0, len(lista_aplicacao_decode)):
        lista_aplicacao_decode[k][1] = \
            f'{float(lista_aplicacao_decode[k][1]):.2f}'

    """Colocando Dados na variável de contexto"""
    context['mes_visualizado'] = mes_com_acentos(mes_a_detalhar)
    context['lista_receitas'] = lista_receita_decode
    context['lista_despesas'] = lista_despesa_decode
    context['lista_aplicações'] = lista_aplicacao_decode
    context['saldo_parcial'] = f'{(somaTotalReceitas-somaTotaDespesas):.2f}'
    context['saldo_final'] = \
        f'''{(somaTotalReceitas-somaTotaDespesas-somaTotaAplicacoes):.2f}'''
    return render(request, 'pynilhaapp/page_month.html', context)


def editar(request, mes_a_detalhar):
    """Editar dados."""
    context['readonly'] = False
    return render(request, 'pynilhaapp/page_month.html', context)


def confirmar_dados_receitas(request, mes_a_detalhar):
    """Cofirmar dados receitas."""
    context['readonly'] = True
    jsonReceitas[0][1] = float(request.POST['Receita1'])
    jsonReceitas[1][1] = float(request.POST['Receita2'])
    jsonReceitas[2][1] = float(request.POST['Receita3'])
    jsonReceitas[3][1] = float(request.POST['Receita4'])
    #    context['errorMessage'] = 'Erro na Alteração/Inclusão dos Dados'
    #    return HttpResponseRedirect('/pynilhaapp/mes_teste',context)
    try:
        lista_receitas_db = Receitas.objects.get(mes_receitas=mes_a_detalhar)
    except Receitas.DoesNotExist:
        lista_receitas_db = Receitas(mes_receitas=mes_a_detalhar)
    lista_receitas_db.list_salario = json.dumps(jsonReceitas)
    lista_receitas_db.save()
    return HttpResponseRedirect(f'/pynilhaapp/mes/{mes_a_detalhar}/')


def confirmar_dados_despesas(request, mes_a_detalhar):
    """Cofirmar dados despesas."""
    context['readonly'] = True
    jsonDespesas[0][1] = float(request.POST['Despesa1'])
    jsonDespesas[1][1] = float(request.POST['Despesa2'])
    jsonDespesas[2][1] = float(request.POST['Despesa3'])
    jsonDespesas[3][1] = float(request.POST['Despesa4'])
    jsonDespesas[4][1] = float(request.POST['Despesa5'])
    jsonDespesas[5][1] = float(request.POST['Despesa6'])
    jsonDespesas[6][1] = float(request.POST['Despesa7'])
    jsonDespesas[7][1] = float(request.POST['Despesa8'])
    jsonDespesas[8][1] = float(request.POST['Despesa9'])
    jsonDespesas[9][1] = float(request.POST['Despesa10'])
    jsonDespesas[10][1] = float(request.POST['Despesa11'])
    jsonDespesas[11][1] = float(request.POST['Despesa12'])
    jsonDespesas[12][1] = float(request.POST['Despesa13'])
    jsonDespesas[13][1] = float(request.POST['Despesa14'])
    jsonDespesas[14][1] = float(request.POST['Despesa15'])
    #    context['errorMessage'] = 'Erro na Alteração/Inclusão dos Dados'
    #    return HttpResponseRedirect('/pynilhaapp/mes_teste',context)
    try:
        lista_despesas_db = Despesas.objects.get(mes_despesas=mes_a_detalhar)
    except Despesas.DoesNotExist:
        lista_despesas_db = Despesas(mes_despesas=mes_a_detalhar)
    lista_despesas_db.list_despesas = json.dumps(jsonDespesas)
    lista_despesas_db.save()
    return HttpResponseRedirect(f'/pynilhaapp/mes/{mes_a_detalhar}/')


def confirmar_dados_aplicacoes(request, mes_a_detalhar):
    """Cofirmar dados aplicações."""
    context['readonly'] = True
    jsonAplicacoes[0][1] = float(request.POST['Aplicacao1'])
    jsonAplicacoes[1][1] = float(request.POST['Aplicacao2'])
    jsonAplicacoes[2][1] = float(request.POST['Aplicacao3'])
    jsonAplicacoes[3][1] = float(request.POST['Aplicacao4'])
    jsonAplicacoes[4][1] = float(request.POST['Aplicacao5'])
    jsonAplicacoes[5][1] = float(request.POST['Aplicacao6'])
    #    context['errorMessage'] = 'Erro na Alteração/Inclusão dos Dados'
    #    return HttpResponseRedirect('/pynilhaapp/mes_teste',context)
    try:
        lista_aplicacoes_db = \
            Aplicacoes.objects.get(mes_aplicacoes=mes_a_detalhar)
    except Aplicacoes.DoesNotExist:
        lista_aplicacoes_db = Aplicacoes(mes_aplicacoes=mes_a_detalhar)
    lista_aplicacoes_db.list_aplicacoes = json.dumps(jsonAplicacoes)
    lista_aplicacoes_db.save()
    return HttpResponseRedirect(f'/pynilhaapp/mes/{mes_a_detalhar}/')


def home(request):
    """Return Home django."""
    return render(request, 'pynilhaapp/home_django.html')
