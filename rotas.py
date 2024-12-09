from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__ , template_folder='templates')
app.secret_key = 'sua_chave_secreta'

#criar a primeira pagina
# route = qual link vai ficar a pagina
#função = o que vou exibir na pagina

@app.route("/")
def index ():
    return render_template("index.html")

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        email = request.form['email']
        full_name = request.form['full_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Validação de senha no backend
        if password != confirm_password:
            flash('As senhas não coincidem.', 'error')
            return render_template('registro.html')

        password_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$&]).{6,}$'
        if not re.match(password_regex, password):
            flash('A senha deve ter pelo menos 6 caracteres, 1 letra maiúscula, 1 número e 1 caractere especial (!@#$&).', 'error')
            return render_template('registro.html')

        # Simula o registro do usuário (aqui você salvaria os dados no banco de dados)
        flash('Conta registrada com sucesso!', 'success')

        # Redireciona para a página de login
        return redirect(url_for('login'))
    
    return render_template('registro.html')


@app.route("/login")
def login ():
    return render_template("login.html")
#colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)
