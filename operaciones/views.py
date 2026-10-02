from django.http import HttpResponse

def calcular(request, num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    resultado = f"""
    <h1>Operaciones</h1>
    <p>Suma: {suma}</p>
    <p>Resta: {resta}</p>
    <p>Multiplicación: {multiplicacion}</p>
    """

    return HttpResponse(resultado)
