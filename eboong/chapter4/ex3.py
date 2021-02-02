# 왕실의 나이트
col = input()
col_row = list(col)

map_list = [[0] * 8 for i in range(8)]  # 맵 배열 만들기
col_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 열 문자->숫자로 바꿔서 저장
col_num = 0  # 열번호
row_num = int(col_row[1])-1  # 행번호

for i in range(8):
    if col_row[0] == col_list[i]:
        col_num = i
        break
cnt = 0  # 총 횟수 구하기

while row_num - 2 >= 0:  # 위로 가기 통과
    if row_num - 2 >= 0 and col_num - 1 >= 0:
        cnt += 1

    if row_num - 2 <= 7 and col_num + 1 <= 7:
        cnt += 1
        break

while col_num + 2 <= 7:  # 오른쪽 가기 통과
    if row_num - 1 >= 0:
        cnt += 1

    if row_num + 1 <= 7:
        cnt += 1
        break

while row_num + 2 <= 7:  # 아래쪽
    if col_num - 1 >= 0:
        cnt += 1

    if col_num + 1 <= 7:
        cnt += 1
        break

while col_num - 2 >= 0:  # 왼쪽
    if row_num - 1 >= 0:
        cnt += 1

    if row_num + 1 <= 7:
        cnt += 1
        break

print(cnt)

# ---------------------책풀이-------------------------
# # 현재 나이트의 위치 입력받기
# input_data=input()
# row=int(input_data[1]) #a1에서 1을 row 변수에 저장
# col=int(ord(input_data[0]))-int(ord('a'))+1
# # 입력값이 c2이면, c의 아스키값-a의 아스키값+1
# # ord()는 아스키 코드 값을 돌려주는 함수값이다.
#
# #나이트가 이동할 수 있는 8가지 방향 정의하기
# steps=[(-2,-1),(-2,1),(-1,-2),(1,-2),(-2,-1),(-2,1),(-1,-2),(1,-2)] #위,오른쪽,아래,왼쪽순으로
#
# #각 위치로 이동 가능한 지 확인
# result=0
# for step in steps:
#     next_row=row+step[0]
#     next_col=col+step[1]
#     if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
#         result+=1
# print(result)