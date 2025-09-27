
# Vamos 'espionar' se houve a chamada do 'Entrei na brincadeira'
def brincadeira(numero):
    print('Entrei na brincadeira') # Item que usaremos pra testar fixture
    if numero < 3:
        return numero
    if numero > 4:
        return 'goiabada'
    return 'queijo'