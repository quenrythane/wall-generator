brick = '[--]'
in_layer = 5
whole = 12

layers = ['']
last_layer = 0
for i in range(whole):
    x = i // in_layer  # 0
    if x > last_layer:
        last_layer = x
        layers.append(brick)
    else:
        layers[x] += brick

for i, layer in enumerate(layers[::-1]):
    if i % 2:
        if len(layer) == len(brick) * in_layer:
            print(layer[2:] + layer[:2])
        else:
            print(' ' * (len(brick) // 2) + layer)
    else:
        print(layer)







