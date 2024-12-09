from flask import Flask

app = Flask(__name__)

#criar a primeira pagina
# route = qual link vai ficar a pagina
#função = o que vou exibir na pagina

@app.route("/")
def raiz ():
    return "Esse é meu primeiro site"


#colocar o site no ar
app.run()
