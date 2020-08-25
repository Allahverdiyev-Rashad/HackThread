if __name__ == '__main__':
    
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    def multiple(x):
        a = 0
        for i in x:
            a += i
        return a/3

    print("{0:.2f}".format(multiple(student_marks[query_name])))
