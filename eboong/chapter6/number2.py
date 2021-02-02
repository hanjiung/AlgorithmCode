# 성적이 낮은 순서로 학생 출력하기
num = int(input())
student_list = []
for i in range(num):
    input_data = input().split()
    student_list.append([input_data[0], int(input_data[1])])

student_list = sorted(student_list, key=lambda student: student[1])

for i, j in student_list:
    print(i, end=' ')
    
# key는 정렬 기준을 정해주는 역할을 한다.
