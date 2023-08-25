# input

victims = [('Hùng', 18, 'nam'),
           ('Lan', 23, 'nữ'),
           ('Lão', 65, 'nam'),
           ('Bà', 62, 'nữ'),
           ('TinTin', 8, 'chó'),
           ('Cu', 6, 'nam'),
           ('Bé', 12, 'nữ')]


# output
# a)
# victims_sorted = [('Lão', 65, 'nam'),
#                   ('Bà', 62, 'nữ'),
#                   ('Lan', 23, 'nữ'),
#                   # ....
#                   ('Cu', 6, 'nam')]
victims.sort(key=lambda bien2: bien2[1], reverse=True)
print(victims)



victims2 = sorted(victims, key=lambda bien2: bien2[1])
victims2.sort(key=lambda bien2: bien2[2] != 'chó', reverse=True)
print(victims2)
