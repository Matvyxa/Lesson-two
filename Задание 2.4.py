name = str(input("Введите текст через пробел")).split()
print(name)
for i in range(len(name)):
  if len(name[i]) <= 10:
    print(i, name[i])
  else:
    print(i, (name[i])[:10])