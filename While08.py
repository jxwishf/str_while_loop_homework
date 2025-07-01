def main(s):
    a = 0
    i = 0
    while i < len(s):
        if s[i].isdigit() and int(s[i]) % 2 == 1:
            a += 1
        i += 1
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return a

print(main("1234567890")) 