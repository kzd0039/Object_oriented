from abc import ABCMeta, abstractmethod

class employee(object, metaclass=ABCMeta):

    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class manager(employee):
        
    def get_salary(self):
        return 15000
    
class programmer(employee):
    def __init__(self,name,hour=0):
        super().__init__(name)
        self._hour=hour

    @property
    def hour(self):
        return self._hour  
    
    @hour.setter
    def hour(self,hour):
        self._hour=hour if hour>0 else 0
    
    def get_salary(self):
        return self._hour*150

class seller(employee):
    def __init__(self,name,sellamount=0):
        super().__init__(name)
        self._sellamount=sellamount
    
    @property
    def sellamount(self):
        return self._sellamount

    @sellamount.setter
    def sellamount(self,sellamount):
        self._sellamount=sellamount if sellamount>0 else 0

    def get_salary(self):
        return 1200+self._sellamount*0.05

def main():
    example=[manager('eva'),programmer('Kun ding'),seller('shadiao')]
    for ele in example:
        if isinstance(ele,programmer):
            ele._hour=int(input('请输入%s工作时间：'%ele._name))
        if isinstance(ele,seller):
            ele._sellamount=int(input('请输入%s销售额：'%ele._name))
        print('%s每月月薪为$%d'%(ele._name,ele.get_salary()))

 
if __name__=='__main__':
    main()