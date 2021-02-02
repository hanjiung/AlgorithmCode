# 예제 4-1 상하좌우 문제
num = int(input())
a_list = input().split() # 리스트 형태로 받아들임
n_list = [[0] * num for i in range(num)]
print(n_list)
cnt = 0

for i in range(num):
    if cnt <= len(a_list):
        for j in range(num):
            if a_list[i] == 'R':
                if j == num - 1:
                    break
                cnt += 1
            elif a_list[i] == 'U':
                if i == 0:
                    break
                cnt += 1
            elif a_list[i] == 'D':
                if i == num - 1:
                    break
                cnt += 1
            elif a_list[i] == 'L':
                if j == 0:
                    break
                cnt += 1
    else:
        print(i+1, j)
        break

# 책 소스코드
# n = int(input())  # 배열 크기
# x, y = 1, 1 #배열 시작이 1,1부터
# plans = input().split() #이동 경로 입력받기
#
# dx = [0, 0, -1, 1] #왼쪽,오른쪽
# dy = [-1, 1, 0, 0] #아래,위
#
# move_types = ['L', 'R', 'U', 'D']
#
# for plan in plans: # 받아온 이동 경로 개수
#     for i in range(len(move_types)): # R,U,L,D 총 4
#         if plan == move_types[i]:
#             nx = x + dy[i]
#             ny = y + dy[i]
#     # 공간을 벗어날 경우 수행되는 IF문
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#
#     x, y = nx, ny
# print(x, y)
