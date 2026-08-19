# Sistema de Catálogo y Tienda Online (Museo)

Aplicación web desarrollada en Python con **Flask**, **SQLAlchemy** y **PostgreSQL**. Permite administrar un catálogo de productos con soporte para imágenes, autenticación con roles de usuario (Administrador y Cliente) y gestión de carrito de compras.

---

## 🚀 Requisitos previos
- Python 3.x
- PostgreSQL en ejecución

---

## 🛠️ Instalación y Configuración

1. **Clonar el repositorio o descargar el proyecto:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd Museo
Crear y activar el entorno virtual:

Bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
Instalar dependencias:

Bash
pip install -r requirements.txt
Configurar variables de entorno:
Crea un archivo .env en la raíz con tus credenciales de PostgreSQL:

Fragmento de código
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_bd
SECRET_KEY=tu_clave_secreta
Inicializar la base de datos:

Bash
python init_db.py
Ejecutar la aplicación:

Bash
python app.py
Accede desde tu navegador a: http://127.0.0.1:5000

🔑 Credenciales de Prueba
Rol	Correo / Usuario	Contraseña
Administrador	admin@ejemplo.com	admin123
Cliente	cliente@ejemplo.com	cliente123
📦 Características Principales
Gestión de Productos: Creación de productos físicos, digitales y perecibles con subida de imágenes.

Seguridad por Roles: Vistas y endpoints protegidos mediante decoradores @login_requerido y @rol_requerido.

Carrito de Compras: Funcionalidad de sesión para agregar y gestionar productos seleccionados por los clientes.


Pégalos en sus respectivos archivos, guarda los cambios con `Ctrl + S` y procede a realizar tu commit.