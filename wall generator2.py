brick = '[--]'
in_layer = 5
whole = 12


def prepare_layers(whole, in_layer):
    layers = ['']  # start with first layer
    last_layer = 0
    for i in range(whole):
        x = i // in_layer  # 0
        if x > last_layer:  # check when i need to add next layer to wall
            last_layer = x
            layers.append(brick)
        else:
            layers[x] += brick
    return layers[::-1]


def build_the_wall(layers):
    for i, layer in enumerate(layers):
        if i % 2:
            if len(layer) == len(brick) * in_layer:
                print(layer[2:] + layer[:2])
            else:
                print(' ' * (len(brick) // 2) + layer)
        else:
            print(layer)
            
            
def build_the_whole_wall(whole, in_layer):
    layers = prepare_layers(whole, in_layer)
    for i, layer in enumerate(layers):
        if i % 2:
            if len(layer) == len(brick) * in_layer:
                print(layer[2:] + layer[:2])
            else:
                print(' ' * (len(brick) // 2) + layer)
        else:
            print(layer)


layers = prepare_layers(whole, in_layer)
build_the_wall(layers)
print()
build_the_whole_wall(12, 5)
