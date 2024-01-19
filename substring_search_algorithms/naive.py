def naive_search(text: str, pattern: str) -> int:
    n = len(text)
    m = len(pattern)

    if m == 0 or n == 0 or m > n:
        return -1
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1
