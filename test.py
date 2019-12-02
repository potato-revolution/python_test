import linecache

with open("input.txt", "r") as f:
    data = f.read()
    print(data)
    #i, sをどうやって分割して取り込むのかが分からない。
    m = linecache.getline('input.txt', 54)
    print(m)

"""
辞書型に格納する場合
for (i, s) in zip(get_dic.keys(), get_dic.values()):
    if m % i == 0:
        print(s)
    else:
        print(m)
"""
