name = []
name1 = {"название": " ", "цена": " ", "количество": " ", "eд": " "}
name2 = {"название": [], "цена": [], "количество": [], "eд": []}
num = 0
while True:
    if input("Для выхода нажмите 's', для продолжения 'enter': ").upper() =='S':
        break
    num += 1
    for a in name1.keys():
        _ = input(f"Введите параметры позиции '{a}': ")
        name1[a] = int(_) if a == "цена" or (a == "количество") else _
        name2[a].append(name1[a])
    name.append((num, name1))
    print(f"Текущая аналитика по товарам:")
    for key, value in name2.items():
        print(f"{key[:10]}: {value}")



