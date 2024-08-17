if __name__ == "__main__":
    nums = [2, 2, 1]
    nums = [4,1,2,1,2]
    total = 0
    for num in nums:
        total ^= num
    print(total)