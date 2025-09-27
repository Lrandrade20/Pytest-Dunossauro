# Pytest – Guia Rápido

Este repositório foi criado conforme vídeo aula de introdução ao **pytest** do [Dunossauro](https://www.youtube.com/@dunossauro).  
A ideia é servir como guia rápido (cheatsheet) para comandos, marcações e exemplos básicos.

```bash
# 📌 Introdução e Instalação
pip install pytest
pytest --version

# 📌 Testes
def test_exemplo():
    assert 2 + 2 == 4

# 📌 Marks
@pytest.mark.skip(reason="Não implementado")
@pytest.mark.skipif(sys.platform == "win32", reason="Não roda no Windows")
@pytest.mark.xfail(reason="Bug conhecido")

pytest -m slow   # rodar testes por marca

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
