a=0
def main(a):
    if a>0:
        return a+1
    if a<0:
        return a-2
    if a==0:
        return 10
    """
    If the number is positive, increase it to 1,if the number is negative decrease it to 2.
    If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    return a
print(main(a))