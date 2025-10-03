from source.jogo4 import brincadeira 
from pytest import mark

# O Xfail é pensado para testes que devem falhar.
# x minusculo = Erro esperado
# X maiusculo = Erro inesperado, mas não falhou

# igual goiabada
@mark.xfail
def test_xfail1():
    assert brincadeira(20) == 'goiabada'

# diferente goiabada
@mark.xfail
def test_xfail2():
    assert brincadeira(20) != 'goiabada'

# Comando: pytest tests/test_pytest16.py -k "xfail" -v