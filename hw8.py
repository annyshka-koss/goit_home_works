import datetime

persons_bd=[
    {'name': 'Anna', 'birthday': datetime.date(1982, 2, 2)},
    {'name': 'Maria', 'birthday': datetime.date(1983, 3, 3)},
    {'name': 'Huanetta', 'birthday': datetime.date(1984, 4, 4)},
    {'name': 'Rodriges', 'birthday': datetime.date(1985, 5, 5)},
    {'name': 'Diablo', 'birthday': datetime.date(1986, 6, 6)}
]


def congratulate(persons_bd):
    week=[['Monday: '], ['Tuesday: '], ['Wednesday: '], ['Thursday: '], ['Friday: ']]
    for dicts in persons_bd:
        if dicts['birthday'].timetuple().tm_wday == 0 or \
                dicts['birthday'].timetuple().tm_wday == 5 or dicts['birthday'].timetuple().tm_wday == 6:
            week[0].append(dicts['name'])
        elif dicts['birthday'].timetuple().tm_wday == 1:
            week[1].append(dicts['name'])
        elif dicts['birthday'].timetuple().tm_wday == 2:
            week[2].append(dicts['name'])
        elif dicts['birthday'].timetuple().tm_wday == 3:
            week[3].append(dicts['name'])
        elif dicts['birthday'].timetuple().tm_wday == 4:
            week[4].append(dicts['name'])
    for elem in week:
        if len(elem) > 1:
            elem=', '.join(elem).replace(',', '', 1)
            print(elem)


congratulate(persons_bd)
