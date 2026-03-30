while True: 
    try:
        numA = float(input(": "))
        numB = float(input(": "))

        print(f"Divisão: {numA/numB}")
        break

    except ValueError:
        print("Valor invalido")

    except ZeroDivisionError:
        print("Tentou dividir por 0")
        
    except Exception as e:
        print(f"Ocorreu um erro do tipo: {e}")