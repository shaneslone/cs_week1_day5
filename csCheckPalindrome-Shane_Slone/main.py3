def csCheckPalindrome(input_str):
    p1 = 0
    p2 = len(input_str) - 1
    while (p1 < p2):
        if input_str[p1] != input_str[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

