if __name__ == "__main__":
    s = ['k','u','m','a','r']
    n = len(s)
    for i in range(n//2):
        s[i], s[n - i - 1] = s[n - i - 1], s[i]

    print(s)