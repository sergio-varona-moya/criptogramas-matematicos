# Imagen base con Python 3.11
FROM python:3.11-slim

# Instalamos LaTeX (texlive-full tarda mucho; esta selección cubre lo que necesitas)
RUN apt-get update && apt-get install -y \
    texlive-full \
    python3-pythontex \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos del proyecto
COPY . .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir flask numpy

# Exponemos el puerto de Flask
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

EXPOSE 5000
# Comando de arranque
CMD ["python", "app.py"]
