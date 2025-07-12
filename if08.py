a=-319
def main(a):
    if abs(a)//10>0 and abs(a)//10<10 and a%2==1:
        return "two-digit odd number"
    if abs(a)//10>0 and abs(a)//10<10 and a%2==0:
        return "two-digit even number"
    if abs(a)//100>0 and abs(a)//100<10 and a%2==1:
        return "three-digit odd number"
    if abs(a)//100>0 and abs(a)//100<10 and a%2==0:
        return "three-digit even number"
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    return a
print (main(a)) 