seasons = {"К зиме": (1, 2, 12),
           "К весне": (3, 4, 5),
           "К лету": (6, 7, 8),
           "К осене": (9, 10, 11)}
month = int(input("Узнайте к какому времени года относится введенный месяц: "))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
