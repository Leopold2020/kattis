list1 = []
modulos = set()
for i in range(10):
    number = int(input())
    modulos.add(number%42)
print(len(modulos))