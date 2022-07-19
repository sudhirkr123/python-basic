#f=open('D:\\test1.txt','a')
#f.write('tea coffce milk butter sprite bread')
#f=open('D:\\test2.txt','a')
#f.write('milk bread tea water apple')
f=open('D:\\test1.txt','r')
m1=f.readlines()
f=open('D:\\test1.txt','r')
m2=f.readlines()
print(m1)
print(m2)
m3=[]
for i in range(0,len(m1)):
    if m1[i]==m2:
        m3=m1[i]
        print(m3)



