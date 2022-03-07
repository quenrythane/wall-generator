brick = '[--]'
in_layer = 5
bricks_ammount = 12


# prepare list where every element is part of wall (1 element = 1 layer)
def prepare_layers(bricks_ammount, in_layer):
    layers = ['']  # start with first layer
    last_layer = 0
    for i in range(whole):
        x = i // in_layer 
        if x > last_layer:  # check when i need to add next layer to wall
            last_layer = x
            layers.append(brick)
        else:
            layers[x] += brick
    return layers[::-1]


# take list from above and print the wall picture
def build_the_wall(layers):
    for i, layer in enumerate(layers):
        if i % 2:
            if len(layer) == len(brick) * in_layer:
                print(layer[2:] + layer[:2])
            else:
                print(' ' * (len(brick) // 2) + layer)
        else:
            print(layer)
            


# it's sum of 2 function above            
def build_the_whole_wall(bricks_ammount, in_layer):
    layers = prepare_layers(bricks_ammount, in_layer)
    build_the_wall(layers)


layers = prepare_layers(bricks_ammount, in_layer)
build_the_wall(layers)
print()
build_the_whole_wall(12, 5)
