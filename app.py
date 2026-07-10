from flask import Flask, request, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)
db_name = "usuarios.db"

# Inicializar DB
def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, password_hash TEXT)''')
    conn.commit()
    conn.close()

# Encriptar contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        action = request.form['action']
        
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        
        if action == "register":
            c.execute("INSERT INTO users VALUES (?, ?)", (username, hash_password(password)))
            conn.commit()
            msg = "Usuario registrado exitosamente."
        else:
            c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            user = c.fetchone()
            if user and user[0] == hash_password(password):
                msg = "Inicio de sesión exitoso."
            else:
                msg = "Credenciales incorrectas."
        
        conn.close()
        return f"<h1>{msg}</h1><a href='/'>Volver</a>"

    return '''
        <form method="post">
            Usuario: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <button type="submit" name="action" value="register">Registrar</button>
            <button type="submit" name="action" value="login">Login</button>
        </form>
    '''

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)