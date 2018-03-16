for i in range(1000,2000):
        Write = open(str(i)+".xml",'w')
        Read = open("0.xml",'r')
        # 0.xml is actually 1000.xml from the default directory
        for j in Read.readlines():
                Write.write(j.replace("1000",str(i)))
        Write.close()
