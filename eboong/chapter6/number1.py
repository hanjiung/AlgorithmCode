#위에서 아래로
num = int(input())
array = [int(input()) for i in range(num)]
array=sorted(array,reverse=True)

for i in array:
    print(i,end=' ')