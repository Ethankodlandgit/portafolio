from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')

# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    # Renderizar la página con el botón específico activado
    return render_template(
        'index.html', 
        button_python=button_python, 
        button_discord=button_discord, 
        button_html=button_html, 
        button_db=button_db
    )

# Procesar el formulario de feedback
@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.form.get('email')
    text = request.form.get('text')
    # Guardar la información en variables (se puede extender para almacenamiento persistente)
    print(f"Email: {email}, Comentario: {text}")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
