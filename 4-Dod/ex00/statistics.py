"""
* passa todos os agumentos para uma tupla "soltos"
** agrupa todos os argumentos nomeados para um dicionario
"""


def ft_statistics(*args: any, **kwargs: any) -> None:
    """statistic function that given a tuple of numbers, can print
        the mean, the median, the quartile, thd standar deviation and the
        variance"""
    stats = {
        "mean": 0,
        "median": None,
        "quartile": None,
        "std": None,
        "var": None,
    }

    try:
        for i in args:
            stats["mean"] += i
        stats["mean"] = stats["mean"] / len(args)
        stats["median"] = args[int(len(args) / 2) - 1]
        sort = sorted(args)
        stats["quartile"] = (sort[int(len(sort) / 4)] * 1.0,
                             sort[int(len(sort) / 1.3)] * 1.0)

        # A variancia é a diferença entre o valor e a media, elevado ao
        # quadrado para não ter numeros negativos
        dist_from_mean = [pow(stats["mean"] - i, 2) for i in args]
        var = 0
        for i in dist_from_mean:
            var += i
        var /= len(args)
        stats["var"] = var

        # Desvio padrão é a raiz quadrada da variancia
        std = var ** 0.5
        stats["std"] = std

        for i in kwargs:
            if kwargs[i] in stats:
                print(f"{kwargs[i]}: {stats[kwargs[i]]}")

    except ZeroDivisionError:
        for i in kwargs:
            if kwargs[i] in stats:
                print("ERROR")
