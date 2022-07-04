tupleFruits = ("apple","banana","cherry") #Tuple
listfruits = ["apple","banana","cherry"] #list
print("original list",tupleFruits)
print("original list",listfruits)
#เปลี่ยนค่าในtuble
x=list(tupleFruits) #แปลงเป็นlistแล้วเก็บในตัวแปรx
x[1]="blueberry"
tupleFruits=tuple(x)
print("เปลี่ยนค่าtuple:",tupleFruits)
#เพิ่มค่าในtuble
x=list(tupleFruits) #แปลงเป็นlistแล้วเก็บในตัวแปรx
x.append("melon")
tupleFruits=tuple(x)
print("เพิ่มค่าtuple:",tupleFruits)
#ลบtuple
x=list(tupleFruits)
x.remove("cherry")
tupleFruits=tuple(x)
print("ลบค่าtuple:",tupleFruits)
#join tuple
vege=("tomato","cucumber","onion")
fruitVage=tupleFruits+vege
print("join tuper:",fruitVage)
x = range(3,6)
for n in x:
    print("range x:",n)
y = range(3,20,2)
for m in y:
    print("range y:",m)
#ทักษ์ดนัย บุษบง เลขที่ 3 ม.6/11