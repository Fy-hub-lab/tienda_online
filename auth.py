from functools import wraps
from flask import session, redirect, url_for, flash

def login_requerido(f):
    """Exige una sesión activa sin importar el rol."""
    @wraps(f)
    def decorada(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Debes iniciar sesión para acceder a esa página.", "danger")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorada

def rol_requerido(rol):
    """Exige que la sesión activa tenga un rol específico (ej. 'admin')."""
    def decorador(f):
        @wraps(f)
        def decorada(*args, **kwargs):
            if "usuario_id" not in session:
                flash("Debes iniciar sesión para acceder a esa página.", "danger")
                return redirect(url_for("login"))
            if session.get("usuario_rol") != rol:
                flash("No tienes permisos para acceder a esa página.", "danger")
                return redirect(url_for("inicio"))
            return f(*args, **kwargs)
        return decorada
    return decorador