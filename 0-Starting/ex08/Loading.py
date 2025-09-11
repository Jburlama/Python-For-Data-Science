import os


def progress_bar(iteration: int, total: int, bar_len: int = 50) -> str:
    """Returs the progress bar string,
    accordently to the numbers of iteration over the total amount"""
    progress = iteration / total
    iterations_string = f"{iteration}/{total}"
    bar_len -= len(iterations_string)
    filled_length = int(bar_len * progress)
    bar = "█" * filled_length + " " * (bar_len - filled_length)

    return f"|{bar}| {iterations_string} "


def format_time(seconds: int) -> str:
    """Format seconds into MM:SS"""
    minutes, seconds = divmod(seconds, 60)

    return f"{minutes:02d}:{seconds:02d}"


def ETA(elapse: int, total: int, completed: int) -> str:
    """ETA (Estimated Time of Arrival)
    ETA = (Total items - Completed items) × Average time per item
    """
    running_time = format_time(elapse)

    if (completed > 0):
        rate = elapse / completed
    else:
        rate = 0

    if completed == 0:
        eta = "?"
    else:
        eta_time = (total - completed) * rate
        minutes, seconds = divmod(eta_time, 60)
        minutes = int(minutes)
        seconds = int(seconds)
        eta = f"{minutes:02d}:{seconds:02d}"

    if rate >= 1:
        return f"[{running_time}<{eta},  {rate:.2f}s/it]"
    elif rate == 0:
        return f"[{running_time}<{eta}, ?it/s]"
    else:
        return f"[{running_time}<{eta}, {1/rate:.2f}it/s]"


def ft_tqdm(lst: range) -> None:
    """Display a progress over the task to complete,
    and the estimate time of completion
            """
    bar_len = os.get_terminal_size().columns
    total_items = len(lst)
    start_time = os.times()[4]

    for i in range(total_items + 1):
        current = os.times()[4]
        elapse = int(current - start_time)
        p = i/(len(lst))
        eta_str = ETA(elapse, total_items, i)
        print(f"{p:.0%}", end="")
        print(progress_bar(i, total_items, bar_len - len(eta_str) - 8), end="")
        print(eta_str, end="")
        print(end="\r")
        yield

    return None
