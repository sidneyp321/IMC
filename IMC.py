import os


def top():
    nome = (input("Informe seu Nome: "))
    idade = (input("Qual sua Idade: "))
    peso = float(input("Qual seu peso. Ex: 60,80,90: "))
    altura = float(input("Qual sua altura. Ex: 1.70: "))
    return nome, idade, peso, altura


try:
    nome = (input("Informe seu Nome: "))
    idade = (input("Qual sua Idade: "))
    peso = float(input("Qual seu peso. Ex: 60,80,90: "))
    altura = float(input("Qual sua altura. Ex: 1.70: "))


    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    formula = altura * altura
    imc = peso / formula


    if imc < 18.5:
        print(nome, "Seu IMC é: %.2f " % imc)
        print("Sua Classificação é: MAGREZA")
        print("Seu grau de obesidade é: 0")

    elif imc >= 18.5 and imc <= 24.9:
        print(nome, "Seu IMC é: %.2f " % imc)
        print("Sua Classificação é: NORMAL")
        print("Seu grau de obesidade é: 0")

    elif imc >= 25.0 and imc <= 29.9:
        print(nome, "Seu IMC é: %.2f " % imc)
        print("Sua Classificação é: SOBREPESO")
        print("Seu grau de obesidade é: 1")

    elif imc >= 30.0 and imc <= 39.9:
        print(nome, "Seu IMC é: %.2f " % imc)
        print("Sua Classificação é: OBESIDADE")
        print("Seu grau de obesidade é: 2")

    else:
        imc > 40
        print(nome, "Seu IMC é: %.2f " % imc)
        print("Sua Classificação é: OBESIDADE GRAVE")
        print("Seu grau de obesidade é: 3")

except NameError and ValueError:

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("USE APENAS 'NÚMEROS' e '.'")
    top()


