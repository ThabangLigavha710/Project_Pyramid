# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower().rstrip()
    if shape != "":
        return shape
    else:
        return get_shape()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")

    if not height.isdigit():
        return get_height()
    else:
        return int(height)


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline:
        for row in range(1, height + 1):
            if row == 1:
                print(" " * (height - row) + "*")
            elif row == height:
                print("*" * (2 * height - 1))
            else:
                print(" " * (height - row) + "*" + " " * (2 * row - 3) + "*")
    else:
        for row in range(1, height + 1):
            print(" " * (height - row) + "*" * (2 * row - 1))


# TODO: Step 3
def draw_square(height, outline):
    if outline:
        for row in range(height):
            if row in (0, height - 1):
                print("*" * height)
            else:
                print("*" + " " * (height - 2) + "*")
    else:
        for _ in range(height):
            print("*" * height)


# TODO: Step 4
def draw_triangle(height, outline):
    if outline:
        for row in range(1, height + 1):
            if row == 1:
                print("*")
            elif row == height:
                print("*" * height)
            else:
                print("*" + " " * (row - 2) + "*")
    else:
        for row in range(1, height + 1):
            print("*" * row)


def draw_diamond(height, outline):
    if not outline:
        for row in range(1, height + 1):
            print(" " * (height - row) + "*" * (2 * row - 1))
        for row in range(height - 1, 0, -1):
            print(" " * (height - row) + "*" * (2 * row - 1))
    else:
        for row in range(1, height + 1):
            if row == 1:
                print(" " * (height - row) + "*")
            elif row == height:
                print("*" * (2 * height - 1))
            else:
                print(" " * (height - row) + "*" + " " * (2 * row - 3) + "*")
        for row in range(height - 1, 0, -1):
            if row == 1:
                print(" " * (height - row) + "*")
            else:
                print(" " * (height - row) + "*" + " " * (2 * row - 3) + "*")


def draw_hourglass(height, outline):
    if not outline:
        for row in range(height, 0, -1):
            print(" " * (height - row) + "*" * (2 * row - 1))
        for row in range(2, height + 1):
            print(" " * (height - row) + "*" * (2 * row - 1))
    else:
        for row in range(height, 0, -1):
            if row == height:
                print("*" * (2 * height - 1))
            elif row == 1:
                print(" " * (height - 1) + "*")
            else:
                print(" " * (height - row) + "*" + " " * (2 * row - 3) + "*")
        for row in range(2, height + 1):
            if row == height:
                print("*" * (2 * height - 1))
            elif row == 1:
                print(" " * (height - row) + "*")
            else:
                print(" " * (height - row) + "*" + " " * (2 * row - 3) + "*")


def draw_rectangle(height, outline):
    width = (height * 2) - 1
    if outline:
        for row in range(height):
            if row in (0, height - 1):
                print("*" * width)
            else:
                print("*" + " " * (width - 2) + "*")
    else:
        for _ in range(height):
            print("*" * width)


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    shape = str(shape).strip().lower()
    if shape == "1" or shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "2" or shape == "square":
        draw_square(height, outline)
    elif shape == "3" or shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "4" or shape == "diamond":
        draw_diamond(height, outline)
    elif shape == "5" or shape == "hourglass":
        draw_hourglass(height, outline)
    elif shape == "6" or shape == "rectangle":
        draw_rectangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    while True:
        outline = input("Outline Only (y/N)? ").strip().lower()
        if outline in ("", "n"):
            return False
        if outline == "y":
            return True


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

