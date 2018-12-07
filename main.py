from PIL import Image

image = Image.open("f1.bmp")
width = image.size[0]
height = image.size[1]
pix = image.load()

arrs = [
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 1, 1],
     [0, 0, 0, 0]],

    [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0]],

    [[0, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0]],

    [[0, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 0],
     [0, 1, 0, 0]],

    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0]],

    [[0, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 0, 1]],

]


# Up = 0; Right = 1; Down = 2; Left = 3;
def leftRotation(dir):
    if (dir == 0):
        return [0, -1, 3]
    if (dir == 1):
        return [-1, 0, 0]
    if (dir == 2):
        return [0, 1, 1]
    if (dir == 3):
        return [1, 0, 2]


def rightRotation(dir):
    if (dir == 0):
        return [0, 1, 1]
    if (dir == 1):
        return [1, 0, 2]
    if (dir == 2):
        return [0, -1, 3]
    if (dir == 3):
        return [-1, 0, 0]


def IsClosed(img):
    firstPix = False
    oldX = 0
    oldY = 0
    for i in range(height):
        if (not firstPix):
            for j in range(width):
                if (img[j, i] == 1):
                    oldX = i
                    oldY = j
                    firstPix = True
                    break;
        else:
            break;

    x = oldX
    y = oldY - 1
    dir = 0
    res = False
    while (True):
        i += 1
        #print("[ %s, %s ]  dir:%s" % (x, y, dir))
        if (dir == 0):
            if (img[y + 1, x] == 1):
                if (img[y, x - 1] == 1):
                    if (img[y - 1, x] == 1):
                        x += 1
                        dir = 2
                    else:
                        y -= 1
                        dir = 3
                else:
                    x -= 1
                    dir = 0
            else:
                y += 1
                dir = 1
        elif (dir == 1):
            if (img[y, x + 1] == 1):
                if (img[y + 1, x] == 1):
                    if (img[y, x - 1] == 1):
                        y -= 1
                        dir = 3
                    else:
                        x -= 1
                        dir = 0
                else:
                    y += 1
                    dir = 1
            else:
                x += 1
                dir = 2
        elif (dir == 2):
            if (img[y - 1, x] == 1):
                if (img[y, x + 1] == 1):
                    if (img[y + 1, x] == 1):
                        x -= 1
                        dir = 0
                    else:
                        y += 1
                        dir = 1
                else:
                    x += 1
                    dir = 2
            else:
                y -= 1
                dir = 3
        elif (dir == 3):
            if (img[y, x - 1] == 1):
                if (img[y - 1, x] == 1):
                    if (img[y, x + 1] == 1):
                        y += 1
                        dir = 1
                    else:
                        x += 1
                        dir = 2
                else:
                    y -= 1
                    dir = 3
            else:
                x -= 1
                dir = 0

        if (x == oldX and y == oldY - 1):
            res = True
            break
        if (i > 100000):
            break

    return res


def main():
    counts = [0] * len(arrs)
    flags = [True] * len(arrs)
    i = 0
    j = 0

    for l in range(height - 2):
        for k in range(width - 2):
            for c in range(len(arrs)):
                while (True):
                    if (j == 3):
                        j = 0
                        i += 1
                    if (i == 3):
                        i = 0
                        j = 0
                        break
                    if (pix[j + k, i + l] != arrs[c][i][j]):
                        flags[c] = False
                        j = 0
                        i = 0
                        break
                    j += 1

            for p in range(len(flags)):
                if (flags[p]):
                    counts[p] += 1
                flags[p] = True

    for i in range(len(counts)):
        print(counts[i])

    print('Фигура замкнута?: %s' % IsClosed(pix))


if __name__ == "__main__":
    main()
