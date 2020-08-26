if __name__ == '__main__':
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append([name,score])
         
marks = sorted(marks, key = lambda x: x[0])
marks = sorted(marks, key = lambda x:x[1])

secondMark = sorted(list(set([b for a, b in marks])))[1]

for i,j in marks:
    if j == secondMark:
        print(i)
        
        