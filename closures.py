def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater


def run():
    repeate_5 = make_repeater_of(5)
    print(repeate_5("Hola"))
    repeate_10 = make_repeater_of(10)
    print(repeate_10("Platzi))


if __name__ == '__main__':
    run()