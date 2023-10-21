from math import sqrt

epsilon = 10 ** -10
delta = 1.0

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))


def f(x):
    return x ** 3 + a * x ** 2 + b * x + c


def discriminant():
    return (2 * a) ** 2 - 4 * 3 * b


def x_min():
    return (-2 * a - sqrt(discriminant())) / (2 * 3)


def x_max():
    return (-2 * a + sqrt(discriminant())) / (2 * 3)


def f_min():
    return f(x_max())


def f_max():
    return f(x_min())


def get_range_by_negative_shift(initial_x_from):
    x_from = initial_x_from - delta
    while not f(x_from) < -epsilon:
        x_from -= delta

    x_to = x_from + delta

    return x_from, x_to


def get_range_by_positive_shift(initial_x_to):
    x_to = initial_x_to + delta
    while not f(x_to) > epsilon:
        x_to += delta

    x_from = x_to - delta

    return x_from, x_to


def get_root_by_bisection_method(x_from, x_to):
    result_x_from = x_from
    result_x_to = x_to
    result = (result_x_from + result_x_to) / 2

    while not abs(f(result)) < epsilon:
        if f(result) < -epsilon:
            result_x_from = result
        elif f(result) > epsilon:
            result_x_to = result

        result = (result_x_from + result_x_to) / 2

    return result


def solve():
    if discriminant() <= 0:
        if abs(f(0)) < epsilon:
            print("One root: x is 0")
        elif f(0) > epsilon:
            x_from, x_to = get_range_by_negative_shift(0)
            x = get_root_by_bisection_method(x_from, x_to)

            print(f"One root: x is {x}")
        elif f(0) < -epsilon:
            x_from, x_to = get_range_by_positive_shift(0)
            x = get_root_by_bisection_method(x_from, x_to)

            print(f"One root: x is {x}")

    else:
        if f_min() > epsilon:
            x_from, x_to = get_range_by_negative_shift(x_min())
            x = get_root_by_bisection_method(x_from, x_to)

            print(f"One root: x is {x}")
        elif f_max() < -epsilon:
            x_from, x_to = get_range_by_positive_shift(x_max())
            x = get_root_by_bisection_method(x_from, x_to)

            print(f"One root: x is {x}")

        elif abs(f_max()) < epsilon and f_min() < -epsilon:
            first_x = x_min()

            second_x_from, second_x_to = get_range_by_positive_shift(x_max())
            second_x = get_root_by_bisection_method(second_x_from, second_x_to)

            print(f"Two roots: first x is {first_x}, second x is {second_x}")
        elif f_max() > epsilon > abs(f_min()):
            first_x_from, first_x_to = get_range_by_negative_shift(x_min())
            first_x = get_root_by_bisection_method(first_x_from, first_x_to)

            second_x = x_max()

            print(f"Two roots: first x is {first_x}, second x is {second_x}")
        elif abs(f_max()) < epsilon and abs(f_min()) < epsilon:
            x = (x_min() + x_max()) / 2

            print(f"Three roots: first x is {x}, second x is {x}, third x is {x}")

        elif f_max() > epsilon and f_min() < -epsilon:
            first_x_from, first_x_to = get_range_by_negative_shift(x_min())
            first_x = get_root_by_bisection_method(first_x_from, first_x_to)

            second_x = get_root_by_bisection_method(x_max(), x_min())

            third_x_from, third_x_to = get_range_by_positive_shift(x_max())
            third_x = get_root_by_bisection_method(third_x_from, third_x_to)

            print(f"Three roots: first x is {first_x}, second x is {second_x}, third x is {third_x}")


if __name__ == "__main__":
    solve()
