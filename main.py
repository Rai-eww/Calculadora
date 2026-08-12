def main ():
    operacao = input("Digite seu calculo: ")
    calcular(operacao)

def calcular(operacao):
    try:
        resultado = eval(operacao) 
        #Eval pega uma String e tentar calcular em formato de expressão.
        print("Resultado: ", resultado)

    except ZeroDivisionError: 
        #Se retornar o erro de "Não é possivel dividir por 0" retornaremos esse print.
        print("Não é possivel dividir por 0.")
    except: 
        #Caso aconteça outro erro, retornaremos esse print.
        print("Calculo não reconhecido.")
main()

