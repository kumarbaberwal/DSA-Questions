# The Leetcode file system keeps a log each time some user performs a change folder operation.

# The operations are described below:

# "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
# "./" : Remain in the same folder.
# "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

# The file system starts in the main folder, then the operations in logs are performed.

# Return the minimum number of operations needed to go back to the main folder after the change folder operations.


def minOperations(logs: list[str]) -> int:
    operations = 0
    for folder in logs:
        if '../' in folder:
            operations -= 1 if operations > 0 else 0
        elif './' in folder:
            continue
        elif '/' in folder:
            operations += 1

    return operations

if __name__ == "__main__":
    # logs = ["d1/","d2/","../","d21/","./"]
    # logs = ["d1/","d2/","./","d3/","../","d31/"]
    logs = ["d1/","../","../","../"]
    print(f"The Minimun Operations is : {minOperations(logs)}")