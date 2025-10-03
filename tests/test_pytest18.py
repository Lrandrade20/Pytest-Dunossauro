from source.jogo5 import brincadeira 
from pytest import mark


# Chamada da fixture capsys - Envia o 'espião' para verificar 
# O erro ocorre pois o print pula uma linha por padrão, e a string testada não pula
@mark.stdout
def test_brincadeira_deve_escrever_entrei_na_brincadeira_na_tela(capsys):
    brincadeira(0)
    resultado = capsys.readouterr() 
    assert resultado.out == 'Entrei na brincadeira'

# Comando: pytest tests/test_pytest18.py -k "stdout" -v