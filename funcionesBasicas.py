#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import math
import subprocess
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#######################################################################################
def generaOperacionesDistintas(numeroTiposOperaciones, longitudElemento):
    tiposOperaciones = []
    if isinstance(numeroTiposOperaciones, int):
        repeticiones = math.ceil(longitudElemento / numeroTiposOperaciones)
        for kuup in range(repeticiones):
            for kiop in range(numeroTiposOperaciones):
                tiposOperaciones.append(kiop + 1)
        random.shuffle(tiposOperaciones)
    elif isinstance(numeroTiposOperaciones, list):
        konti = 0
        for kuup in range(longitudElemento):
            if konti >= len(numeroTiposOperaciones):
                konti = 0
            tiposOperaciones.append(random.randint(numeroTiposOperaciones[konti][0], numeroTiposOperaciones[konti][1]))
            konti += 1
    return tiposOperaciones

#######################################################################################
def creaCodigoAlfabetico(valorLetraA):
    if valorLetraA is None:
        valorLetraA = -13
    codigoAlfabetico = {
        'A': valorLetraA,
        'Á': valorLetraA,
        'Ä': valorLetraA,
        'B': valorLetraA + 1,
        'C': valorLetraA + 2,
        'D': valorLetraA + 3,
        'E': valorLetraA + 4,
        'É': valorLetraA + 4,
        'Ë': valorLetraA + 4,
        'F': valorLetraA + 5,
        'G': valorLetraA + 6,
        'H': valorLetraA + 7,
        'I': valorLetraA + 8,
        'Í': valorLetraA + 8,
        'Ï': valorLetraA + 8,
        'J': valorLetraA + 9,
        'K': valorLetraA + 10,
        'L': valorLetraA + 11,
        'M': valorLetraA + 12,
        'N': valorLetraA + 13,
        'Ñ': valorLetraA + 14,
        'O': valorLetraA + 15,
        'Ó': valorLetraA + 15,
        'Ö': valorLetraA + 15,
        'P': valorLetraA + 16,
        'Q': valorLetraA + 17,
        'R': valorLetraA + 18,
        'S': valorLetraA + 19,
        'T': valorLetraA + 20,
        'U': valorLetraA + 21,
        'Ú': valorLetraA + 21,
        'Ü': valorLetraA + 21,
        'V': valorLetraA + 22,
        'W': valorLetraA + 23,
        'X': valorLetraA + 24,
        'Y': valorLetraA + 25,
        'Z': valorLetraA + 26
    }
    return codigoAlfabetico

#######################################################################################
# CAMBIO: ahora recibe la ruta directamente como parámetro, en lugar de leerla de argv
def leeElementos(rutaArchivoElementos):
    elementos = []
    with open(rutaArchivoElementos, 'r', errors='replace', encoding="latin-1") as fTxt:
        lines = fTxt.readlines()
        tema = lines[0]
        for linea in range(len(lines) - 1):
            elementos.append(lines[linea + 1][0:-1].upper())
    random.shuffle(elementos)
    return tema, elementos

#######################################################################################
# CAMBIO: ahora recibe la ruta directamente como parámetro, en lugar de leerla de argv
def leeDatosCabecera(rutaArchivosCabecera):
    Centro = []
    Nivel = []
    Curso = []
    Unidad = []
    Materia = []
    Autor = []
    Saberes = []
    CompetenciaCriterio = []
    Producto = []
    Escala = []
    Titulo = []
    Archivo = []

    with open(rutaArchivosCabecera, 'r', errors='replace', encoding="latin-1") as fTXT:
        lines = fTXT.readlines()
        for linea in range(len(lines)):
            posicionComas = lines[linea].find(',')
            texto = lines[linea]
            palabraClave = texto[0:posicionComas]
            if palabraClave == "Centro":
                Centro.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Nivel":
                Nivel.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Curso":
                Curso.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Unidad":
                Unidad.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Materia":
                Materia.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Autor":
                Autor.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Título":
                Titulo.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Saberes":
                Saberes.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Producto":
                Producto.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "CompetenciaCriterio":
                CompetenciaCriterio.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Escala":
                Escala.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
            elif palabraClave == "Archivo":
                Archivo.append(texto[posicionComas + 1:-1].replace(r"%", r"\%"))
    fTXT.close()

    datos = {
        "Centro": Centro[0],
        "Nivel": Nivel[0],
        "Curso": Curso[0],
        "Unidad": Unidad[0],
        "Materia": Materia[0],
        "Autor": Autor[0],
        "Título": Titulo[0],
        "Subtítulo": "",
        "Saberes": Saberes[0],
        "Producto": Producto[0],
        "CompetenciaCriterio": CompetenciaCriterio,
        "Escala": Escala[0],
        "Archivo": Archivo[0]
    }
    return datos

#######################################################################################
def creaArchivoLaTeX(datos, archivoElementos, directorioFichas):
    nombreArchivoElementos = archivoElementos[archivoElementos.rfind('/') + 1:-4]
    rutaArchivoLaTeX = directorioFichas + datos["Archivo"] + r"_" + nombreArchivoElementos + ".tex"
    fLaTeX = open(rutaArchivoLaTeX, "w", encoding="latin-1")
    return rutaArchivoLaTeX, fLaTeX

#######################################################################################
def escribePreambuloLaTeX(datos, fLaTeX):
    fLaTeX.write(r"\documentclass[14pt]{exam}" + "\n")
    fLaTeX.write(r"\RequirePackage{amssymb, amsfonts, amsmath, latexsym, verbatim, xspace}" + "\n")
    fLaTeX.write(r"\RequirePackage{tikz, pgflibraryplotmarks}" + "\n")
    
    fLaTeX.write(r"\graphicspath{{" + BASE_DIR.replace("\\", "/") + r"/imagenes/}}" + "\n")
    
    fLaTeX.write(r"\usepackage[utf8]{inputenc}" + "\n")
    fLaTeX.write(r"\usepackage[T1]{fontenc}" + "\n")
    fLaTeX.write(r"\usepackage[a4paper,margin=1.25cm,top=1.25in,bottom=0.50in,headheight=1.20in,headsep=0.15in,footskip=0.15in]{geometry}" + "\n")
    fLaTeX.write(r"\usepackage[normalem]{ulem}" + "\n")
    fLaTeX.write(r"\usepackage{pdflscape}" + "\n")
    fLaTeX.write(r"\usepackage{setspace}" + "\n")
    fLaTeX.write(r"\usepackage{soul}" + "\n")
    fLaTeX.write(r"\usepackage{ragged2e}")
    fLaTeX.write(r"\usepackage{fourier}" + "\n")
    fLaTeX.write(r"\usepackage{color}" + "\n")
    fLaTeX.write(r"\usepackage{selectp}" + "\n")
    fLaTeX.write(r"\usepackage{afterpage}" + "\n")
    fLaTeX.write(r"\usepackage{tabularx}" + "\n")
    fLaTeX.write(r"\usepackage{tcolorbox}" + "\n")
    fLaTeX.write(r"\usepackage{xcolor,colortbl}" + "\n")
    fLaTeX.write(r"\usepackage{amsmath}" + "\n")
    fLaTeX.write(r"\usepackage{enumitem}" + "\n")
    fLaTeX.write(r"\setlist[itemize]{align=parleft,left=5pt..11pt}" + "\n")
    fLaTeX.write(r"\usepackage{spalign}" + "\n")
    fLaTeX.write(r"\usepackage{multirow}" + "\n")
    fLaTeX.write(r"\usepackage{hyperref}" + "\n")
    fLaTeX.write(r"\usepackage{lastpage}" + "\n")
    fLaTeX.write(r"\usepackage{nicefrac}" + "\n")
    fLaTeX.write(r"\usepackage{caption}" + "\n")
    fLaTeX.write(r"\usepackage{xhfill}" + "\n")
    fLaTeX.write(r"\usepackage{dashrule}" + "\n")
    fLaTeX.write(r"\usepackage{graphicx}" + "\n")
    fLaTeX.write(r"\usepackage{framed}" + "\n")
    fLaTeX.write(r"\usepackage{xpatch}" + "\n")
    fLaTeX.write(r"\usepackage{cancel}" + "\n")
    fLaTeX.write(r"\usepackage{xlop}" + "\n")
    fLaTeX.write(r"\usepackage{relsize}" + "\n")
    fLaTeX.write(r"\usepackage{tkz-euclide}" + "\n")
    fLaTeX.write(r"\usetikzlibrary{hobby} " + "\n")
    fLaTeX.write(r"\usepackage[english,spanish]{babel}" + "\n")
    fLaTeX.write(r"\usepackage{textgreek}" + "\n")
    fLaTeX.write(r"\usepackage[autostyle]{csquotes}" + "\n")
    fLaTeX.write(r"\makeatletter" + "\n")
    fLaTeX.write(r"\newcommand\notsotiny{\@setfontsize\notsotiny\@vipt\@viipt}" + "\n")
    fLaTeX.write(r"\makeatother" + "\n")
    fLaTeX.write(r"\usepackage[gobble=auto,runall]{pythontex}" + "\n")
    fLaTeX.write(r"\definecolor{grisPregunta}{rgb}{0.925, 0.925, 0.925}" + "\n")
    fLaTeX.write(r"\definecolor{grisActividad}{rgb}{0.725, 0.725, 0.725}" + "\n")
    fLaTeX.write(r"\definecolor{grisTeoríaTítulo}{rgb}{0.25, 0.25, 0.25}" + "\n")
    fLaTeX.write(r"\definecolor{grisTeoríaSubtítulo}{rgb}{0.35, 0.35, 0.35}" + "\n")
    fLaTeX.write(r"\definecolor{asparagus}{rgb}{0.53, 0.66, 0.42}" + "\n")
    fLaTeX.write(r"\definecolor{applegreen}{rgb}{0.55, 0.71, 0.0}" + "\n")
    fLaTeX.write(r"\definecolor{alizarin}{rgb}{0.82, 0.1, 0.26}" + "\n")
    fLaTeX.write(r"\definecolor{amber}{rgb}{1.0, 0.75, 0.0}" + "\n")
    fLaTeX.write(r"\definecolor{cadmiumyellow}{rgb}{1.0, 0.96, 0.0}" + "\n")
    fLaTeX.write(r"\definecolor{carrotorange}{rgb}{0.93, 0.57, 0.13}" + "\n")
    fLaTeX.write(r"\definecolor{electricviolet}{rgb}{0.56, 0.0, 1.0}" + "\n")
    fLaTeX.write(r"\definecolor{electriccrimson}{rgb}{1.0, 0.0, 0.25}" + "\n")
    fLaTeX.write(r"\definecolor{forestgreen}{rgb}{0.13, 0.55, 0.13}" + "\n")
    fLaTeX.write(r"\AtEndDocument{\clearpage\ifodd\value{page}\else\null\clearpage\fi}" + "\n")
    fLaTeX.write(r"\makeatletter" + "\n")
    fLaTeX.write(r"\def\graphicspath#1{\def\Ginput@path{#1}\edef\moodleimgpath{\@firstofone#1}}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\xpatchcmd{\moodle@includegraphics@int@int}%" + "\n")
    fLaTeX.write(r"{\openssl\otherspace enc -base64 -in #2.png -out #2.enc}%" + "\n")
    fLaTeX.write(r"{\openssl\otherspace enc -base64 -in \moodleimgpath#2.png -out #2.enc}%" + "\n")
    fLaTeX.write(r"{\typeout{patch ok}}%" + "\n")
    fLaTeX.write(r"{\typeout{patch failed}}" + "\n")
    fLaTeX.write(r"\makeatother" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\pointpoints{punto}{puntos}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\renewcommand{\familydefault}{\sfdefault}" + "\n")
    fLaTeX.write(r"\usepackage[scaled=1]{helvet}" + "\n")
    fLaTeX.write(r"\usepackage[helvet]{sfmath}" + "\n")
    fLaTeX.write(r"\everymath={\sf}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\parindent 0ex" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\linespread{1.2}" + "\n")
    fLaTeX.write(r"\pagestyle{headandfoot}" + "\n")
    fLaTeX.write(r"\firstpagefooter{\footnotesize\textcolor{lightgray}{" + datos['Autor'] + r"}}{}{}" + "\n")
    fLaTeX.write(r"\runningfooter{\footnotesize\textcolor{lightgray}{" + datos['Autor'] + r"}}{}{}" + "\n")
    fLaTeX.write(r"\firstpageheader{\includegraphics[height=0.75in]{logoCilniana_horizontal_5cm}}{ }{\large \textbf{\textcolor{darkgray}{Actividad criterial}} \\  \textbf{\textcolor{darkgray}{ " + datos['Nivel'] + r" " + datos['Materia'] + r"}}\\ \large \textcolor{darkgray}{ " + datos['Título'] + r"}}" + "\n")
    fLaTeX.write(r"\runningheader{\includegraphics[height=0.75in]{logoCilniana_horizontal_5cm}}{ }{\large \textbf{\textcolor{darkgray}{Actividad criterial}} \\  \textbf{\textcolor{darkgray}{ " + datos['Nivel'] + r" " + datos['Materia'] + r"}}\\ \large \textcolor{darkgray}{ " + datos['Título'] + r"}}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\renewcommand\thefootnote{\@fnsymbol\c@footnote}" + "\n")
    fLaTeX.write(r"\renewcommand\thefootnote{\alph{footnote}}" + "\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{1.00}" + "\n")
    fLaTeX.write(r"\setlength{\tabcolsep}{1.5 pt}" + "\n")
    fLaTeX.write(r"\setlength{\fboxrule}{0.50pt}" + "\n")
    fLaTeX.write(r"\setlength{\fboxsep}{1.5pt}" + "\n")
    fLaTeX.write(r"\begin{document}" + "\n")
    fLaTeX.write(r"" + "\n")

def escribeInicioFichaLaTeX(datos, tema, valorLetraA, fLaTeX):
    fLaTeX.write(r"\renewcommand{\arraystretch}{0.65}" + "\n")
    fLaTeX.write(r"\vspace{0.5\baselineskip}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\noindent\flushleft\includegraphics[height=0.35in]{ejercicio}\hspace{0.1cm}\raisebox{1.75ex}{\fcolorbox{grisActividad}{grisActividad}{\parbox{0.9365\textwidth}{\Large \textbf{\textcolor{black}{  " + datos['Título'] + r"}}\\ \scriptsize \textcolor{black}{" + datos['Subtítulo'] + r"}}}}}\vspace{0.25\baselineskip}" + "\n")
    fLaTeX.write(r"" + "\n")
    texto = datos["Saberes"]
    fLaTeX.write(r"\renewcommand{\arraystretch}{0.55} \raisebox{0.00ex}{\fcolorbox{black}{white}{\parbox{\textwidth - 5\fboxsep}{\notsotiny \setstretch{0.500} \textcolor{black}{  \textbf{Saberes básicos}\\ " + texto + r"}}}}\renewcommand{\arraystretch}{1.00}" + "\n")
    texto = datos["Producto"]
    fLaTeX.write(r"\renewcommand{\arraystretch}{0.55} \raisebox{0.00ex}{\fcolorbox{black}{white}{\parbox{\textwidth - 5\fboxsep}{\notsotiny \setstretch{0.500} \textcolor{black}{  \textbf{Producto/instrumento de evaluación}\\ " + texto + r"}}}}\renewcommand{\arraystretch}{1.00}" + "\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{0.65}" + "\n")
    fLaTeX.write(r"\setlength\tabcolsep{1.5 pt}" + "\n")
    for nutu in range(len(datos["CompetenciaCriterio"])):
        texto = datos["CompetenciaCriterio"][nutu]
        partes = texto.split('---')
        fLaTeX.write(r"\renewcommand{\arraystretch}{0.35} \raisebox{0.00ex}{\fcolorbox{black}{grisActividad}{\parbox{\textwidth - 5\fboxsep}{\notsotiny \setstretch{0.500} \textcolor{black}{  \textbf{Competencia específica} " + partes[0] + r"} \\ \textcolor{black}{  \textbf{Criterio} " + partes[1] + r"}}}}\renewcommand{\arraystretch}{1.00}" + "\n")
    texto = datos["Escala"]
    partes = texto.split('---')
    tipoEscala = partes[0]
    kkop = r"\noindent \renewcommand{\arraystretch}{1.15}\begin{tabularx}{0.9935\textwidth}{|X|p{0.085\textwidth}|} \hline "
    for nujiop in range(len(partes) - 1):
        kkop += r" \setstretch{0.500} \notsotiny \cellcolor{grisPregunta}{" + partes[nujiop + 1] + r"}  & \\\hline "
        kkop += r"\end{tabularx}\renewcommand{\arraystretch}{1.00}" + "\n"
        fLaTeX.write(kkop)
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\vspace{0.5\baselineskip}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\small\justify{En esta ficha se ha encriptado \textbf{" + tema + r"} usando un cifrado de sustituci\'{o}n. Cada letra ha sido sustituida por un n\'{u}mero entero, de acuerdo con la siguiente tabla:}" + "\n")
    fLaTeX.write(r"\vspace{-0.25\baselineskip}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{0.8}" + "\n")
    fLaTeX.write(r"\begin{center}" + "\n")
    fLaTeX.write(r"	\begin{footnotesize}" + "\n")
    fLaTeX.write(r"		\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}" + "\n")
    fLaTeX.write(r"			\hline" + "\n")
    fLaTeX.write(r"			A & B & C & D & E & F & G & H & I & J & K & L & M & N & Ñ & O & P & Q & R & S & T & U & V & W & X & Y & Z \\" + "\n")
    fLaTeX.write(r"			\hline" + "\n")
    fLaTeX.write(r"			" + str(valorLetraA) + r" & " + str(valorLetraA + 1) + r" & " + str(valorLetraA + 2) + r" & " + str(valorLetraA + 3) + r" & " + str(valorLetraA + 4) + r" & " + str(valorLetraA + 5) + r" & " + str(valorLetraA + 6) + r" & " + str(valorLetraA + 7) + r" & " + str(valorLetraA + 8) + r" & " + str(valorLetraA + 9) + r" & " + str(valorLetraA + 10) + r" & " + str(valorLetraA + 11) + r" & " + str(valorLetraA + 12) + r" & " + str(valorLetraA + 13) + r" & " + str(valorLetraA + 14) + r" & " + str(valorLetraA + 15) + r" & " + str(valorLetraA + 16) + r" & " + str(valorLetraA + 17) + r" & " + str(valorLetraA + 18) + r" & " + str(valorLetraA + 19) + r" & " + str(valorLetraA + 20) + r" & " + str(valorLetraA + 21) + r" & " + str(valorLetraA + 22) + r" & " + str(valorLetraA + 23) + r" & " + str(valorLetraA + 24) + r" & " + str(valorLetraA + 25) + r" & " + str(valorLetraA + 26) + r" \\" + "\n")
    fLaTeX.write(r"			\hline" + "\n")
    fLaTeX.write(r"		\end{tabular}" + "\n")
    fLaTeX.write(r"	\end{footnotesize}" + "\n")
    fLaTeX.write(r"\end{center}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\vspace{-0.25\baselineskip}" + "\n")

#######################################################################################
def escribeFinalFichaLaTeX(fLaTeX):
    fLaTeX.write(r"\vspace{0\baselineskip}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\renewcommand{\arraystretch}{0.85}" + "\n")
    fLaTeX.write(r"\noindent\begin{tabularx}{\textwidth}{|X|}" + "\n")
    fLaTeX.write(r"	\hline " + "\n")
    fLaTeX.write(r"	\cellcolor{white}{\textbf{\textcolor{black}{\small Lo encriptado en este ficha era:}}} \\\hline" + "\n")
    fLaTeX.write(r"\end{tabularx} " + "\n")
    fLaTeX.write(r"\vspace{\fill}" + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"\newpage" + "\n")

#######################################################################################
def limpiaArchivosAuxiliares(rutaArchivoLaTeX):
    for ext in [".pytxcode", ".log", ".aux", ".out"]:
        subprocess.run(["rm", "-f", rutaArchivoLaTeX[0:-4] + ext])
