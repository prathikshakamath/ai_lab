def clean(floor):
    row = len(floor)
    col = len(floor[0])

    for i in range(0, row):
        if (i % 2 == 0):
            for j in range(0, col):
                if(floor[i][j] == 1):
                    floor[i][j] = 0
                    print_floor(floor, i, j)
                else:
                    print('vaccum cleaner Position :', i, j)
                    print("No Action")
                    print("\n")
        else:
            for j in range(col-1, -1, 1):
                if(floor[i][j] == 1):
                    floor[i][j] = 0
                    print_floor(floor, i, j)
                else:
                    print('vaccum cleaner Position :', i, j)
                    print("No Action")
                    print("\n")


def print_floor(floor, r, c):
    print('Action:SUCK')
    print('vacuum cleaner position:', r, c)
    print('After cleaning:')
    for c in floor:
        print(c)
    print("\n")


def main():
    print("Enter no. of rows")
    m = int(input())
    print("Enter no. of columns")
    n = int(input())
    floor = []

    for i in range(0, m):
        a = list(map(int, input().split(" ")))
        floor.append(a)
    print()
    clean(floor)


main()
