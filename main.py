arr = [['-', '-', '-'],
     ['-', '-', '-'],
     ['-', '-', '-']]
def matrix(arr: list[list[str]], s: str, i: int, j: int):
    arr[i][j] = s

def move(arr: list[list[str]]):
    is_x_turn = True
    for i in arr:
        for j in i:
            print(f'Игрок {"X" if is_x_turn else "0"}, сделайте ход')
            i = int(input('Введите стобец: '))
            j = int(input('Введите строчку: '))
            while arr[i][j] != '-':
                print("Тут занято. Введите заново")
                i = int(input('Введите стобец: '))
                j = int(input('Введите строчку: '))
            c = "X" if is_x_turn else "0"
            matrix(arr, c, i, j)
            print_matrix(arr)
            if check_winner(arr,c):
                print(f"Победил {c}")
                return
            is_x_turn = not is_x_turn

def print_matrix(arr):
    for i in arr:
        print(i)

def check_winner(arr: list[list[str]], c: str):
    if (arr[0][0] == c and arr[1][1] == c and arr[2][2] == c) or \
            (arr[0][2] == c and arr[1][1] == c and arr[2][0] == c) or \
             (arr[0][0] == c and arr[0][1] == c and arr[0][2] == c) or \
              (arr[1][0] == c and arr[1][1] == c and arr[1][2] == c) or \
               (arr[2][0] == c and arr[2][1] == c and arr[2][2] == c) or \
                (arr[0][0] == c and arr[1][0] == c and arr[2][0] == c) or \
                 (arr[0][1] == c and arr[1][1] == c and arr[2][1] == c) or \
                  (arr[0][2] == c and arr[1][2] == c and arr[2][2] == c):
        return True
    else:
        return False

move(arr)

