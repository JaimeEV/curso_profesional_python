def is_prime(num: int) -> bool:
    numbers_list = [ x for x in range(2, num+1) if (num % x == 0)]
    return len(numbers_list) == 1

def run():
    num: int = int(input("Ingresa un número: "))
    if num > 1 :
        print(is_prime(num))
    else:
        print("Ingresa un número mayor que 0")


if __name__ == '__main__':
    run()