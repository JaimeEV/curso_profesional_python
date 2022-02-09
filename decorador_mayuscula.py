def decorador(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@decorador
def mensaje(nombre):
    return f'{nombre} recibiste un mensaje'


print(mensaje("Cesar"))
print(mensaje("Julieta"))