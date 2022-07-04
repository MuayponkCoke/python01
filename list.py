fruits = ["apple","banana","cherry","orange"]
print(fruits[0])
#เปลี่ยนนำในlsit
fruits[1]="blackcurrant"
print(fruits)
fruits[1:3]=["banana","kiwa","melon"]
print(fruits)
fruits[1:3]=["blackcurrant"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"banana")
print(fruits)
tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("pineapple")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits ลบตัวแปรlistทิ้งไปจากระบบ
#เรียงค่าในlist
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#รวมlist
vege=["carrot","potata","cucamber"]
all=fruits+vege
print(all)
#นาย ทักษ์ดนัย บุษบง ม.6/11 เลขที่ 3