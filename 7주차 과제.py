
class Score:
    def __init__(self, hakbunlist, namelist, korlist, englist, mathlist):
        self.hakbunlist = hakbunlist
        self.namelist = namelist
        self.korlist = korlist
        self.englist = englist
        self.mathlist = mathlist

        

  
    def readList(self):
        
    
        flag = True
        print("프로그램을 종료하려면 학번에 0을 입력하시오.")
        while flag:
            hakbun = input("학번을 입력하시오: ")
            if hakbun == '0':
                flag = False
            else : 
                name = input("이름을 입력하시오: ")
                kor = int(input("국어 점수를 입력하시오: "))
                eng = int(input("영어 점수를 입력하시오: "))
                math = int(input("수학 점수를 입력하시오: "))

                self.hakbunlist.append(hakbun)
                self.namelist.append(name)
                self.korlist.append(kor)
                self.englist.append(eng)
                self.mathlist.append(math)
        self.calList()
        return hakbunlist, namelist, korlist, englist, mathlist

class Callist():
    def calList(self,totalist,avglist,haksjumlist):
        self.totalist = totalist
        self.avglist = avglist
        self.haksjumlist = haksjumlist
        self.totalist =[]
        self.avglist= []
        self.haksjumlist = []
        total = 0 
        avg = 0.0
        for i in range(len(korlist)):
            total= self.korlist[i] + self.englist[i] + self.mathlist[i]
            avg = total / 3.0
            self.totalist.append(total)
            self.avglist.append(avg)

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
            self.haksjumlist.append(grade)
        return totalist,avglist,haksjumlist

class Printlist (Readlist):
    def printList(self):
        print("="*70)
        print(" 번호 \t\t이름\t국어\t영어\t수학\t총점\t평균\t학점")
        for i in range(len(self.hakbunlist)):
            print("%3s\t%5s\t%3d\t\t%3d\t\t%3d\t\t%3d\t\t%.2f\t\t%s"%(self.hakbunlist[i],self.namelist[i],\
                self.korlist[i],self.englist[i],self.mathlist[i],self.totalist[i],self.avglist[i],haksjumlist[i]))



if __name__ == "__main__":
    #객체 만들기
    객체 클래스
    
  


