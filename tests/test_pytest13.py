from source.jogo4 import brincadeira 
from pytest import mark

"""
# Multiplos testes do mesmo tipo com valores diferentes
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == 'goiabada'

def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    assert brincadeira(20) == 'goiabada'
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Criado o paramtrize para rodar os 3 testes acima em uma unica função teste
# Também criamos o mark 'parametrizado' nomeado para rodar somente ele separado
# Podemos adicionar quantos parametros no parametrize quisermos
@mark.parametrizado
@mark.parametrize(
    'entrada',
    [5, 10, 20]
)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    """
        pytest -m parametrize -v  
        # roda a mark com goiabada

        pyteste -m parametrizado -v  
        # Aqui NÃO vai rodar o mark de goiabada
    """
    assert brincadeira(entrada) == 'goiabada'

