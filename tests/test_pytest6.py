# ARQUIVO test_pytest.py
from source.jogo2 import brincadeira

def teste_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1 # given/arange
    esperado = 1
    resultado = brincadeira(entrada) # when/act
    assert resultado == esperado # then/assert

# Irá ocorrer erro pois a brincadeira não esta setada para rodar esse teste
def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2
