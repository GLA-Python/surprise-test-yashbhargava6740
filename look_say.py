def look_say(n):
    st = ''
    if n > 1:
        x = 1
        print(x)
        for i in range(1, n):
            o = ''
            while x > 0:
                y = x % 10
                c = 1
                x = x // 10
                while x > 0:
                    if x % 10 == y:
                        c += 1
                        x = x // 10
                    else:
                        break
                o = str(c) + str(y) + str(o) 
            st += o +'\n'
            x = int(o)
    return st
print(look_say(int(input()))[-1])
