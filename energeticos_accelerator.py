# Define a função que calcula o total geral
def compute_total(value=0, ornament=False):
    result = value + icms(value) + ipi(value) + pis(value) + cofins(value)
    return result if ornament is False else format_value(result)


# Define a função que calcula o imposto ICMS sobre o valor da mercadoria
def icms(value=0, ornament=False):
    result = value * 18/100
    return result if ornament is False else format_value(result)


# Define a função que calcula o imposto IPI sobre o valor da mercadoria
def ipi(value=0, ornament=False):
    result = value * 4/100
    return result if ornament is False else format_value(result)


# Define a função que calcula o imposto PIS sobre o valor da mercadoria
def pis(value=0, ornament=False):
    result = value * 1.86/100
    return result if ornament is False else format_value(result)


# Define a função que calcula o imposto COFINS sobre o valor da mercadoria
def cofins(value=0, ornament=False):
    result = value * 8.54/100
    return result if ornament is False else format_value(result)


# Define uma função para formatar os valores monetários
def format_value(value=0, coin='R$'):
    return f'{coin}{value:.2f}'.replace('.', ',')


# Cria uma lista para receber os dados temporariamente
data = list()
# Cria uma lista que receberá os dados da lista data
data_clients = list()

print('===== BEM-VINDO(a) AO SISTEMA DE CÁLCULO DE TRIBUTAÇÃO =====\n'
      'Alíquoas de impostos atual:\nICMS: 18%\nIPI: 4%\nPIS: 1,86%\nCOFINS: 8,54%\n'
      'Para gerar os valores, preencha os campos abaixo.')
print()

while True:
    # Recebe o nome do cliente, quantidade de enérgicos e guarda na lista data
    data.append(input("Cliente: "))
    amount_commodity = int(input("Quantidade da mercadoria comprada: "))
    price_commodity = amount_commodity * 4.50   # Calcula o valor da mercadoria
    data.append(price_commodity)
    data_clients.append(data[:])    # Adiciona os dados da lista data para a data_clients
    data.clear()    # Limpa a lista data

    check = input('Cadastrar outro cliente? [S/N] ').lower()
    if not check == 's':
        break

total_taxes = 0
total_commodity = 0
total_general = 0

for client in data_clients:
    name, price_commodity = client

    # Calcula o total geral, total das taxas e total do valor das mercadorias
    total_general += compute_total(price_commodity)
    total_taxes += compute_total(price_commodity) - price_commodity
    total_commodity += price_commodity

    # Mostra todos os resultados na tela
    print(f"Cliente: {name}\n"
          f"ICMS: {icms(price_commodity, True)}; IPI: {ipi(price_commodity, True)}; "
          f"PIS: {pis(price_commodity, True)}; COFINS: {cofins(price_commodity, True)}; "
          f"TOTAL: {compute_total(price_commodity, True)}")
    print()
print(f'Total Impostos: {format_value(total_taxes)}')
print(f'Total Merdorias: {format_value(price_commodity)}')
print(f'Total Geral: {format_value(total_general)}')
