if __name__ == '__main__':
    N = int(input())
    output=[];
    for i in range(0,N):
        cmd=input().split();
        if cmd[0] == "insert":
            output.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            output.append(int(cmd[1]))
        elif cmd[0] == "pop":
            output.pop();
        elif cmd[0] == "print":
            print(output)
        elif cmd[0] == "remove":
            output.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            output.sort();
        else:
            output.reverse();
