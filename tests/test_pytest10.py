from source.jogo4 import brincadeira 
from pytest import mark

# Testes com mark 'goiabada'
# logica do teste: multiplos de 5
@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    assert brincadeira(20) == 'goiabada'

# Comando: pytest -m goiabada OU pytest -m goiabada -v 
    # realiza os testes com markadores