import pip
import requests

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json"

response = requests.get(url)
data = response.json()

cotacao_dolar = float(data[-1]['valor'])

saldo = float(input('digite seu saldo em reais: '))
saldoConvertido = saldo/cotacao_dolar
saldo_convertido_formatado = "{:.3f}".format(saldoConvertido)
print('seu saldo em dolar e', saldo_convertido_formatado)







