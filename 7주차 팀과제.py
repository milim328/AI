class Score:
    def __init__(self, hakbun, name, kor, eng, math):
        self.hakbun = hakbun
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

class Readlist:           
    def readList(self):
        hakbunlist = []
        namelist = [] 
        korlist = []
        englist = []
        mathlist = []
    
        flag = True
        print("프로그램을 종료하려면 학번에 0을 입력하시오.")
        while flag:
            self.hakbun = input("학번을 입력하시오: ")
            if self.hakbun == '0':
                flag = False
            else : 
                self.name = input("이름을 입력하시오: ")
                self.kor = int(input("국어 점수를 입력하시오: "))
                self.eng = int(input("영어 점수를 입력하시오: "))
                self.math = int(input("수학 점수를 입력하시오: "))

                hakbunlist.append(hakbun)
                namelist.append(name)
                korlist.append(kor)
                englist.append(eng)
                mathlist.append(math)
        
        return hakbunlist, namelist, korlist, englist, mathlist

class Callist:
    def calList(self,total,avglis,haksjum):
        totalist =[]
        avglist= []
        haksjumlist = []
        self.total = 0 
        self.avg = 0.0
        for i in range(len(korlist)):
            self.total= korlist[i] + englist[i] + mathlist[i]
            self.avg = self.total / 3.0
            totalist.append(total)
            avglist.append(avg)
 
            if self.avg >= 90:
                grade = 'A'
            elif self.avg >= 80:
                grade = 'B'
            elif self.avg >= 70:
                grade = 'C'
            elif self.avg >= 60:
                grade = 'D'
            else:
                grade = 'F'
            haksjumlist.append(grade)
        return totalist,avglist,haksjumlist

class Printlist:
    def printList():
        print("="*70)
        print(" 번호 \t\t이름\t국어\t영어\t수학\t총점\t평균\t학점")
        for i in range(len(hakbunlist)):
            print("%3s\t%5s\t%3d\t\t%3d\t\t%3d\t\t%3d\t\t%.2f\t\t%s"%(hakbunlist[i],namelist[i],\
                korlist[i],englist[i],mathlist[i],totalist[i],avglist[i],haksjumlist[i]))

class Main:           
    def main(self):
         hakbunlist,namelist,korlist,englist,mathlist = self.Readlist()
         totalist,avglist,haksjumlist = Callist(korlist, englist, mathlist)
         Printlist(hakbunlist,namelist,korlist,englist,mathlist,totalist,avglist,haksjumlist)

    if __name__ == "__main__":
        main()


#학생 성적 관리 class 작성하기
#- attribute: 국어, 영어, 수학, ...등의 속성
#- 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정
#- 각 속성은 private 으로 설정
#- method: 전체 과목 점수 평균, 전체 과목 총점 두 가지 method 구현
#- 각 method 는 private 으로 설정