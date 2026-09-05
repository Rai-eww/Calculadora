def calcular(calculo):
    try:
        resultado = eval(calculo) 
        return resultado

    except ZeroDivisionError: 
        return "Não é possivel dividir por 0."
    except NameError as e: 
        return "Erro: " + str(e)