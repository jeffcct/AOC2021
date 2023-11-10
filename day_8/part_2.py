letters = [None, None, None, None, None, None, None]
fives = []
sixes = []
length = len(val) 
if length == 2:
    letters[0] = val
elif length == 4:
    letters[3] = val
elif length == 3:
    letters[6] = val
elif length == 7:
    letters[7] = val

if len(val) == 5:
    if letters[1] == None:
        continue
    for letter in letters[1]:
        if letter not in val:
            
        
    
if len(val) == 6:
    