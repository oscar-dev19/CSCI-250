def isLucky(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n/10
    return sum == 1


def luckySum(n):
    sum = 0
    number ="%d"%n
    for i in number:
        temp = int(i)
        sum += temp
    return sum

def isLucky2(n):
    lucky_nums = list()
    while n > 0:
        n = luckySum(n)
        if n == 1: 
            return True
        elif n in lucky_nums:
            return False
        else:
            lucky_nums.append(n)


print(isLucky(19))
print(isLucky(5))
print(isLucky(3))
print(isLucky(10))
