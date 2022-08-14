import json
from collections import defaultdict

badge_times = [
["Paul", "1355"], ["Jennifer", "1910"], ["Jose", "835"],
["Jose", "830"], ["Paul", "1315"], ["Chloe", "0"],
["Chloe", "1910"], ["Jose", "1615"], ["Jose", "1640"],
["Paul", "1405"], ["Jose", "855"], ["Jose", "930"],
["Jose", "915"], ["Jose", "730"], ["Jose", "940"],
["Jennifer", "1335"], ["Jennifer", "730"], ["Jose", "1630"],
["Jennifer", "5"], ["Chloe", "1909"], ["Zhang", "1"],
["Zhang", "10"], ["Zhang", "109"], ["Zhang", "110"],
["Amos", "1"], ["Amos", "2"], ["Amos", "400"],
["Amos", "500"], ["Amos", "503"], ["Amos", "504"],
["Amos", "601"], ["Amos", "602"], ["Paul", "1416"],
]


name_logins = defaultdict(list)

for name, logins in badge_times:
    name_logins[name].append(int(logins))

result = dict()

keys = name_logins.keys()

for k in keys:
    name_logins[k].sort()

for name, login in name_logins.items():
    #print(f"checking for {name}, {login}")
    l = 0
    r = 1
    while True:
        while r < len(login) and login[l] + 100 >= login[r]:
            r += 1
        
        if r - l >= 3:
            result[name] = login[l:r]
            break

        if r == len(login) or r == len(login)-1:
            break
        
        while l <= r and login[l] + 100 < login[r]:
            l += 1

        r += 1

print(json.dumps(result, indent=4))

