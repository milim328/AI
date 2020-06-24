class readList:
    def __init__(self):
        self.student_number_list = []
        self.name_list = []
        self.kor_list = []
        self.eng_list = []
        self.math_list = []
        self.total_list = []
        self.avg_list = []
        self.haksjum_list = []

    def getScore(self):
        flag = True
        print("프로그램을 종료하려면 학번에 0을 입력하세요.")
        while flag:
            student_number = input("학번을 입력하세요 : ")
            if student_number == '0':
                flag = False
            else:
                name = input("이름을 입력하세요 : ")
                kor = int(input("국어점수를 입력하세요 : "))
                eng = int(input("영어점수를 입력하세요 : "))
                math = int(input("수학점수를 입력하세요 : "))
                print("-"*50)

                self.student_number_list.append(student_number)
                self.name_list.append(name)
                self.kor_list.append(kor)
                self.eng_list.append(eng)
                self.math_list.append(math)
        self.calList()

    def calList(self):
        for i in range(len(self.student_number_list)):
            total = self.kor_list[i] + self.eng_list[i] + self.math_list[i]
            avg = total/3.0
            self.total_list.append(total)
            self.avg_list.append(avg)

            if avg >= 90:
                grade = 'A'
            elif avg >= 80:
                grade = 'B'
            elif avg >= 70:
                grade = 'C'
            elif avg >= 60:
                grade = 'D'
            else:
                grade = 'F'
            self.haksjum_list.append(grade)
        return self.total_list, self.avg_list, self.haksjum_list

class printLi(readList):
    def printList(self):
        print("="*70)
        print("번호\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t\t학점")
        print("=" * 70)
        for i in range(len(self.student_number_list)):
            print("%3s\t\t%5s\t%3d\t\t%3d\t\t%3d\t\t%3d\t\t%.2f\t\t%s"%(self.student_number_list[i], self.name_list[i], self.kor_list[i], self.eng_list[i], self.math_list[i],
                                                                      self.total_list[i], self.avg_list[i], self.haksjum_list[i]))

if __name__ == "__main__":
    result = printLi()
    result.getScore()
    result.printList()