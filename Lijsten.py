lijst1=[]
for i in range (5):
  lijst1.append(int(input("geef een getal in: ")))
  
lijst2=[11, 9, 19, 13, 17]
lijst1.extend(lijst2)
lijst1.sort()
for x in lijst1:
  print(x)