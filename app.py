#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import uuid
import shutil
from flask import Flask, request, render_template, send_file, after_this_request
try:
    from criptografia_Algebra_EcuacionesGrado1 import genera_pdf
except Exception as e:
    import traceback
    print("ERROR EN IMPORTACIÓN:", traceback.format_exc())
    raise
import resource

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"
FICHAS_FOLDER = "./fichas"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(FICHAS_FOLDER, exist_ok=True)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generar", methods=["POST"])
def generar():
    archivo_datos = request.files.get("archivo_datos")
    archivo_elementos = request.files.get("archivo_elementos")

    if not archivo_datos or not archivo_elementos:
        return "Faltan archivos. Por favor, sube ambos archivos .txt.", 400

    try:
        valorLetraA = int(request.form.get("valorLetraA", -13))
    except ValueError:
        valorLetraA = -13

    conDenominadores = int(request.form.get("conDenominadores", 0))

    id_sesion = str(uuid.uuid4())
    directorio_trabajo = os.path.join(UPLOAD_FOLDER, id_sesion)
    os.makedirs(directorio_trabajo, exist_ok=True)

    try:
        ruta_datos = os.path.join(directorio_trabajo, "datos.txt")
        ruta_elementos = os.path.join(directorio_trabajo, "elementos.txt")
        archivo_datos.save(ruta_datos)
        archivo_elementos.save(ruta_elementos)

        ruta_pdf = genera_pdf(
            ruta_datos=ruta_datos,
            ruta_elementos=ruta_elementos,
            valorLetraA=valorLetraA,
            conDenominadores=conDenominadores,
            directorio_trabajo=directorio_trabajo
        )

        @after_this_request
        def limpia(response):
            try:
                shutil.rmtree(directorio_trabajo)
            except Exception:
                pass
            return response

        return send_file(ruta_pdf, as_attachment=True, download_name="fichas_criptografia.pdf", mimetype="application/pdf")

    except Exception as e:
        import traceback
        error_completo = traceback.format_exc()
        shutil.rmtree(directorio_trabajo, ignore_errors=True)
        return f"<pre>{error_completo}</pre>", 500
