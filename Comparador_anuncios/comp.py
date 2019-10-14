#texto_1 = 'https://www.indeed.com.br/jobs?q=Cientista%20Dados&start=70&vjk=e1c71dec9e863266'
#texto_2 = 'https://www.indeed.com.br/jobs?q=Cientista%20Dados&start=70&vjk=453acfa691622815'

def comparacao(objeto_1, objeto_2):
    if objeto_1 == objeto_2:
        print('Integralmente iguais\n')
    else:
        print('Integralmente diferentes\n')

    objeto_1 = objeto_1.replace('.', ' ')
    objeto_2 = objeto_2.replace('.', ' ')

    palavras_1 = objeto_1.split(' ')
    palavras_2 = objeto_2.split(' ')

    for i in palavras_1:
        for j in palavras_2:
            if i == j and i != 'https://www' and i != 'com':
                print('Semelhanças:')
                print(j)


#comparacao(texto_1, texto_2)

