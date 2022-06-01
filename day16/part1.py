import re
sues = dict()

ticker = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

with open('input.txt', 'r') as f:
    items = f.read()

for line in items.split('\n'):
    x = int(line.split(": ")[0].split(' ')[1])
    matches = re.findall('(\w+): (\d+)', line)
    sues[x] = [(type, int(num)) for type, num in matches]

for sue, features in sues.items():
    wrongsue = False
    for feature, num in features:
        if ticker[feature] != num:
            wrongsue = True
    if not wrongsue:
        with open('output1.txt', 'w') as f:
            print(sue, file=f)