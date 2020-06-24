num = input("번호")
korean = int(input("국어 점수:"))
english = int(input("영어 점수:"))
math = int(input("수학 점수:"))
physics = int(input("물리 점수:"))
s = korean + english + math + physics
count = 4
avg = s / 4

print ('----번호----국어----영어----수학----물리----총점----평균')
print ('----',num,'----',korean,'----',english,'----',math,'----',physics,'----',s,'----',avg)
if avg >= 90:
    print("학점: A")

elif avg >= 80:
    print("학점 : B")

elif avg >= 70:
    print("학점 : C")

elif avg >= 60:
    print("학점 : D")

else:
    print("학점 : F")


