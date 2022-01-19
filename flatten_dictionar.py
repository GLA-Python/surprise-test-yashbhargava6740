inp = eval(input())    # {"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}}
st1 = '{'
out = list(inp.items())
x = 0
t = 0
ind = []
for i in out:
    c = 0
    st = ''
    for j in i:
        if type(j) != dict:
            c = 1
            st += str(j)
        else:
            c = 0
            for k in str(j):
                x += 1
                if k.isalpha():
                    st += k
                elif k.isdigit():
                    st8 = ''
                    if str(j).index(k) not in ind:
                        ind.append(str(j).index(k))
                        for z in range(str(j).index(k),len(str(j))):
                            if str(j)[z].isdigit():
                                st8 += str(j)[z]
                                ind.append(z)
                            else:
                                break
                        st += '\"' + ':' + st8
                    else:
                        pass
                elif k == '{':
                    st += '.'
                elif k == ',': 
                    st += ',' + ('\"'+str(i[0])) + '.'
            st1 += '\"' + st
    if c == 1:
        st1 += '\"' + str(i[0]) + '\"' + ':' + str(i[1])+ ','
st1 += '}'
print(eval(st1))

#output : {'key': 3, 'foo.a': 5, 'foo.bar.baz': 8}