if __name__ == '__main__':
    N = int(input())
    
    containerList = []

    for i in range(N):

        inputList = input().split(" ")

        if inputList[0] == "insert":
            containerList.insert(int(inputList[1]),int(inputList[2]))

        elif inputList[0] == "print":
            print(containerList)

        elif inputList[0] == "remove":
            containerList.remove(int(inputList[1]))

        elif inputList[0] == "append":
            containerList.append(int(inputList[1]))

        elif inputList[0] == "sort":
            containerList.sort()

        elif inputList[0] == "pop":
            containerList.pop()

        elif inputList[0] == "reverse":
            containerList.reverse()
        else:
            pass