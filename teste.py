
num= int(input('Digite um número:'))
tab=1

while num<0 or num>=1:
    while tab<=10:
        print(num,'x',tab,'=',num*tab)
        tab=tab+1
    num= int(input('Digite um número:'))
    tab=1
print('Não tem tabuada do 0')
print('Essa é a tabuada do número digitado')


