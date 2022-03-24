class Student:
    def __init__(self,name,conf):
        self.name = name
        self.lab_max = conf['lab_max']
        self.lab_num = conf['lab_num']
        self.lab = [0] * self.lab_num
   
    def set_lab(self,score,number = None):
        self.score = score
        self.number = number
        if number == None:
            if not 0 in self.lab:
                print('error')
            else:
                for i in range(len(self.lab)):
                    if self.lab[i] == 0:
                        self.lab[i] = score
                        break
        else:
            if number > len(self.lab):
                print('error')
            elif score > self.lab_max:
                self.lab[number] = self.lab_max
            else:
                self.lab[number] = self.score
    
    #для проверки s и др значений
    '''def average(self):
        s = 0
        for i in self.lab:
            s += i
        s /= len(self.lab)
        print(s)
        return(round(s,1))'''
    def average(self):
        return (round(sum(self.lab) / self.lab_num,1))
 
#test_part       
'''ivan = Student("Ivan", {"lab_max": 5, "lab_num": 4})
print(ivan.name)
print(ivan.lab)
ivan.set_lab(4, 1)
print(ivan.lab)
ivan.set_lab(5)
print(ivan.lab)
print(ivan.average())
ivan.set_lab(5, 6) 
ivan.set_lab(8, 2)
print(ivan.lab)
ivan.set_lab(3)
print(ivan.lab)
ivan.set_lab(5) 
print(ivan.average())'''