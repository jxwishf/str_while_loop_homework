def main(s):
    a = 0
    i = 0
    while i < len(s):
        if s[i].isdigit() and int(s[i]) % 2 == 1:
            a += int(s[i])
        i += 1
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return a

print(main("123abc456")) 
