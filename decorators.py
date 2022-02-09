from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        elapsed_time = final_time - initial_time
        print(f'Pasaron {elapsed_time.total_seconds()} segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1,100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre: str = "Cesar"):
    print(f'Hola {nombre}')

random_func()
suma(3,4)
saludo("Jaime")