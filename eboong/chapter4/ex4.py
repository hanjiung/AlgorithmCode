# # 게임 개발 118p

n, m = map(int, input().split())
x, y, d = map(int, input().split())
map_list = [list(map(int, input().split())) for i in range(n)]
result_list = [[0] * m for _ in range(n)]  # 들렀던 곳인지 확인하는 테스트
result_list[x][y]=1

dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]  # 북동남서

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
rotate_time = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if result_list[nx][ny] == 0 and map_list[nx][ny] == 0:
        result_list[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        rotate_time = 0
        continue
    else:
        rotate_time += 1
    if rotate_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        rotate_time = 0
print(cnt)





# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# result_list = [[0] * n for i in range(n)]  # 들렀던 곳인지 확인하는 테스트
# map_list = [list(map(int, input().split())) for i in range(n)]
# d[x][y] = 1  # 방문처리하기
#
# dx = [-1, 0, 1, 0]  # 북동남서
# dy = [0, 1, 0, -1]  # 북동남서
#
#
# def tunr_left():
#     global d
#     d -= 1
#     if d == -1:  # 0은 북쪽,1은 서쪽, 2는 남, 3은 동쪽
#         d = 3

# if map_list[next_row][next_row] != 1:  # 왼쪽
#     d = 1
#     cnt += 1
#     y -= 1
#     result_list[next_row][next_col] = 1
#
# elif map_list[next_row][next_col] != 1:  # 아래
#     d = 2
#     cnt+=1
#     x+=1
#     result_list[next_row][next_col] = 1
#     print("3c")
#
# elif map_list[next_row][next_col] != 1:  # 오른쪽
#     d = 3
#     cnt += 1
#     y += 1
#     result_list[next_row][next_col] = 1
#     print("4d")
#
# elif map_list[next_row][next_col] != 1:  # 위
#     d = 0
#     cnt += 1
#     x -= 1
#     result_list[next_row][next_col] = 1
#     print("1a")
