# Generador de fichas de criptografía

Aplicación web que genera fichas de ejercicios de matemáticas en PDF a partir de archivos de texto con palabras o frases a encriptar.

## Estructura del proyecto

```
proyecto/
├── app.py                                      ← Servidor Flask
├── criptografia_Algebra_EcuacionesGrado1.py    ← Lógica de generación
├── funcionesBasicas.py                         ← Funciones auxiliares
├── imagenes/
│   └── logoCilniana_horizontal_5cm.png         ← Logo del centro
├── templates/
│   └── index.html                              ← Formulario web
├── uploads/                                    ← Archivos temporales (se crea solo)
├── fichas/                                     ← PDFs temporales (se crea solo)
├── Dockerfile
└── README.md
```

## Prueba local

1. Instala las dependencias:
   ```
   pip install flask numpy
   ```

2. Asegúrate de tener `pdflatex` instalado en tu sistema (en Xubuntu ya lo tienes).

3. Ejecuta:
   ```
   python app.py
   ```

4. Abre el navegador en `http://localhost:5000`

## Despliegue en Render (gratuito)

1. Sube el proyecto a un repositorio de GitHub.
2. En [render.com](https://render.com), crea un nuevo servicio de tipo **Web Service**.
3. Conecta tu repositorio de GitHub.
4. En la configuración:
   - **Environment**: Docker
   - **Branch**: main (o la que uses)
5. Render detectará el Dockerfile automáticamente y construirá la imagen.
6. Una vez desplegado, recibirás una URL pública para compartir.

> **Nota**: La primera vez que Render construye la imagen puede tardar varios minutos porque instala LaTeX. Las siguientes veces es más rápido.
