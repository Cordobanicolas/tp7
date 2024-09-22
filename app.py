from flask import Flask, render_template, request


# Creamos una instancia de la aplicación Flask
app = Flask(__name__)


# Ruta para la página de inicio
@app.route('/')
def home():
    # Renderiza la plantilla 'home.html'
    return render_template('home.html')


# Ruta para la página de contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    # Si la solicitud es POST, procesa los datos del formulario
    if request.method == 'POST':
       nombre = request.form.get('nombre')
       mensaje = request.form.get('mensaje')
       # Respuesta simple para confirmar la recepción del mensaje
       return f"Gracias {nombre}, hemos recibido tu mensaje: {mensaje}"
   # Si es una solicitud GET, muestra el formulario
    return render_template('contacto.html')
 
 
# Ruta para el perfil del usuario
@app.route('/perfil/<nombre>')
def perfil(nombre):
    # Pasa el nombre como variable a la plantilla 'perfil.html'
    return render_template('perfil.html', nombre=nombre)
# Ejecuta la aplicación en modo debug
if __name__ == '__main__':
