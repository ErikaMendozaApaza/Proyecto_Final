# Utiliza una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements_local.txt /app/

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements_local.txt

# Copia todo el contenido del proyecto al directorio de trabajo
COPY . /app/

# Expone el puerto en el que Django correrá
EXPOSE 8000

# Comando por defecto para correr el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
