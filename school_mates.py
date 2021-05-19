school_mates = [
    {'school_class': '4a', 'scores' : [3, 4, 4, 5, 2]}, 
    {'school_class': '9б', 'scores' : [4, 5, 3, 2, 5]}, 
    {'school_class': '3в', 'scores' : [2, 3, 3, 2, 3]}, 
    {'school_class': '6а', 'scores' : [4, 5, 5, 5, 4]}
]

def sum_mate(scores):
    sum_mate = 0
    for mate in scores:
        sum_mate += mate
    return sum_mate

sum_mate_school = 0
for x in range(len(school_mates)):
    sum_mate_school = sum_mate_school + sum_mate(school_mates[x]['scores'])

aver_mate_school = sum_mate_school / len(school_mates)
print(f'Средний бал по всей школе =  {aver_mate_school}')

for y in range(len(school_mates)):
    name_class = school_mates[y]['school_class']
    average_class_mates = sum_mate(school_mates[y]['scores']) / len(school_mates[y]['scores'])
    print(f'Средний бал по классу {name_class} составляет {average_class_mates}')

#print(sum_mate(school_mates[0]['scores']))
#print(sum_mate(school_mates[1]['scores']))