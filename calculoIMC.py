print('\033[1;97m-' * 20)
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
print('\033[1;97m-' * 20)

imc = peso / (altura * altura)

if imc < 18.5:
    print('\033[1;91mAbaixo do peso.\033[1;91m\n')

elif imc > 18.5 and imc <= 25:
    print('\033[1;32mPeso ideal\033[m\n')

elif imc >= 25 and imc <= 30:
    print('\033[1;33mSobrepeso\033[1;33m\n')

elif imc >= 30 and imc <= 40:
    print('\033[1;31mObesidade\033[1;31m\n')

elif imc > 40:
    print('\033[1;91mObesidade mórbida\033[1;91m\n')