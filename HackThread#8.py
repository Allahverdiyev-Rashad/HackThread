if __name__ == '__main__':
    s = input()
    a = []
    b = []
    c = []
    d = []
    e = []
    

    for i in s:
        if i.isalnum() == True:
            a.append(True)
        if i.isalpha() == True:
            b.append(True)
        if i.isdigit() == True:
            c.append(True)
        if i.islower() == True:
            d.append(True)
        if i.isupper() == True:
            e.append(True)

    print(any(a),any(b),any(c),any(d),any(e),sep = "\n")