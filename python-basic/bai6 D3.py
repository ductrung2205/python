from scipy.spatial.distance import cdist

map_data = [('A', [76, 203]), ('B', [165, 75]), ('C', [366, 159]), ('D', [342, 307]),
            ('E', [201, 402]), ('F', [353, 97]), ('G', [489, 310]), ('H', [390, 380]),
            ('I', [501, 302]), ('J', [389, 510]), ('K', [509, 350]), ('L', [410, 160]),
            ('M', [380, 110])]
#Khoảng cách giữa 2 điểm A,H
map.dict = dict(map_data)
D = cdist([map.dict('A')],[map.dict['H']])
print(D)