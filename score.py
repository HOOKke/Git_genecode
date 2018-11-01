import sys
from itertools import islice
path = "SavageJansen_2018_intelligence_metaanalysis.txt"  # 数据来源
#path ="test.txt"
f = open(path)
list = []
line = f.readline()
for line in islice(f, 0, None):
    a = line.split()
    i = float(a[8])
    if i < 0:
        i = abs(i)
        b = a[0] + ' ' + a[5] + ' ' + str(i)
    else:
        b = a[0] + ' ' + a[4] + ' ' + str(i)
    list.append(b)
f.close


with open('score.txt', 'a') as out_file:  # 提取后的数据文件
#with open('test1.txt', 'a') as out_file:  # 提取后的数据文件
    out_file.write('snp reference score\n')
    for tag in list:
        for j in tag:
            out_file.write(str(j))
        out_file.write('\n')

