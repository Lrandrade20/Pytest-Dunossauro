from source.jogo4 import brincadeira 
from pytest import mark
import sys

# Se a plataform for igual win32, pula esse teste
# Esse teste não é executado
@mark.skipif(sys.platform == 'win32', reason="não roda no windows")
def test_skipif_windows():
    assert brincadeira(20) == 'goiabada'
    # Comando - pytest tests/test_pytest17.py -k "skipif" -v