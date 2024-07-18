file=open(r"myTet 5.stl","r")
lines=file.readlines()
#print(lines)
vertices=[]

for i in lines:
    reading=i.split()
    if reading[0]=="vertex":
        vertices.append([float(reading[1]),float(reading[2]),float(reading[3])])
#Finding distance b/w two vertices
triangle=int(len(vertices)/3)
Area=0
print(f"No of triangles is {triangle}" )

for j in range(0,triangle):
#side a
        x2x1=vertices[(j*3)+1][0]-vertices[(j*3)][0]
        y2y1=vertices[(j*3)+1][1]-vertices[(j*3)][1]
        z2z1=vertices[(j*3)+1][2]-vertices[(j*3)][2]
        a=(x2x1**2 + y2y1**2 + z2z1**2 )**(1/2)

#side b
        x3x2=vertices[(j*3)+2][0]-vertices[(j*3)+1][0]
        y3y2=vertices[(j*3)+2][1]-vertices[(j*3)+1][1]
        z3z2=vertices[(j*3)+2][2]-vertices[(j*3)+1][2]
        b=(x3x2**2 + y3y2**2 + z3z2**2 )**(1/2)

#side c
        x3x0=vertices[(j*3)+2][0]-vertices[(j*3)][0]
        y3y0=vertices[(j*3)+2][1]-vertices[(j*3)][1]
        z3z0=vertices[(j*3)+2][2]-vertices[(j*3)][2]
        c=(x3x0**2 + y3y0**2 + z3z0**2 )**(1/2)
        s=(a+b+c)/2
        A=((s*(s-a)*(s-b)*(s-c)))**(1/2)
        Area+=A

print(f"The surface area of the stl file is {Area}")
