import big_o


def estimate_big_o(func, generator, **kwargs):
    """
    Integers:
        generator = lambda n: big_o.datagen.integers(n, 0, 10000)
    List integers:
        generator = lambda n: big_o.datagen.range_n(n, 1)
    """
    best, others = big_o.big_o(func, generator, **kwargs)
    print(best)
