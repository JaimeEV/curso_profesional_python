import random

def juego_azar(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        menu = """
        ¡Premio decorador!
        _________________________________________________
        Adivina el número y gana un premio, ¿estás listo?
        _________________________________________________
        """
        num_secreto = str(random.randint(1,10))
        is_num = False
        print(menu)
        while is_num == False:
            num_usu = input("Dime un número del 1 al 10: ")
            if num_usu.isnumeric():
                break
            else:
                print(f'Uppp, debes de introducir un número')
        if num_secreto == num_usu:
            print("¡Felicidades, has adivinado el número secreto, has ganado!")
        else:
            print(f"Los siento, el número secreto era {num_secreto}")
    return wrapper


@juego_azar
def saludo(nombre: str) -> str:
    print(f'Hola {nombre} hoy es un excelente día')

def run():
    saludo("Jaime")

if __name__ == '__main__':
    run()
