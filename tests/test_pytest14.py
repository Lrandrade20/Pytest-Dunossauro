from source.jogo4 import brincadeira 
from pytest import mark

# Outro exemplo de parametrize

@mark.parametrizado
@mark.parametrize(
    'entrada',
    [3, 6, 9, 12, 18]
)
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    assert brincadeira(entrada) == 'queijo'
    
# So o 3 funciona, devido a estrutura da função brincadeira

