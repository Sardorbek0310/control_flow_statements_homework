a=3
def main(a):
    if a>0:
        return a+1
    if a<=0:
        return a-2

    """
    If the number is positive, increase it to 1,otherwise decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    """
    return a
print(main(a))