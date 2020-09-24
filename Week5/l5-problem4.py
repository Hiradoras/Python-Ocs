keys = ['Jan','Feb','Mar','Apr',
'May','June','July','Aug','Sep',
'Oct','Nov','Dec']
values = ['1','2','3','4','5','6','7','8','9','10','11','12']

for i in range(0,12):
    if i ==0:
        print(" {'"+keys[i]+"': "+values[i]+", ", end="")
    if i>0 and i<11:
        print("'"+keys[i]+"': "+values[i]+", ",end="")
    if i ==11:
        print("'"+keys[i]+"': "+values[i]+"}")    
        break