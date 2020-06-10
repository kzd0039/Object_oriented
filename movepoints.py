from math import sqrt
class point:

    def __init__(self,x=0,y=0):
        self._x = x
        self._y = y
    
    def move_by(self,dx,dy):
        self._x+=dx
        self._y+=dy
    
    def move_to(self,x,y):
        self._x=x
        self._y=y
    
    def dist_to(self,x,y):
        dx=self._x-x
        dy=self._y-y
        return sqrt(dx**2+dy**2)

    def new_dist_to(self,other):
        dx=self._x-other._x
        dy=self._y-other._y
        return sqrt(dx**2+dy**2)
    
def main():
    p1=point(1,2)
    p1.move_by(1,2)
    print(p1._x,p1._y)
    print(p1.dist_to(3,4))
    p2=point()
    print('%.3f'%(p1.new_dist_to(p2)))

if __name__=='__main__':
    main()