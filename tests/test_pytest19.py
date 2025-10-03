from source.jogo5 import brincadeira # alterado o testador
from pytest import mark

# Inserindo o pulo de linha
@mark.stdout
def test_brincadeira_deve_escrever_entrei_na_brincadeira_na_tela(capsys):
    brincadeira(0)
    resultado = capsys.readouterr() 
    assert resultado.out == 'Entrei na brincadeira\n'

# Comando: pytest tests/test_pytest18.py -k "stdout" -v