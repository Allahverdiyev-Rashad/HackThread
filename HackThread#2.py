
N = int(input("Sayı daxil edin: "))

a = list(map(int, input("Array ədədini daxil edin: ").rstrip().split()))

a = a[::-1]

print(*a)
