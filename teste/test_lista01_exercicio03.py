from codigo.lista01_exercicio03 import *

def test_modificar_titulo():
    livro = Livro()
    livro.set_titulo("O magico de Oz")
    assert livro.get_titulo() == "O magico de Oz"

def test_modificar_autor():
    livro = Livro()
    livro.set_autor("Platao")
    assert livro.get_autor() == "Platao"

def test_modificar_genero():
    livro = Livro()
    livro.set_genero("Romance")
    assert livro.get_genero() == "Romance"

def test_modificar_numero_paginar():
    livro = Livro()
    livro.set_numero_paginas(400)
    assert livro.get_numero_paginas() == 400

def test_modificar_ano_publicacao():
    livro = Livro()
    livro.set_ano_publicacao(1989)
    assert livro.get_ano_publicacao() == 1989

def test_abrir_livro():
    livro = Livro()
    assert livro.abrir() == "O livro foi aberto"

def test_fechar_livro():
    livro = Livro()
    assert livro.fechar() == "O livro foi fechado"

def test_marcar_pagina_livro():
    livro = Livro()
    livro.set_numero_paginas(200)
    livro.marcar_pagina(50)
    assert livro.get_pagina_atual() == 50

def test_marcar_pagina_livro_nao_tem():
    livro = Livro()
    livro.set_numero_paginas(50)
    livro.marcar_pagina(60)
    assert livro.get_pagina_atual() == 1

def test_avancar_pagina():
    livro = Livro()
    livro.set_numero_paginas(200)
    livro.avancar_pagina()
    assert livro.get_pagina_atual() == 2
# só pula de 1 em 1 pagina pq sim

def test_retroceder_pagina():
    livro = Livro()
    livro.set_numero_paginas(400)
    livro.set_pagina_atual(40)
    livro.retroceder_pagina()
    assert livro.get_pagina_atual() == 39
# voce não consegue retroceder na pagina 1 que é ditada no lista, pq vc vai pra pagina 0 e ela não existe :D

def test_pagina_atual():
    livro = Livro()
    livro.set_pagina_atual(50)
    assert livro.get_pagina_atual() == 50



