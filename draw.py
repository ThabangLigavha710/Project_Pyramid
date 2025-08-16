

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    shape = input("Enter a shape (1. Pyramid, 2. Square, 3. Triangle, 4. diamond,"
                  + " 5. hourglass, 6. rectangle): ").lower()
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
                count -= 1
        print((count * space) + star*(height + (height-1)))
                


# TODO: Step 3
def draw_square(height, outline):
    
    star = "*"
    
    if not outline:
        for i in range(height):
            print(height*star)
    else:
        count = 1
        for i in range(height):
            if i == 0 or i == height-1:
                print(height*star)
            else:
                print(star + ((height-2)*" ") + star)
                count += 1

# TODO: Step 4
def draw_triangle(height, outline):

    star = "*"
    orgin_height = height

    if not outline:
        for i in range(height+1):
            print(i*star)
            height -= 1
    else:
        count = 1
        for i in range(height):
            if i == 1:
                print(i*star)
                height -= 1
            elif i > 1:
                print(star + (count*" ") + star)
                count += 1
                height -= 1
        print((orgin_height*star)+star)

   
def draw_diamond(height, outline):

    star = "*"
    space = " "
    count = height
    next_height = height-1
    next_count = 1


    if not outline:
        for i in range(height+1):
            print((count * space) + (i*star), end='')
            print(((i-1)*star))
            count -= 1

        for j in range(next_height, -1, -1):
            print((next_count * space) + (j*star), end='')
            print(((j-1)*star))
            next_count += 1   

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
                count -= 1

        for j in range(next_height, -1, -1):
            if j == 0:
                print(((next_count)*space) + star)
            else:
                print((next_count * space) + star, end='')
                print((space * inner_val) + star)
                inner_val -= 2
                next_count += 1  



def draw_hourglass(height, outline):

    star = "*"
    space = " "
    count = height
    next_height = height-1
    next_count = 1


    if not outline:
        for j in range(next_height+1, -1, -1):
            if j != 0:
                print((next_count * space) + (j*star), end='')
                print(((j-1)*star))
                next_count += 1
        
        for i in range(height+1):
            if i != 0 and i != 1:
                print(((count-1) * space) + (i*star), end='')
                print(((i-1)*star))
                count -= 1


    else:
        inner_val = ((next_height+1)*2)-4
        origin_height = next_height
        for j in range(next_height, -1, -1):
            if origin_height == next_height:
                print(((j+1)*star)*2)
                origin_height = 0

            elif j > 0:
               
                print((next_count * space) + star, end='')
                print((space * inner_val) + star)
                inner_val -= 2
                next_count += 1

        for i in range(height+1):
            origin_height = height
            if i == 1:
                print(( count * space) + ((i+1)*star))
                count -= 1
                inner_val += 2
            elif i > 1 and i < origin_height:
                print((count * space) + star, end='')
                print((space * inner_val) + star)
                inner_val += 2
                count -= 1
            elif i == origin_height:
                print((i*star)*2)
                origin_height = 0
            else:
                count-=1


def draw_rectangle(height, outline):
    star = "*"
    
    if not outline:
        for i in range(height):
            print(((height*2)-1)*star)
    else:
        count = 1
        for i in range(height):
            if i == 0 or i == height-1:
                print(((height*2)-1)*star)
            else:
                print(star + ((((height*2)-1)-2)*" ") + star)
                count += 1



# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "1" or shape == "pyramid".lower():
        draw_pyramid(height, outline)
    elif shape == "2" or shape == "square".lower():
        draw_square(height, outline)
    elif shape == "3" or shape == "triangle".lower():
        draw_triangle(height, outline)
    elif shape == "4" or shape == "diamond".lower():
        draw_diamond(height, outline)
    elif shape == "5" or shape == "hourglass".lower():
        draw_hourglass(height, outline)
    elif shape == "6" or shape == "rectangle".lower():
        draw_rectangle(height, outline)


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

