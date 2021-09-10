import os

#ENTRA NA PASTA
os.chdir('C:\\Users\\Robson\\Desktop\\PROJETO - EXTRAÇÃO')

#LISTA A PASTA
os.listdir() #<- Não preciso colocar nada, porque já entrei na pasta. Porém eu poderia
             #PODERIA COLOCAR ESSE LISTDIR em um Var

for i in os.listdir():
    if i == 'RECOVER': #ESSE IF É PORQUE SERÁ MOVIDO PARA CÁ
        continue
    if i == 'AuladeMover.py': #ESSE IF É PORQUE ELE É O PROGRAMA
        continue
    print(i)                                                            #SE NÃO COLOCAR O \\ NO FINAL, A FUNÇÃO IRA RENOMEAR DENTRO DA PASTA ANTERIOR
    os.rename(i,'C:\\Users\\Robson\\Desktop\\PROJETO - EXTRAÇÃO\\RECOVER\\' + i) #FUNCAO PARA MOVER ARQUIVOS DE COLAR EM OUTRO LUGAR
              #O I SERÁ RECORTA                                 #ESSE ARQUIVO VAI RECEBER + I