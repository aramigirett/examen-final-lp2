from flask import Flask, render_template, request, redirect, url_for, flash
from dao.NacionalidadDao import NacionalidadDao

app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/inicio')
def inicio():
    return "hola mundo desde el backend"

# endpoint o ruta
@app.route('/contacto')
def contacto():
    return "<h3>Introduciendo HTML desde el servidor</h3>"

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')

@app.route('/nacionalidades-index')
def nacionalidades_index():
    #creacion de la instancia de ciudaddao
    nacionalidadDao = NacionalidadDao()
    lista_nacionalidades = nacionalidadDao.getNacionalidades()
    return render_template('nacionalidades-index.html', lista_nacionalidades=lista_nacionalidades)

@app.route('/nacionalidades')
def nacionalidades():
    return render_template('nacionalidades.html')

@app.route('/guardar-nacionalidad', methods=['POST'])
def guardarNacionalidad():
    nacionalidad = request.form.get('txtDescripcion').strip()
    if nacionalidad == None or len(nacionalidad) < 1:
       # mostrar un mensaje al usuario
       flash('Debe escribir algo en la descripcion', 'warning')
    
       # redireccionar a la vista ciudades
       return redirect(url_for('nacionalidades'))
    
    nacionalidaddao = NacionalidadDao()
    nacionalidaddao.guardarNacionalidad(nacionalidad.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista ciudades 
    return redirect(url_for('nacionalidades_index'))

@app.route('/nacionalidades-editar/<id>')
def nacionalidadesEditar(id):
    nacionalidaddao = NacionalidadDao()
    return render_template('nacionalidades editar.html', nacionalidad=nacionalidaddao.getNacionalidadById(id))

@app.route('/actualizar-naciodalidad', methods=['POST'])
def actualizarNacionalidad():
    id = request.form.get('txtIdNacionalidad')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('ciudadesEditar', id=id))

    # actualizar
    nacionalidaddao = NacionalidadDao()
    nacionalidaddao.updateNacionalidad(id, descripcion.upper())

    return redirect(url_for('nacionalidades_index'))

@app.route('/guardar-mascota', methods=['POST'])
def guardarMascota():
    print(request.form)
    nombreMascota = request.form.get('txtNombreMascota')
    return f"Ya llego tu mascota <strong>{nombreMascota}</strong> al servidor"

@app.route('/nacionalidades-eliminar/<id>')
def nacionalidadesEliminar(id):
    nacionalidaddao = NacionalidadDao()
    nacionalidaddao.deleteNacionalidad(id)
    return redirect(url_for('nacionalidades_index'))

if __name__=='__main__':
    app.run(debug=True)