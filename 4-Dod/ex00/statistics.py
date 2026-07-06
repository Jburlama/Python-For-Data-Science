"""
* passa todos os agumentos para uma tupla "soltos"
** agrupa todos os argumentos nomeados para um dicionario
"""


def get_mean(args: tuple) -> float:
    """gets the mean from a tuple"""
    mean = 0
    for i in args:
        mean += i
    return mean / len(args)


def get_median(args: tuple) -> float:
    """gets the median from a tuple"""
    sorted_list = sorted(args)
    n = len(sorted_list)

    if len(sorted_list) % 2:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2] + sorted_list[n // 2 - 1]) / 2

    return median


def get_variance(args: tuple) -> float:
    """
    Gets the varience from a tuple
    It calculates the median distance from each value and the median (square to
    not have negative numbers)
    """
    mean = get_mean(args)
    dist_from_mean = [pow(mean - i, 2) for i in args]
    var = 0
    for i in dist_from_mean:
        var += i
    return var / len(args)


def get_std(args: tuple) -> float:
    """
    Gets the standar deviation, which is the square root of the variance,
    We make the square root because we squared the variance
    """
    return get_variance(args) ** 0.5


def get_quartile(args: tuple) -> list:
    """
    Gets the 1st and 3rd quartiles from a tuple.
    Returns them as a list: [Q1, Q3].
    """
    sorted_list = sorted(args)
    n = len(sorted_list)
    mid = n // 2

    if len(sorted_list) % 2 != 0:
        lower_half = sorted_list[:mid]
        upper_half = sorted_list[mid + 1:]
    else:
        lower_half = sorted_list[:mid]
        upper_half = sorted_list[mid:]

    return [float(lower_half[-1]), float(upper_half[0])]


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
        stats["mean"] = get_mean(args)
        stats["median"] = get_median(args)
        stats["var"] = get_variance(args)
        stats["std"] = get_std(args)
        stats["quartile"] = get_quartile(args)

        for i in kwargs:
            if kwargs[i] in stats:
                print(f"{kwargs[i]}: {stats[kwargs[i]]}")

    except ZeroDivisionError:
        for i in kwargs:
            if kwargs[i] in stats:
                print("ERROR")
