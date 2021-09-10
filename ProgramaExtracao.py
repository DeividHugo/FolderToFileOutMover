import os
from tkinter import filedialog

PastaAtual =  filedialog.askdirectory() #Abri arquivos filedialog.askopenfilename()
os.chdir(PastaAtual) #FIZ ASSIM PARA OS DITORIOS A BAIXO RECONHECEREM, SEM EU PRECISAR FICAR PONDO DIRETORIOS

for i in os.listdir(): #LISTADIR SERVER PARA LISTA OS ARQUIVOS E PASTAS DENTRO DO DIRETORIO
    if ( '.' in i): #NÃO ACEITAR ARQUIVOS, SÓ PASTAS | #NÃO RETORNA APENAS OS INDICES, MAS TAMBÉM OS DIRETORIOS
        continue
    for x in os.listdir(i):
        os.chdir(i) #ABRINDO A PASTA QUE ESTÁ O ARQUIVO | #SAI DA PASTA PRINCIPAL
        os.rename(x, PastaAtual + '/'+ x) #MOVENDO ARQUIVO DA PASTA QUE ELE ESTÁ, PARA PASTA ATUAL
        os.chdir(PastaAtual) #RETORNANDO A PASTA PRINCIPAL, PARA NÃO HAVER ERROS, E O CHDIR ABRIR APATIR DAQ
    os.rmdir(i) #EXCLUIR AS PASTAS QUE ESTAVAM OS ARQUIVOS

