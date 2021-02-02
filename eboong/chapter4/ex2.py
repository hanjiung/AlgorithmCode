## 예제 4-2 시각문제
n = int(input())
cnt = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)

# 초,분,시 숫자를 문자열로 합친 후 3이 있을 때마다 cnt+=1