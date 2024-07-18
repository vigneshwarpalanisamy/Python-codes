file=open(r"myTet 5.stl","r")
lines=file.readlines()
coordinates=[]
Area=0
for i in lines:
    reading=i.split()
    if reading[0]=="vertex":
        coordinates.append([float(reading[1]),float(reading[2]),float(reading[3])])
for index in range(0,len(coordinates),3):
        x1,y1,z1=coordinates[index]
        x2,y2,z2=coordinates[index+1]
        x3,y3,z3=coordinates[index+2]
        a=((x2-x1)**2 +(y2-y1)**2 +(z2-z1)**2)**0.5
        b=((x3-x2)**2 +(y3-y2)**2 +(z3-z2)**2)**0.5
        c=((x3-x1)**2 +(y3-y1)**2 +(z3-z1)**2)**0.5
        s=(a+b+c)/2
        A=(s*(s-a)*(s-b)*(s-c))**0.5
        Area+=A
print(Area)
