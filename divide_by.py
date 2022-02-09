def make_division_by(n):
    """ This function returns a function that returns the division 
    of an x number by n """
    def division(x):
        assert (type(x) == int) and (x != 0), "Solo puedes introducir números que sean diferenes a 0 "
        return x / n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == '__main__':
    run()
