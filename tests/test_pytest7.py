from source.jogo2 import brincadeira

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1
    esperado = 1
    resultado = brincadeira(entrada)
    assert resultado == esperado

def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2

# Nova função adicionada - ira ocorrer erro
def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'