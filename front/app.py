from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests

# Importar los Blueprints de las rutas
from rutas.rutas_usuarios import rutas_usuario
from rutas.rutas_tipo_responsable import rutas_tipo_responsable
from rutas.rutas_tipo_proyecto import rutas_tipo_proyecto
from rutas.rutas_estado import rutas_estado
from rutas.rutas_tipo_producto import rutas_tipo_producto
from rutas.rutas_entregable import rutas_entregable
from rutas.rutas_variable_estrategica import rutas_variable_estrategica
from rutas.rutas_actividad import rutas_actividad
from rutas.rutas_archivo import rutas_archivo
from rutas.rutas_archivo_entregable import rutas_archivo_entregable
from rutas.rutas_distribucion_presupuesto import rutas_distribucion_presupuesto
from rutas.rutas_ejecucion_presupuesto import rutas_ejecucion_presupuesto
from rutas.rutas_estado_proyecto import rutas_estado_proyecto
from rutas.rutas_meta_estrategica import rutas_meta_estrategica
from rutas.rutas_meta_proyecto import rutas_meta_proyecto
from rutas.rutas_objetivo_estrategico import rutas_objetivo_estrategico
from rutas.rutas_presupuesto import rutas_presupuesto
from rutas.rutas_proyecto import rutas_proyecto
from rutas.rutas_responsable import rutas_responsable
from rutas.rutas_producto import rutas_producto
from rutas.rutas_proyecto_producto import rutas_proyecto_producto
from rutas.rutas_producto_entregable import rutas_producto_entregable
from rutas.rutas_responsable_entregable import rutas_responsable_entregable
from rutas.rutas_login import rutas_login  # 🚪 Blueprint del login

# ------------------- CONFIGURACIÓN DE LA APLICACIÓN -------------------
aplicacion = Flask(__name__)
aplicacion.secret_key = 'clave-super-secreta-123'  # 🔐 Necesaria para usar sesiones

# ------------------- REGISTRO DE BLUEPRINTS -------------------
aplicacion.register_blueprint(rutas_usuario)
aplicacion.register_blueprint(rutas_tipo_responsable)
aplicacion.register_blueprint(rutas_tipo_proyecto)
aplicacion.register_blueprint(rutas_estado)
aplicacion.register_blueprint(rutas_tipo_producto)
aplicacion.register_blueprint(rutas_entregable)
aplicacion.register_blueprint(rutas_variable_estrategica)
aplicacion.register_blueprint(rutas_actividad)
aplicacion.register_blueprint(rutas_archivo)
aplicacion.register_blueprint(rutas_archivo_entregable)
aplicacion.register_blueprint(rutas_distribucion_presupuesto)
aplicacion.register_blueprint(rutas_ejecucion_presupuesto)
aplicacion.register_blueprint(rutas_estado_proyecto)
aplicacion.register_blueprint(rutas_meta_estrategica)
aplicacion.register_blueprint(rutas_meta_proyecto)
aplicacion.register_blueprint(rutas_objetivo_estrategico)
aplicacion.register_blueprint(rutas_presupuesto)
aplicacion.register_blueprint(rutas_proyecto)
aplicacion.register_blueprint(rutas_responsable)
aplicacion.register_blueprint(rutas_producto)
aplicacion.register_blueprint(rutas_proyecto_producto)
aplicacion.register_blueprint(rutas_producto_entregable)
aplicacion.register_blueprint(rutas_responsable_entregable)
aplicacion.register_blueprint(rutas_login)

# ------------------- PROTECCIÓN GLOBAL DE RUTAS -------------------
@aplicacion.before_request
def proteger_todo():
    """Bloquea todo el sitio si no hay sesión activa (excepto login y archivos estáticos)."""
    rutas_publicas = ['rutas_login.login', 'rutas_login.logout', 'static']
    if not session.get('usuario') and request.endpoint not in rutas_publicas:
        return redirect(url_for('rutas_login.login'))

# ------------------- RUTAS PRINCIPALES -------------------
@aplicacion.route("/")
def inicio():
    return render_template("index.html", usuario=session.get("usuario"))

@aplicacion.route("/acerca")
def acerca():
    return render_template("acerca.html")

# ------------------- PUNTO DE ENTRADA -------------------
if __name__ == "__main__":
    aplicacion.run(host="0.0.0.0", port=5000, debug=True)
