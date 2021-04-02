



print("nhap vao day so nguyen: ")
so = int(input()) 
sapxep = []
while (so != 0):
    sodu = so % 2
    sapxep.append(sodu)
    so=so//2
print(sapxep)
b= ''
while (sapxep != []):
    b=b+str(sapxep.pop())
print('số nhị phân của dãy số là: ', b)
    
    
