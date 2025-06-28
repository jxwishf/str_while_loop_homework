def main(s):
    a = 0
    i = 0
    while i < len(s):
        if s[i].isupper():
            a += 1
        i += 1
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return a
print(main("python %^&^%$ 2022"))