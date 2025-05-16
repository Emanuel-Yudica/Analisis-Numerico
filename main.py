import sympy as sp

def main(f_str):

    # Diccionario personalizado para distinguir ln y log
    namespace = {
        'ln': sp.log,              # ln(x) = log(x) base e
        'log': lambda x: sp.log(x, 10),  # log(x) = log base 10
        'sin': sp.sin,
        'cos': sp.cos,
        'tan': sp.tan,
        'exp': sp.exp,
        'sqrt': sp.sqrt,
        'pi': sp.pi,
        'e': sp.E,
    }

    # Parsear la función con contexto personalizado
    f = sp.sympify(f_str, locals=namespace)

    # Extraer variables de la función ya parseada
    free_symbols_list = list(f.free_symbols)  # set a list
    variables = []
    for i in range(len(free_symbols_list)):
        variables.append(str(free_symbols_list[i]))

    variables = sorted(variables)
    valores = []
    cotas = []

    # Definir simbolos
    simbolos = {}
    for i in range(len(variables)):
        simbolos[variables[i]] = sp.Symbol(variables[i])


    # Pedir Valores
    for i in range(len(variables)):
        valor = float(input(f"Valor de la variable {variables[i]}: "))
        cota = input(f"Cota de la variable {variables[i]}: ")
        

        if cota == "":
            if valor >=1:
                cota = 0.5
            else:
                valor_str = str(valor)
                for digito in '123456789':
                    valor_str = valor_str.replace(digito, '0')
                cota = float(valor_str + '5')

        valores.append(valor)
        cotas.append(float(cota))
    

    

    subs = {simbolos[var]: val for var, val in zip(variables, valores)}


    # Evaluar Funcion
    valor_real = f.subs(subs).evalf()
    print("\nValor de la función en el punto dado:", round(valor_real, 4))

    # Derivadas parciales
    derivadas = []

    for var in variables:
        derivadas.append(sp.diff(f, simbolos[var]))


    # Evaluar derivadas en el punto
    derivadas_punto = []
    for var, derivada in zip(variables, derivadas):
        df = derivada.subs(subs).evalf()
        derivadas_punto.append(df)
        print(f"Derivada parcial respecto a {var}: {round(df, 4)}")

    # Calcular cota total usando la formula del diferencial total

    error_absoluto = 0
    for valor, cota in zip(derivadas_punto, cotas):
        error_absoluto += abs(valor)*abs(cota)
    
    error_relativo = error_absoluto/abs(valor_real)
    error_porcentual = error_relativo*100

    print(f"Error absoluto: {error_absoluto}")
    print(f"Error relativo: {error_relativo}")
    print(f"Error porcentual: {error_porcentual}%")


if __name__ == '__main__':
    print("Funcion de ejemplo: 2*x**2+2*y**2+2*z**2") 

    print("Sintaxis de operaciones: https://chatgpt.com/share/6813974c-3fac-800e-9ca9-fb1f0d1e85b0")
    
    f = input("Inserte su funcion (usar letras de variables):\n> ")
    main(f)
        except :
            print("Error: La expresión ingresada no es válida.")
