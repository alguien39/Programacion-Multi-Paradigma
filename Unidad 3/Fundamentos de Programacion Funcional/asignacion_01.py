def crear_transformador(funcion):
    def transformador(lista):
        return [funcion(x) for x in lista]
    return transformador

def crear_filtro(predicado):
    def filtro(lista):
        return [x for x in lista if predicado(x)]
    return filtro

def crear_reductor(func, valor_inicial):
    def reductor(lista):
        acumulador = valor_inicial
        for x in lista:
            acumulador = func(acumulador,x)
        return acumulador
    return reductor

def componer(*funciones):
    def pipeline(valor):
        for func in funciones:
            valor = func(valor)
        return valor
    return pipeline

#Funciones A utilizar
def es_positivo(x):
    return x > 0

def al_cuadrado(x):
    return x * x

def sumar(acc, x):
    return acc + x


pipeline = componer(
    crear_filtro(es_positivo),
    crear_transformador(al_cuadrado),
    crear_reductor(sumar, 0)
)

numeros = [1, -2, 3, -4, 5]
print(pipeline(numeros))

numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]
print(pipeline(numeros))