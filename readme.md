# Pytest – Guia Rápido

```bash
# 📌 Introdução e Instalação
pip install pytest
pytest --version

# 📌 Testes
# Estrutura básica: funções iniciando com test_ e uso de assert
def test_exemplo():
    assert 2 + 2 == 4

# 📌 Marks
# pular teste
@pytest.mark.skip(reason="Não implementado")

# pular se condição for verdadeira
@pytest.mark.skipif(sys.platform == "win32", reason="Não roda no Windows")

# esperar falha
@pytest.mark.xfail(reason="Bug conhecido")

# rodar testes com mark específica
pytest -m slow

# 📌 Fixtures
import pytest

@pytest.fixture
def recurso():
    return "dados"

def test_recurso(recurso):
    assert recurso == "dados"

# 📌 Comandos Básicos
pytest             # roda todos os testes
pytest -v          # modo verboso
pytest -q          # modo silencioso
pytest tests/      # roda apenas a pasta tests
pytest -k soma     # roda testes que contenham 'soma' no nome
pytest -m slow     # roda testes com a mark 'slow'
