def main ():
    operacao = input("Digite seu calculo: ")
    calcular(operacao)

def calcular(operacao):
    try:
        resultado = eval(operacao) 
        print("Resultado: ", resultado)

    except ZeroDivisionError: 
        print("Não é possivel dividir por 0.")
    except: 
        print("Calculo não reconhecido.")
main()

