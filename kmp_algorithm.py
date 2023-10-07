def compute_lps(pattern):
    lps = [0] * len(pattern)
    j = 0  # Length of the previous longest prefix suffix

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        lps[i] = j

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0  # Index for text[]
    j = 0  # Index for pattern[]
    flag = False

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
            flag = True

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if (flag == False):
        print("Pattern not found!")


# Example usage:
text = "I am a computer science under graduate"
pattern = "computer s"
kmp_search(text, pattern)
