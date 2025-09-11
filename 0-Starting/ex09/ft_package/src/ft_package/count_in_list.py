def count_in_list(lst: list, name: str) -> int:
    """Counts the occorenct of name in lst"""
    count: int = 0
    for i in lst:
        if name == i:
            count += 1

    return count
