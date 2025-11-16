def search_divisors(number: int) -> list:
    '''
    The function get a number and find all divisors of a given number.
    
    Args:
        int: The number for which divisors are being searched
    
    Returns:
        list: List of all divisors of the number
    '''
    divisors = set()
    
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    
    return sorted(list(divisors))


def main():
    num = int(input())
    divisors = search_divisors(num)
    print(divisors)


if __name__ == '__main__':
    main()