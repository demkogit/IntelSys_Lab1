from PIL import Image

image = Image.open("imgs/f11.bmp")
width = image.size[0]
height = image.size[1]
pix = image.load()
for h in range(height):
    for w in range(width):
        if (pix[w, h] == 0):
            pix[w, h] = 1
        else:
            pix[w, h] = 0
image.close()
arrs = []

def InitArrs():
    arr = []
    with open("patterns4x4_2.txt") as f:
        for line in f:
            if (line == '\n'):
                arrs.append(arr)
                arr = []
            else:
                arr.append([int(x) for x in line.split()])
    print('init patterns')


# Up = 0; Right = 1; Down = 2; Left = 3;
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
        if (img[y, x] == 2):
            break
        img[y, x] = 2
        # print('[ %s, %s ]  %s' % (x, y, i))

    return res


def main():
    counts = [0] * len(arrs)
    flags = [True] * len(arrs)

    for l in range(height - 3):
        for k in range(width - 3):
            for c in range(len(arrs)):
                for i in range(4):
                    if (flags[c]):
                        for j in range(4):
                            if (pix[j + k, i + l] != arrs[c][i][j]):
                                flags[c] = False
                                break
                    else:
                        break

            for p in range(len(flags)):
                if (flags[p]):
                    counts[p] += 1
                    # print('flag[%s]  [ %s, %s ]' % (p, k, l))
                flags[p] = True

    sum = 0
    str1 = ''
    for i in range(len(counts)):
        print(counts[i])
        if (counts[i] > 0):
            for e in range(4):
                for ee in range(4):
                    str1 += str(arrs[i][e][ee]) + ' '
                print(str1)
                str1 = ''
        sum += counts[i]

    isClosed = IsClosed(pix)

    print('Количество углов: %s' % sum)
    if (isClosed):
        print('Контур замкнутый...')
    else:
        print('Контур не замкнутый!')

    if (isClosed):
        if (sum == 4):
            print('Это прямоугольник?')
        elif (sum == 3):
            print('Это треугольник?')
        else:
            print('Я не знаю что это за фигура(')


if __name__ == "__main__":
    InitArrs()
    main()
