import csv
import datetime
import collections
from pathlib import Path
from collections import defaultdict

# result_dict = DefaultDict()

res_dict = defaultdict(list)


path = Path("") / 'data3.csv'

with open(path) as f:
    reader = csv.reader(f, delimiter=";")

    for row in reader:
        # print(row)
        if row[0] == '70939599':
            time1 = datetime.datetime.strptime(
                f'{row[2]} {row[3]}', r'%d.%m.%Y %H:%M:%S')

            time2 = datetime.datetime.strptime(
                f'{row[5]} {row[6]}', r'%d.%m.%Y %H:%M:%S')

            delta_time = time2 - time1
            print(time1, '    ', time2, '    delta: ', delta_time)

        for count in range(6, len(row), 3):
            if len(row[count].split(':')) == 3 and len(row[count-3].split(':')) == 3:
                time_task = datetime.datetime.strptime(
                    f'{row[count-1]} {row[count]}', r'%d.%m.%Y %H:%M:%S') - datetime.datetime.strptime(
                    f'{row[count-4]} {row[count-3]}', r'%d.%m.%Y %H:%M:%S')
                res_dict[row[count-2]].append(time_task.total_seconds())
                # print(time_task)

    print(res_dict)
    for task in res_dict:
        counter = 0
        sum_time = 0
        for elem in res_dict[task]:
            sum_time += elem

        avg = sum_time / len(res_dict[task])
        print(avg)
