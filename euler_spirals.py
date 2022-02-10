import turtle


def decimal(p: int, q: int, base: int = 10):
    p = (p % q) * base
    while True:
        r = p % q
        yield (p - r) // q
        p = r * base


def draw_rational(
    p: int, q: int, base: int = 10, size: int = 1, iterations: int = 1000
):
    turtle.tracer(0)
    angle = 360 / base
    for (_, x) in zip(range(1, iterations + 1), decimal(p, q, base)):
        turtle.forward(size)
        turtle.left((x + 1) * angle)
    turtle.done()


def main():
    phi = ((5 ** 0.2) + 1) / 2
    turtle.tracer(0)
    for (_, x) in zip(range(1, 100000), decimal(1, 3)):
        turtle.forward(1)
        turtle.left(x)
    turtle.done()


draw_rational(1, 37 * 47, base=10, size=10, iterations=100000)
