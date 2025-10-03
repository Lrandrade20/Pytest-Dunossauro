from source.jogo4 import brincadeira 
from pytest import mark

"""
# Comando
pytest -v 

# Comando para mostrar os Skipados
pytest -rs
"""

# Item teste exemplo deste file
# Essa tag faz pular o teste, podendo colocar a razão
@mark.skip(reason='Não vai rodar esse teste pq ainda não implementei')
def test_quando_brincadeira_receber_menos_1_entao_deve_retornar_None():
    assert brincadeira(20) == 'None'


##### EStão aqui só pra fazer volume

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


