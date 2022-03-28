# Biochemical Laboratory



* Registro de pacientes y estudios.
* Genera PDF para descargar los estudios del paciente.
* Almacenamiento por SQLite.

Este proyecto fue desarrollado con fines personales, educativos y no lucrativos.

## Instalación
Creamos un entorno virtual y lo activamos
```sh
python -m venv entv
cd entv
cd scripts
activate
```

Nos ubicamos en la carpeta del proyecto e instalamos dependencias.
```sh
pip install -r requirements.txt
```

## Configuracion

Editar el archivo `server.py` y cambiar "PRIVATE_IP" por tu ip privada.

```python
serve(application, host='PRIVATE_IP', port=8000)
```

## Inicializar

```
python manage.py server.py
```
