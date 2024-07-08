def fizzBuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                result.append('fizzbuzz')
            else:
                result.append('fizz')
        elif i % 5 == 0:
            result.append('buzz')
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    print(fizzBuzz(3))
    print(fizzBuzz(5))