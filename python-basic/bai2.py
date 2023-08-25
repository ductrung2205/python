def peramutation(head, tail=""):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            peramutation(head[0:i] + head[i + 1:], tail + head[i])
list_one = ['a','b','c','d']
perm_list_one = peramutation(list_one)