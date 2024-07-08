def findTheWineer(n: int, k: int) -> int:
    queue = []
    for i in range(1, n+1):
        queue.append(i)
    while len(queue)>=k:
        i = 0
        while i < k-1:
            queue.append(queue.pop(0))
            i +=1
        queue.pop(0)
    return queue.pop(0)

def findTheWinner(n: int, k: int) -> int:
    def recursion(n: int, k: int) -> int:
        if n == 1:
            return 0
        return (recursion(n-1, k) + k) % n
    return recursion(n, k) + 1

if __name__ == "__main__":
    print(f"The Winner is : {findTheWineer(5, 2)}")
    print(f"The Winner is : {findTheWinner(5, 2)}")