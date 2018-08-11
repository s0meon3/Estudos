#Funçoes
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mut(x,y):
    return x*y
def div(x,y):
    return x/y

#Variaveis
x = int(input('\nDigite o primeiro numero a ser calculado:'))
y = int(input('Digite o segundo numero a ser calculado:'))
choic = (input('Escolha uma das operacoes disponiveis(+,-,*,/)'))

#Execuçao do codigo
if choic == '+':
    print(x,'+',y,'=',add(x,y))
elif choic == '-':
    print(x,'-',y,'=',sub(x,y))
elif choic == '*':
    print(x,'*',y,'=',mut(x,y))
elif choic == '/':
    print(x,'/', y,'=',div(x,y))
else:
    print('Coloque uma opcao valida')