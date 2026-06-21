#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import numpy as np
import random
import time
import math
import os
import funcionesBasicas
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_UP


def generaOperacionesTipo1(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    listaOperacionesUnicas = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        if (D - A * C) % (A * B) == 0 and (D - A * C) / (A * B) == solucion:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo2(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        if (A - C) != 0:
            if (D - B) / (A - C) == solucion:
                textoOperacion = "$" + str(A) + "x"
                if B > 0:
                    textoOperacion += "+" + str(B) + " = "
                else:
                    textoOperacion += str(B) + " = "
                textoOperacion += str(C) + "x"
                if D > 0:
                    textoOperacion += "+" + str(D) + "$"
                else:
                    textoOperacion += str(D) + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo3(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(2, maximoPositivo)
        B = random.randrange(1, maximoPositivo)
        C = random.randrange(1, maximoPositivo)
        D = random.randrange(2, maximoPositivo)
        E = random.randrange(1, maximoPositivo)
        F = random.randrange(1, maximoPositivo)
        if (A * B - D * E) != 0:
            if (D * F - A * C) / (A * B - D * E) == solucion:
                textoOperacion = "$" + str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + ") = "
                else:
                    textoOperacion += str(C) + ") = "
                textoOperacion += str(D) + "(" + str(E) + "x"
                if F > 0:
                    textoOperacion += "+" + str(F) + ")" + "$"
                else:
                    textoOperacion += str(F) + ")" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo4(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(2, maximoPositivo)
        B = random.randrange(1, maximoPositivo)
        C = random.randrange(1, maximoPositivo)
        D = random.randrange(2, maximoPositivo)
        E = random.randrange(1, maximoPositivo)
        F = random.randrange(2, maximoPositivo)
        G = random.randrange(2, maximoPositivo)
        H = random.randrange(1, maximoPositivo)
        I = random.randrange(2, maximoPositivo)
        J = random.randrange(1, maximoPositivo)
        K = random.randrange(1, maximoPositivo)
        if (A * B + D - F * G + I * J) != 0:
            if (F * H - I * K - A * C + E) / (A * B + D - F * G + I * J) == solucion:
                textoOperacion = "$" + str(A) + "(" + str(B) + "x" + "+" + str(C) + ")" + "+" + str(D) + "x" + "-" + str(E) + "=" + str(F) + "(" + str(G) + "x" + "+" + str(H) + ")" + "-" + str(I) + "(" + str(J) + "x" + "+" + str(K) + ")" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo5(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(2, maximoPositivo)
        B = random.randrange(1, maximoPositivo)
        C = random.randrange(1, maximoPositivo)
        D = random.randrange(2, maximoPositivo)
        E = random.randrange(1, maximoPositivo)
        F = random.randrange(2, maximoPositivo)
        G = random.randrange(1, maximoPositivo)
        H = random.randrange(2, maximoPositivo)
        I = random.randrange(1, maximoPositivo)
        J = random.randrange(1, maximoPositivo)
        if (A * B + D - F + H * I) != 0:
            if (G + H * J - A * C + E) / (A * B + D - F + H * I) == solucion:
                textoOperacion = "$" + str(A) + "(" + str(B) + "x" + "+" + str(C) + ")" + "+" + str(D) + "x" + "-" + str(E) + "=" + str(F) + "x" + "+" + str(G) + "-" + str(H) + "(" + str(I) + "x" + "-" + str(J) + ")" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo6(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        F = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        if F != C and (F * A - C * D) != 0:
            if (C * E - F * B) / (F * A - C * D) == solucion:
                textoOperacion = "$" + r"\dfrac{" + str(A) + "x"
                if B > 0:
                    textoOperacion += "+" + str(B) + "}{" + str(C) + "} = "
                else:
                    textoOperacion += str(B) + "}{" + str(C) + "} = "
                textoOperacion += r"\dfrac{" + str(D) + "x"
                if E > 0:
                    textoOperacion += "+" + str(E) + "}{" + str(F) + "}" + "$"
                else:
                    textoOperacion += str(E) + "}{" + str(F) + "}" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo7(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        F = 1
        if (F * A - C * D) != 0:
            if (C * E - F * B) / (F * A - C * D) == solucion:
                textoOperacion = "$" + r"\dfrac{" + str(A) + "x"
                if B > 0:
                    textoOperacion += "+" + str(B) + "}{" + str(C) + "} = "
                else:
                    textoOperacion += str(B) + "}{" + str(C) + "} = "
                textoOperacion += str(D) + "x"
                if E > 0:
                    textoOperacion += "+" + str(E) + "$"
                else:
                    textoOperacion += str(E) + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo8(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        F = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        if (A * F * B - D) != 0:
            if (-A * F * C + E) / (A * F * B - D) == solucion:
                textoOperacion = "$" + str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + ") = "
                else:
                    textoOperacion += str(C) + ") = "
                textoOperacion += r"\dfrac{" + str(D) + "x"
                if E > 0:
                    textoOperacion += "+" + str(E) + "}{" + str(F) + "}" + "$"
                else:
                    textoOperacion += str(E) + "}{" + str(F) + "}" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaOperacionesTipo9(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        F = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        G = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        H = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        I = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        if (H * A * B - D * H - D * F - D * H * I) != 0:
            if (D * G - H * A * C + D * H * E) / (H * A * B - D * H - D * F - D * H * I) == solucion:
                textoOperacion = r"$\dfrac{" + str(A) + "(" + str(B) + "x"
                if C > 0:
                    textoOperacion += "+" + str(C) + ")}{" + str(D) + "}" + "-(x"
                else:
                    textoOperacion += str(C) + ")}{" + str(D) + "}" + "-(x"
                if E > 0:
                    textoOperacion += "+" + str(E) + ") = "
                else:
                    textoOperacion += str(E) + ") = "
                textoOperacion += r"\dfrac{" + str(F) + "x"
                if G > 0:
                    textoOperacion += "+" + str(G) + "}{" + str(H) + "}"
                else:
                    textoOperacion += str(G) + "}{" + str(H) + "}"
                if I > 0:
                    textoOperacion += "+" + str(I) + "x" + "$"
                else:
                    textoOperacion += str(I) + "x" + "$"
                listaOperaciones.append(textoOperacion)
                listaOperacionesUnicas = np.unique(listaOperaciones)
                contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaIdentidadTipo1(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        F = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        if A * B == D * E and A * C == D * F:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "(" + str(E) + "x"
            if F > 0:
                textoOperacion += "+" + str(F) + "$"
            else:
                textoOperacion += str(F) + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaIdentidadTipo2(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        if A * B == D and A * C == E:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "x"
            if E > 0:
                textoOperacion += "+" + str(E) + "$"
            else:
                textoOperacion += str(E) + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaIdentidadTipo3(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        F = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        if A * F == D * C and B * F == E * C:
            textoOperacion = r"$\dfrac{" + str(A) + "x"
            if B > 0:
                textoOperacion += "+" + str(B) + "}{" + str(C) + "} = "
            else:
                textoOperacion += str(B) + "}{" + str(C) + "} = "
            textoOperacion += r"\dfrac{" + str(D) + "x"
            if E > 0:
                textoOperacion += "+" + str(E) + "}{" + str(F) + "}$"
            else:
                textoOperacion += str(E) + "}{" + str(F) + "}$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaSinSolucionTipo1(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        F = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        if A * B == D * E and A * C != D * F:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "(" + str(E) + "x"
            if F > 0:
                textoOperacion += "+" + str(F) + ")$"
            else:
                textoOperacion += str(F) + ")$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaSinSolucionTipo2(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        if A * B == D and A * C != E:
            textoOperacion = "$" + str(A) + "(" + str(B) + "x"
            if C > 0:
                textoOperacion += "+" + str(C) + ") = "
            else:
                textoOperacion += str(C) + ") = "
            textoOperacion += str(D) + "x"
            if E > 0:
                textoOperacion += "+" + str(E) + "$"
            else:
                textoOperacion += str(E) + "$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


def generaSinSolucionTipo3(solucion, numeroOperacionesDistintas, maximoPositivo):
    contador = 0
    listaOperaciones = []
    while contador < numeroOperacionesDistintas:
        A = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        B = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        C = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        D = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        E = random.randrange(-1, 2, 2) * random.randrange(1, maximoPositivo)
        F = random.randrange(-1, 2, 2) * random.randrange(2, maximoPositivo)
        if A * F == D * C and B * F != E * C:
            textoOperacion = r"$\dfrac{" + str(A) + "x"
            if B > 0:
                textoOperacion += "+" + str(B) + "}{" + str(C) + "} = "
            else:
                textoOperacion += str(B) + "}{" + str(C) + "} = "
            textoOperacion += r"\dfrac{" + str(D) + "x"
            if E > 0:
                textoOperacion += "+" + str(E) + "}{" + str(F) + "}$"
            else:
                textoOperacion += str(E) + "}{" + str(F) + "}$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas


# Mapa de funciones para evitar exec()
_TIPOS = {
    1: generaOperacionesTipo1,
    2: generaOperacionesTipo2,
    3: generaOperacionesTipo3,
    4: generaOperacionesTipo4,
    5: generaOperacionesTipo5,
    6: generaOperacionesTipo6,
    7: generaOperacionesTipo7,
    8: generaOperacionesTipo8,
    9: generaOperacionesTipo9,
}
_IDENTIDADES = {1: generaIdentidadTipo1, 2: generaIdentidadTipo2, 3: generaIdentidadTipo3}
_SIN_SOL = {1: generaSinSolucionTipo1, 2: generaSinSolucionTipo2, 3: generaSinSolucionTipo3}


# -----------------------------------------------------------------------
# FUNCIÓN PRINCIPAL: llamada desde Flask
# -----------------------------------------------------------------------
def genera_pdf(ruta_datos, ruta_elementos, valorLetraA=-13, conDenominadores=0, directorio_trabajo="./"):
    """
    Genera el PDF de fichas de criptografía con ecuaciones de 1er grado.
    Devuelve la ruta al PDF generado.
    """
    start = time.time()

    maximoPositivo = int(1.25 * (valorLetraA + 30))
    numeroOperacionesDistintas = 4

    directorioFichas = os.path.join(directorio_trabajo, "fichas") + "/"
    os.makedirs(directorioFichas, exist_ok=True)

    codigoAlfabetico = funcionesBasicas.creaCodigoAlfabetico(valorLetraA)
    tema, elementos = funcionesBasicas.leeElementos(ruta_elementos)
    datos = funcionesBasicas.leeDatosCabecera(ruta_datos)
    rutaArchivoLaTeX, fLaTeX = funcionesBasicas.creaArchivoLaTeX(datos, ruta_elementos, directorioFichas)
    funcionesBasicas.escribePreambuloLaTeX(datos, fLaTeX)

    if conDenominadores == 0:
        numeroTiposOperaciones = 5
    else:
        numeroTiposOperaciones = 9

    cadenaSoluciones = r"\newpage{} \begin{itemize}[noitemsep] "
    for koko in range(len(elementos)):
        funcionesBasicas.escribeInicioFichaLaTeX(datos, tema, valorLetraA, fLaTeX)
        fLaTeX.write(r"\begin{small} Para desencriptarlo, tendrás que resolver las siguientes ecuaciones lineales, buscar su solución en la tabla y anotar la letra correspondiente. \textbf{Si es una identidad o una ecuación sin solución}, anota un espacio en blanco.\end{small}" + "\n")
        fLaTeX.write(r"\vspace{0.15\baselineskip}" + "\n")
        fLaTeX.write(r"\renewcommand{\arraystretch}{2.0}" + "\n")
        fLaTeX.write(r"\begin{footnotesize}" + "\n")
        fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|c|c|}" + "\n")
        fLaTeX.write(r"	\hline" + "\n")
        fLaTeX.write(r"	\textbf{Ecuación} & \textbf{Solución} & \textbf{Letra} \\" + "\n")
        fLaTeX.write(r"	\hline" + "\n")

        print(str(koko + 1), "de", str(len(elementos)), ":", elementos[koko])
        cadenaSoluciones += r" \item " + elementos[koko]
        operacionesDistintas = funcionesBasicas.generaOperacionesDistintas(numeroTiposOperaciones, len(elementos[koko]))

        for papa in range(len(elementos[koko])):
            if codigoAlfabetico.get(elementos[koko][papa]) is not None:
                cadenas = _TIPOS[operacionesDistintas[papa]](
                    codigoAlfabetico.get(elementos[koko][papa]),
                    numeroOperacionesDistintas,
                    maximoPositivo
                )
            else:
                if random.randrange(0, 2) == 0:
                    if conDenominadores == 0:
                        cadenas = _IDENTIDADES[random.randrange(1, 3)](0, numeroOperacionesDistintas, maximoPositivo)
                    else:
                        cadenas = _IDENTIDADES[random.randrange(1, 4)](0, numeroOperacionesDistintas, maximoPositivo)
                else:
                    if conDenominadores == 0:
                        cadenas = _SIN_SOL[random.randrange(1, 3)](0, numeroOperacionesDistintas, maximoPositivo)
                    else:
                        cadenas = _SIN_SOL[random.randrange(1, 4)](0, numeroOperacionesDistintas, maximoPositivo)

            pot = 2 * random.randrange(0, int(len(cadenas) / 2))
            fLaTeX.write(r"\footnotesize " + cadenas[pot] + r" & & \\\hline" + "\n")

        fLaTeX.write(r"\end{tabularx}" + "\n")
        fLaTeX.write(r"\end{footnotesize}" + "\n")
        funcionesBasicas.escribeFinalFichaLaTeX(fLaTeX)

    cadenaSoluciones += r" \end{itemize} "
    fLaTeX.write(cadenaSoluciones + "\n")
    fLaTeX.write(r"\end{document}" + "\n")
    fLaTeX.close()

    #subprocess.run(["pdflatex", "--interaction=batchmode", "-output-directory=" + directorioFichas, rutaArchivoLaTeX])

    resultado = subprocess.run(["pdflatex", "--interaction=nonstopmode", "-output-directory=" + directorioFichas, rutaArchivoLaTeX],capture_output=True,text=True)

    print("STDOUT pdflatex:", resultado.stdout[-3000:])
    print("STDERR pdflatex:", resultado.stderr[-1000:])

    end = time.time()
    print(len(elementos), "elementos procesados en", int(end - start), "segundos.")

    funcionesBasicas.limpiaArchivosAuxiliares(rutaArchivoLaTeX)

    rutaPDF = rutaArchivoLaTeX[0:-4] + ".pdf"
    return rutaPDF
