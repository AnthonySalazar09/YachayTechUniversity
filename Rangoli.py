ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def print_rangoli(size):
    leters = ALPHABET[:size]
    res = []
    for i in range(size):
        cur_letters = leters[size-1-i:]
        cur_letters = '-'.join(list(cur_letters[::-1][:-1] + cur_letters))
        amount = ( 4 * size - 3 - len(cur_letters))//2
        res.append("-"*amount+cur_letters+"-"*amount)
    print('\n'.join(res + res[::-1][1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
