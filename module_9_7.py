def is_prime(sum_three):
    def wrapper(*args):
        res = sum_three(*args)
        if res < 2:
            print("Составное")
        else:
            for i in range(2, int(res ** 0.5) + 1):
                if res % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return res
    return wrapper

@is_prime
def sum_three(*args):
    res = sum([*args])
    return res

result = sum_three(2, 3, 6)
print(result)