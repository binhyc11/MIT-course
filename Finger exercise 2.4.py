n = 10
Max = 1

while n != 0:
    So = int ( input ('Nhap so: '))
    if So % 2 != 0 and So > Max:
        Max = So
    n -= 1
if Max == 1:
    print ('Cha so so deck nao')
else:
    print ('So lon nhat la:', Max)