# Importando o arquivo jogo.py como variavel 'brincadeira'
from source.jogo import brincadeira

"""
O teste é formado por três etapas (GWT - AAA):
- Given - Dado
- When - Quando
- Then - Então
OU 
- Arange
- Act
- Assert
"""

def teste_quando_brincadeira_receber_1_entao_deve_retornar_1():
    """
        Brincadeira - SUT - System Under Test
    """
    entrada = 1 # given/arange
    esperado = 1
    resultado = brincadeira(entrada) # when/act

    # No livro TDD - Kent Back - Isso é chamado de One-step Test
    assert resultado == esperado # then/assert

    # Versão simples: assert brincadeira(1) == 1
    # A versão simples não segue boas práticas
