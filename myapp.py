from flask import Flask,render_template

app = Flask(__name__,template_folder='templates') #Creo una instancia de Flask, defiendo la carpeta "templates" para acceder a las plantillas html

########################################
########### PAGINA PRINCIPAL ###########
########################################

@app.route('/') #defino la ruta correspondiente al directorio raiz de mi sitio web
def index():
    return render_template('index.html') #renderizo el template indicado

#########################################
########### SECCION PROYECTOS ###########
#########################################
    
@app.route('/proyectos') #ruta a proyectos (ej. geofisicachile.cl/proyectos)
def proyectos():
    return render_template('proyectos.html')

#!!!!!!!!!!!!!!!!!!!!!
#AGREGAR PROYECTOS AQUI
#!!!!!!!!!!!!!!!!!!!!!
    
@app.route('/proyectos/contaminacion1') #ruta a proyectos (ej. geofisicachile.cl/proyectos)
def contaminacion1():
    return render_template('temp-plot_2.html')

@app.route('/proyectos/contaminacion2') #ruta a proyectos (ej. geofisicachile.cl/proyectos)
def contaminacion2():
    return render_template('temp-plot.html')


########################################
########### SECCION MATERIAL ###########
########################################   
@app.route('/material') #ruta a material (ej. geofisicachile.cl/material)
def material():
    return render_template('material.html')

#!!!!!!!!!!!!!!!!!!!!!
#AGREGAR MATERIAL AQUI
#!!!!!!!!!!!!!!!!!!!!!
@app.route('/material/programacion_cuantica')
def progcuantica():
   return render_template('material-progcuantica.html') 


############################################
########### SECCION EQUIPO y CVS ###########
############################################
    
@app.route('/equipo') #ruta a equipo (ej. geofisicachile.cl/equipo)
def equipo():
    return render_template('equipo.html')

#!!!!!!!!!!!!!!!!!!!!!
#AQUI VAN LOS CURRICULUMS
#!!!!!!!!!!!!!!!!!!!!!
@app.route('/cv/piero') #ruta a cv piero 
def piero():
    return render_template('piero.html')

@app.route('/cv/josse') #ruta a cv josse
def josse():
    return render_template('josse.html')

@app.route('/cv/rocio') #ruta a cv rocio
def rocio():
    return render_template('rocio.html')

@app.route('/cv/camilo') #ruta a cv camilo
def camilo():
    return render_template('camilo.html')

########################################
########### SECCION CONTACTO ###########
########################################
@app.route('/contacto') #ruta a contacto (ej. geofisicachile.cl/contacto)
def contacto():
    return render_template('contacto.html')



if __name__ == '__main__':
    app.run(debug=True)