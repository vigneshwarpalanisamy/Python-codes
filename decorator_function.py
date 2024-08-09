import time
def outer_decorator(functionpointer):
    def newinnerfunction(*args,**kwds):
        print("Process started")
        i=functionpointer(*args,**kwds)
        print ("Process completed")
        return i
    return newinnerfunction

def mydecorator(functionpointer):
    def newinnerfunction(*args,**kwds):
        start_time = time.time()
        i=functionpointer(*args,**kwds)
        end_time=time.time()
        print(f'Time Taken - {end_time - start_time}')
        return i
    return newinnerfunction


@outer_decorator
@mydecorator
def areacalc():
    file=open(r"myTet 5.stl","r")
    lines=file.readlines()
    coordinates=[]
    Area=0
    for i in lines:
        reading=i.split()
        if reading[0]=="vertex":
            coordinates.append([float(reading[1]),float(reading[2]),float(reading[3])])
        if len(coordinates)==3:
            x1,y1,z1=coordinates[0]
            x2,y2,z2=coordinates[1]
            x3,y3,z3=coordinates[2]
            a=((x2-x1)**2 +(y2-y1)**2 +(z2-z1)**2)**0.5
            b=((x3-x2)**2 +(y3-y2)**2 +(z3-z2)**2)**0.5
            c=((x3-x1)**2 +(y3-y1)**2 +(z3-z1)**2)**0.5
            s=(a+b+c)/2
            A=(s*(s-a)*(s-b)*(s-c))**0.5
            Area+=A
            coordinates.clear()
    print(f'Stl file area = {Area}')

areacalc()



