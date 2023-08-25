
money = 8280000


list_speech_num = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
list_speech_index = ['đồng', 'mươi', 'trăm', 'nghìn', 'mươi', 'trăm', 'triệu', 'mươi', 'trăm', 'tỷ']

money_str = ''
for idx, k in enumerate(str(money)):
    # speech num
    money_str += list_speech_num[int(k)] + ' '

    # speech index
    money_str += list_speech_index[len(str(money)) - idx - 1] + ' '

money_str = money_str.replace('không trăm không mươi không đồng', '' )
money_str = money_str.replace('không nghìn', 'nghìn')
money_str = money_str.replace('mươi một', 'mươi mốt')

print(money_str)

