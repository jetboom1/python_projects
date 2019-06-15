'''Возникли проблемы с получением доступа к файлу через интернет, поэтому пришлось скачать его локально'''
from operator import itemgetter
with open('intro.txt') as romeo:
    counts = dict()
    for i in romeo.readlines():
        words = i.lower().split()
        for k in words:
            if k in counts:
                counts[k]+=1
            else:
                counts[k]=1
counts = sorted(counts.items(), key=itemgetter(1), reverse=True)
for k in range(len(counts)):
    for i in range(len(counts[k])):
        print(counts[k][i], end=' ')
    print()