for i in range(1, 10):
        for j in range(1, i+1):
            print("%d*%d=%d\t" % (j, i, i*j), end="")
        print()
