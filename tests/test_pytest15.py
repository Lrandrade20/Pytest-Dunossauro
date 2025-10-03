from source.jogo4 import brincadeira 
from pytest import mark

# Entrada (4, 4) vai falhar
@mark.parametrizado
@mark.parametrize(
    'entrada, esperado',
    [(1, 1), (2, 2), (3, 'queijo'), (4, 4), (5, 'goiabada')]
)
def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
    assert brincadeira(entrada) == esperado