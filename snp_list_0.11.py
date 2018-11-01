from itertools import islice
path = "SavageJansen_2018_intelligence_metaanalysis.txt"  # 数据来源
#path ="test.txt"
f = open(path)
list = []
line = f.readline()
for line in islice(f, 0, None):
    a = line.split()
    b = float(a[10])
    if b<0.11:
        c = a[0]
        list.append(c)
f.close
#print(list)

with open('snp_list_0.11.txt', 'a') as out_file:  # 提取后的数据文件
#with open('test1.txt', 'a') as out_file:  # 提取后的数据文件
    out_file.write('snp\n')
    for tag in list:
        for i in tag:
            out_file.write(str(i))
        out_file.write('\n')
