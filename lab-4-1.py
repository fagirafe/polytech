# TODO решите задачу
import json

def task(file):
    with open(file, 'r') as f:
        data = json.load(f)

    total_sum = 0.0

    for x in data:
        if 'score' in x and 'weight' in x:
            plus = x['score'] * x['weight']
            total_sum += plus

    return round(total_sum, 3)

result = task('input.json')
print(result)
