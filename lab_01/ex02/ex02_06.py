input_str1,input_str2=input("nhap X,y: ").split(" ")
listfinal =[]
for i in range(int(input_str1)):
    multilist = [i*j for j in range(int(input_str2))]
    listfinal.append(multilist)
print(listfinal)