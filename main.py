import json
from collections import defaultdict

def solve(f, t):
    with open(f, 'r', encoding='utf-8') as jsonfile:
        state = []
        data = json.load(jsonfile)
        h,s = 0,0
        for d in data:
            if d['tovar_nomi'] == t:
                h += d['hajm']
                s += d['soni']
                state.append(d['davlat'])

    set_state = set(state)

    result = {
        "hajmi" : h,
        "soni"  : s,
        "davlatlar" : set_state
    }

    return result
f = 'EXPORT.json'
t = "Olma"
r = solve(f, t)
print(r)