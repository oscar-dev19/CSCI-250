fib_dict = dict()

def alt_fib(n, a_dict):
    if n <= 2 and n >= 1:
        return 1
    else:
        if n in a_dict:
            return a_dict[n]
        return alt_fib(n-1, a_dict) + alt_fib(n-2, a_dict)


print(alt_fib(5, fib_dict))
