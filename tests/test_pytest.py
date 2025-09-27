from source.jogo import brincadeira # importando função teste 'brincadeira'
from pytest import mark, fixture # Importando fixture

@fixture
def minhaFixture():
    """
        Essa fixture é top, mas só será feita na proxima live
    """
    ...

@mark.exemplo_fixture
def test_minhaFixture_em_acao():
    print(minhaFixture)

# @mark.smoke
# def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
#     entrada = 1
#     esperado = 1
#     resultado = brincadeira(entrada)
#     assert resultado == esperado

# @mark.smoke
# def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
#     assert brincadeira(2) == 2

# def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
#     assert brincadeira(3) == 'queijo'

# @mark.goiabada
# @mark.smoke
# def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
#     assert brincadeira(5) == 'goiabada'

# @mark.goiabada
# def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
#     assert brincadeira(10) == 'goiabada'


# def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
#     assert brincadeira(20) == 'goiabada'

# # Essa tag faz pular o teste, podendo colocar a razão
# @mark.skip(reason='Não vai rodar esse teste pq ainda não implementei')
# def test_quando_brincadeira_receber_menos_1_entao_deve_retornar_None():
#     assert brincadeira(20) == 'None'

# @mark.parametrize(
#     'entrada',
#     [5, 10, 20]
# )
# def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
#     assert brincadeira(entrada) == 'goiabada'

# @mark.parametrizado
# @mark.parametrize(
#     'entrada',
#     [3, 6, 9, 12, 18]
# )
# def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
#     assert brincadeira(entrada) == 'queijo'

# @mark.parametrizado
# @mark.parametrize(
#     'entrada, esperado',
#     [(1, 1), (2, 2), (3, 'queijo'), (4, 4), (5, 'goiabada')]
# )
# def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
#     assert brincadeira(entrada) == esperado

# @mark.xfail
# def test_xfail1():
#     assert brincadeira(20) == 'goiabada'

# @mark.xfail
# def test_xfail2():
#     assert brincadeira(20) != 'goiabada'


# # Criando um teste mais realistas
# # Falhar se for em plataforma windows
# import sys

# # Esse teste  é executado
# @mark.xfail(sys.platform == 'win32')
# def test_xfail_windows():
#     assert brincadeira(20) == 'goiabada'


# Se a plataform for igual win32, pula esse teste

# # Esse teste não é executado
# @mark.skipif(sys.platform == 'win32', reason="não roda no windows")
# def test_skipif_windows():
#     assert brincadeira(20) == 'goiabada'

# # Chamada da fixture capsys - Envia o 'espião' para verificar 
# @mark.stdout
# def test_brincadeira_deve_escrever_entrei_na_brincadeira_na_tela(capsys):
#     brincadeira(0)
#     resultado = capsys.readouterr() 
#     assert resultado.out == 'Entrei na brincadeira\n'

