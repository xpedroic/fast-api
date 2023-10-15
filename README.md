# FastAPI User Management API by Pedro Izquierdo

![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

Este proyecto es una API de gestión de usuarios creada con [FastAPI](https://fastapi.tiangolo.com/), un moderno y rápido marco de desarrollo web para API en Python. La API ofrece una variedad de funciones que permiten la creación, eliminación y consulta de usuarios, así como la autenticación a través de OAuth2PasswordBearer.

## Funcionalidades principales

- **Creación de Usuarios:** Puedes crear nuevos usuarios proporcionando información como nombre de usuario, dirección de correo electrónico y contraseña.

- **Eliminación de Usuarios:** La API permite eliminar usuarios existentes de forma segura.

- **Consulta de Usuarios:** Puedes consultar información sobre los usuarios registrados en la base de datos.

- **Autenticación con OAuth2:** La API utiliza OAuth2PasswordBearer para garantizar un inicio de sesión seguro y proteger las rutas y recursos sensibles.

Esta API es una base sólida para proyectos que requieran autenticación de usuarios y gestión de cuentas. Es flexible y fácil de usar, lo que la convierte en una excelente opción para aplicaciones web y servicios que necesitan estas funcionalidades.

## Requisitos

Asegúrate de tener Python 3.6+ instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

## Instalación

1. Clona este repositorio o descarga el código fuente.

   git clone https://github.com/tuusuario/tuproyecto-fastapi.git
   cd tuproyecto-fastapi
   
3. Crea un entorno virtual (opcional pero recomendado).

   python -m venv venv
   source venv/bin/activate  # En sistemas Unix/Linux
   venv\Scripts\activate  # En Windows

3. Instala las dependencias.
   
   pip install -r requirements.txt

## Uso

1. Inicia la aplicación FastAPI.

   uvicorn main:app --reload
   Esto iniciará el servidor de desarrollo en http://localhost:8000.

2. Abre tu navegador web y visita http://localhost:8000/docs para acceder a la documentación interactiva generada automáticamente con Swagger. Aquí podrás probar los endpoints de la API y obtener detalles sobre su funcionamiento.

3. ¡Explora y modifica la aplicación a tu gusto! Puedes encontrar la lógica de la aplicación en el archivo main.py.

## Contribuciones

Si deseas contribuir a este proyecto, ¡estás más que bienvenido! Siéntete libre de crear un fork del repositorio, hacer tus cambios y enviar una solicitud de extracción.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Para obtener más información, consulta el archivo LICENSE.

## Registro de cambios

### Versión 1.0.0 (2023-10-14)

- Funcionalidad principal implementada.
- Añadida la capacidad de crear, eliminar y consultar usuarios.


Para ver todos los cambios, consulta [el registro completo de cambios](CHANGELOG.md).


## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactar a Pedro Izquierdo:
- Correo electrónico: pedro.izqcas@gmail.com
- GitHub: [github.com/xpedroic](https://github.com/xpedroic)
  
¡Gracias por tu interés en este proyecto!
