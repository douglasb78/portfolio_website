from flask import Flask, render_template
from whitenoise import WhiteNoise

app = Flask(__name__)

informacoes = {
    "nome": "Nome Sobrenome",
    "telefone": "(54) 12345-6789",
    "email": "teste@pm.me",
    "telefone_ddi": "+5554123456789",
    "links" : {
        "github" : "https://github.com",
        "linkedin" : "https://br.linkedin.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com"
    },
    "resumo": "Biografia.",
    "descricao": "Descrição. O que está cursando, ou carreira."
}

@app.route("/")
def home():
    formacoes = [
        {"periodo": "YYYY ― XXh",
         "titulo": "Título da formação",
         "descricao": "Nome da Instituição"
        },
        {"periodo": "YYYY ― XXh",
         "titulo": "Título da formação",
         "descricao": "Nome da Instituição"
        },
        {"periodo": "YYYY ― XXh",
         "titulo": "Título da formação",
         "descricao": "Nome da Instituição"
        },
    ]

    cursos = [
        {"periodo": "YYYY ― XXh",
         "titulo": "Título do Curso",
         "descricao": "Nome da Instituição"
        },
        {"periodo": "YYYY ― XXh",
         "titulo": "Título do Curso",
         "descricao": "Nome da Instituição"
        },
        {"periodo": "YYYY ― XXh",
         "titulo": "Título do Curso",
         "descricao": "Nome da Instituição"
        },
        {"periodo": "YYYY ― XXh",
         "titulo": "Título do Curso",
         "descricao": "Nome da Instituição"
        }
    ]
    return render_template('index.html', formacoes=formacoes, cursos=cursos, informacoes=informacoes)

@app.route("/projetos")
def projetos():
    projetos = [
        {
            "titulo": "Leitor de RSS",
            "link": "https://gist.github.com/douglasb78/f6e8f89124e0da2d7eb27d2329c3c61b",
            "descricao": "Um programa simples, que verifica as postagens mais recentes de um feed RSS de um blog e notifica ao abrir se há postagens.",
            "linguagem": "Go",
        },
        {
            "titulo": "Cadastro de Pesquisadores",
            "link": "https://github.com/douglasb78/Trabalho_POO_2_facul",
            "descricao": "Programa desenvolvido como parte de um trabalho em grupo na faculdade. Faz a leitura e manipulação de arquivos de texto utilizando expressões regulares (RegEx), faz, lê e modifica cadastros, e salva os dados.",
            "linguagem": "Java",
        },
        {
            "titulo": "TDE de Grafos",
            "link": "https://gist.github.com/douglasb78/e928295ce3e182b6ca3273b0eaec1c01",
            "descricao": "Programa que lista as articulações, demarcadores, pontes, vértices e componentes biconexas de um grafo.",
            "linguagem": "C",
        }
    ]
    return render_template('projetos.html', projetos=projetos, informacoes=informacoes)

@app.route("/contato")
def contato():
    return render_template('contato.html', informacoes=informacoes)

if __name__ == '__main__':
    app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
    app.run(debug=True)