file = open("C:/Users/HP/Desktop/data.py","w",encoding="utf-8")
file.write("Name : Hakan\nSurname : Temiz\nGender : Male\nUsername : Eagle\nJob : Student\n")
file = open("C:/Users/HP/Desktop/data.py","r",encoding="utf-8")
dict1={}
for i in file:
    a,b=i.split(":")
    b,c=b.split("\n")
    dict1[a]=b
print(dict1)
file.close()