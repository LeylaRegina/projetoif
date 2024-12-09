from flask import Flask, render_template


app = Flask(__name__ , template_folder='templates')

#criar a primeira pagina
# route = qual link vai ficar a pagina
#função = o que vou exibir na pagina

@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/login")
def login ():
    return render_template("login.html")


@app.route('/registro')
def registro(): 
    return render_template('registro.html') 

#colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)
