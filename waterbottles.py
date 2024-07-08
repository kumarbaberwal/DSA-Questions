def numWaterBottles(numBottles: int, numExchange: int) -> int:
    return numbottles + (numbottles - 1)//(numexchange - 1)

def numWaterBottles2(numBottles: int, numExchange: int) -> int:
    total_drunk = numbottles
    empty_bottles = numbottles

    while empty_bottles >= numexchange:
        new_bottles = empty_bottles // numexchange
        total_drunk += new_bottles
        empty_bottles = (empty_bottles % numexchange) + new_bottles

    return total_drunk

if __name__ == '__main__':
    numbottles, numexchange = 15, 4
    print(numWaterBottles(numbottles, numexchange))
    print()
    print(numWaterBottles2(numbottles, numexchange))