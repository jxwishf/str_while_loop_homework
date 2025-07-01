def main(s):
    a = 0
    i = 0
    vowels = "aeiouAEIOU"
    while i < len(s):
        if s[i].isalpha() and s[i] not in vowels:
            a += 1
        i += 1
    """
    A variable of type str is given. Find how many consonant letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return a

print(main("python %^&^%$ 2022"))  # Output: 5 (p, y, t, h, n)
