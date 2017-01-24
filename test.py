import numpy as np

lightbulbs = [0] * 100
def flip(num):
    return 1 if num == 0 else 0

for person in range(1, 101):
    for lightbulb in range(1, 101):
        if lightbulb % person is 0:
            lightbulbs[lightbulb - 1] = flip(lightbulbs[lightbulb - 1])

print('Final count: %i' % lightbulbs.count(1))
print(np.array(lightbulbs).reshape(10, 10))
