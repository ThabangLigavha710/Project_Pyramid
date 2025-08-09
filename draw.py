

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    shape = input("Enter a shape (1. Pyramid, 2. Square, 3. Triangle): ").lower()
    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():

    height = int(input("Enter a height between 3 - 80: "))
    return height


# TODO: Step 2
def draw_pyramid(height, outline):

    star = "*"
    space = " "
    count = height

    if not outline:
        for i in range(height+1):
            print((count * space) + (i*star), end='')
            print(((i-1)*star))
            count -= 1
    else:
        inner_val = 1
        for i in range(height):
            if i == 1:
                print((count * space) + (i*star))
                count -= 1
            elif i > 1:
                print((count * space) + star, end='')
                print((space * inner_val) + star)
                inner_val += 2
                # print(((i-1)*space) + star)
                count -= 1
        print((count * space) + star*(height + (height-1)))
                


    # print('pyramid')


# TODO: Step 3
def draw_square(height, outline):
    
    star = "*"
    # count = height
    
    for i in range(height):
        print(height*star)
    # print('square')


# TODO: Step 4
def draw_triangle(height, outline):

    star = "*"

    for i in range(height+1):
        print(i*star)
        height -= 1

    # print('triangle')


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid".lower():
        draw_pyramid(height, outline)
    elif shape == "square".lower():
        draw_square(height, outline)
    elif shape == "triangle".lower():
        draw_triangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    outline = input("Outline Only (y/N)? ").lower()

    if outline == "".strip() or outline == "n".lower().strip():
        return False
    else:
        if outline == "y".lower().strip():
            return True

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

