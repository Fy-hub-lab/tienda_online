# 🛒 Tienda Online — Flask + PostgreSQL

Proyecto final que implementa una plataforma de comercio electrónico orientada a objetos con Flask y PostgreSQL. El sistema gestiona un catálogo con tres tipos de productos mediante herencia, control de acceso por roles (Administrador y Cliente), persistencia en sesión para el carrito de compras y gestión de imágenes para cada producto.

**Autor:** Derek Moreno  
**Materia:** Programación Orientada a Objetos (POO)  
**Paralelo:** P4  

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Framework Web:** Flask
* **Base de Datos:** PostgreSQL
* **ORM:** SQLAlchemy
* **Estilos:** Bootstrap 5

---

## 🚀 Instrucciones de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto localmente:

### 1. Clonar el repositorio e ingresar a la carpeta
```bash
git clone [https://github.com/Fy-hub-lab/tienda_online.git](https://github.com/Fy-hub-lab/tienda_online.git)
cd tienda_online
2. Crear y activar el entorno virtual
Linux/macOS:

Bash
python3 -m venv venv
source venv/bin/activate
Windows:

DOS
python -m venv venv
venv\Scripts\activate
3. Instalar las dependencias
Bash
pip install -r requirements.txt
4. Configurar las variables de entorno (.env)
Crea un archivo llamado .env en la raíz del proyecto con el siguiente contenido:

Fragmento de código
SECRET_KEY=clave_secreta_para_sesiones
DATABASE_URL=postgresql://postgres:tu_contraseña@localhost:5432/tienda_online
5. Inicializar la base de datos y ejecutar la aplicación
Bash
python init_db.py
python app.py
Abre tu navegador e ingresa a: http://127.0.0.1:5000

🔐 Credenciales de Prueba
Para probar el control de roles y permisos del sistema:

Cuenta Administrador (Acceso a la creación, edición, desactivación de productos y subida de imágenes)

Correo: admin@tienda.com

Contraseña: admin123

Cuenta Cliente (Acceso a la visualización del catálogo y adición de ítems al carrito)

Correo: cliente@tienda.com

Contraseña: cliente123

📸 Capturas de Pantalla
1. Catálogo de Productos
Captura1.PNG

2. Detalle de Producto
Captura2.PNG

3. Carrito de Compras
Captura3.PNG

4. Carrito de Compras con valor
Captura4.PNG


***

**Notas finales antes del push:**
* Puedes reemplazar la ruta de las imágenes `static/uploads/default.png` con la ubicación real de tus capturas (por ejemplo, gua