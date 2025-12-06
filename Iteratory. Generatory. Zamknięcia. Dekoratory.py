#zadanie 1
class picun:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield i ** 1


iterable_gen = picun(5)

for value in iterable_gen:
    print(value)

#zadanie 2
def checker(*exc_types):
    def decorator(function):
        def wrapper(expression):
            try:
                result = function(expression)
            except exc_types as exc:
                print(f"Problem: {exc}")
                if isinstance(exc, ZeroDivisionError):
                    print("Rozwiązanie: Dzielnik nie może być równy 0")
                elif isinstance(exc, SyntaxError):
                    print("Rozwiązanie: Sprawdź poprawność wyrażenia")
                elif isinstance(exc, NameError):
                    print("Rozwiązanie: Używaj tylko liczb i prawidłowych zmiennych")
                else:
                    print("Rozwiązanie: Sprawdź wyrażenie ")
            else:
                print(f" {result}")
        return wrapper
    return decorator


@checker(NameError, TypeError, SyntaxError, ZeroDivisionError)
def calculate(expression):
    return eval(expression)


def main():
    print("Kalkulator")


    while True:
        user_input = input(">>> ")
        if user_input.lower() == "exit":
            print("Koniec")
            break
        if not user_input.strip():
            continue
        calculate(user_input)


main()
