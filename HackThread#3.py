
def swap_case(s):
    b = ""
    for i in s:
        if i == i.upper():
            b += i.lower()
        else:
            b += i.upper()        
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)