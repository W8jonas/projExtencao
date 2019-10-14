import PyPDF2
from comp import *

def extrator(name):
    pdfFile = open('pdfs\\' + name, 'rb')
    pdfObj = PyPDF2.PdfFileReader(pdfFile)

    total_paginas = pdfObj.numPages

    pagina = pdfObj.getPage(0)

    texto = pagina.extractText()

    _texto = texto.split()

    cont = 0
    link = ''
    abertura = False
    total = []

    for i in _texto:
        if i == 'Link:':
            abertura = True
            #print('abertura', cont, _texto[cont])

        if abertura == True:
            link += _texto[cont]
            #print('abertura == true', cont)

        if i == 'Anuncio':
            #print('fechou', cont)
            abertura = False
            total.append(link)
            link = ''

        cont += 1


    linkSeparado = total.__str__().replace(', ', '\n')
    linkSeparado = linkSeparado.replace("'", '')
    linkSeparado = linkSeparado.replace('[', '')
    linkSeparado = linkSeparado.replace(']', '')

    print('total extraído: ', linkSeparado)

    arquivo = open('linksExtraidos.txt', 'w')
    arquivo.write(linkSeparado)
    arquivo.close()

    comparacao(total[1], total[2])
