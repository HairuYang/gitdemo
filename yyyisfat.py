for i in range(1, 10):
        for j in range(1, i+1):
            print("%d*%d=%d\t" % (j, i, i*j), end="")
        print()

#斐波那契数列  0，1，1，2，3，5，8,...
num=int(input("需要几项？"))
n1=0
n2=1
count=2
if num<=0:
    print("请输入一个整数。")
elif num==1:
    print("斐波那契数列:")
    print(n1)
elif num==2:
    print("斐波那契数列:")
    print(n1,",",n2)
else:
    print("斐波那契数列:")
    print(n1,",",n2,end=" , ")
    while count<num:
        sum=n1+n2
        print(sum,end=" , ")
        n1=n2
        n2=sum
        count+=1
print()
