from time import sleep

class clock:
    def __init__(self,hour,minute,second):
        self._hour=hour
        self._min=minute
        self._second=second
    
    def run(self):
        if self._second<59:
            self._second+=1
        else:
            self._second=0
            if self._min<59:
                self._min+=1
            else:
                self._min=0
                if self._hour<23:
                    self._hour+=1
                else:
                    self._hour=0
def main():
    t=clock(23,59,59)
    while True:
        print('%02d:%02d:%02d'%(t._hour,t._min,t._second))
        t.run()
        sleep(1)

if __name__=='__main__':
    main()        
    