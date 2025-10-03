from source.jogo4 import brincadeira 
from pytest import mark

@mark.smoke
def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1
    esperado = 1
    resultado = brincadeira(entrada)
    assert resultado == esperado

@mark.smoke
def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2

def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'

# Dois grupos de teste
@mark.goiabada
@mark.smoke
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'


def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == 'goiabada'


def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    assert brincadeira(20) == 'goiabada'


    
"""
# Comando:  pytest tests/test_pytest11.py -m smoke -v
# Exemplos 

pytest -m goiabada 
# roda a mark com goiabada

pyteste -m "not goiabada"
# Aqui NÃO vai rodar o mark de goiabada
"""
    
    