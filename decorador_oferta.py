from datetime import datetime



def oferta_countdown(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        elapsed_time = final_time - initial_time
        print(f'Pasaron {elapsed_time.total_seconds()} segundos')
    return wrapper



@oferta_countdown
def welcome(name):
    print(f"Welcome {name} is nice to see you again")


def run():
    user_name = input("What's your name?: ")
    welcome(user_name)



if __name__ == '__main__':
    run()