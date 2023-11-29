def somar(memoria,numero):
    return memoria + numero

def subtrair(memoria,numero):
    return memoria - numero

def multiplicar(memoria,numero):
    return memoria * numero

def dividir(memoria,numero):
    if numero !=0:
        return memoria/numero
    else:
        print('Erro: divisão por zero')
        return memoria

def limparMemória(memoria):
    memoria = 0
    return memoria  
    
if __name__=="__main__":

    op = 0
    memoria=0    
    while op!= 6:
        print('1-somar')
        print('2-subtrair')
        print('3-multiplicar')
        print('4-Dividir')
        print('5-Apagar memória')
        print('6-sair do programa')
        op=int(input('digite sua opção:'))

        if op==1:
            print('Somar')
            print(f'memoria atual:{memoria}')
            numero = float(input('Numero a ser somado:'))
            memoria = somar(memoria,numero)
            print(memoria)

        if op==2:
            print('Subtrair')
            print(f'memoria atual:{memoria}')
            numero = float(input('Numero a ser subtraido:'))
            memoria = subtrair(memoria,numero)
            print(memoria)

        if op==3:
            print('Multiplicar')
            print(f'memoria atual:{memoria}')
            numero = float(input('Numero a ser multiplicado:'))
            memoria = multiplicar(memoria,numero)
            print(memoria)

        
        if op==4:
            print('Dividir')
            print(f'memoria atual:{memoria}')
            numero = float(input('Numero a ser Dividido:'))
            memoria = dividir(memoria,numero)
            print(memoria)

        if op==5:
            print('Apagando Memória....')
            memoria = limparMemória(memoria)
            print(memoria)

        if op==6:
            print('Fechando calculadora....')
            break         