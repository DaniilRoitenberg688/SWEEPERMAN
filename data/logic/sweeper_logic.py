from random import randrange


class Sweeper:
    def __init__(self):
        self.field = [['' for _ in range(10)] for _ in range(10)]
        self.player_field = [['' for _ in range(10)] for _ in range(10)]
        self.moves = 0
        self.bombs_coordinates = []
        self.flags_coordinates = []
        self.flags_col = 0

    def poles_around(self, x, y):
        if x == 0 and y == 0:
            return [(x + 1, y + 1), (x, y + 1), (x + 1, y)]

        elif x == 9 and y == 9:
            return [(x - 1, y - 1), (x, y - 1), (x - 1, y)]

        elif x == 0 and y == 9:
            return [(x + 1, y - 1), (x, y - 1), (x + 1, y)]

        elif x == 9 and y == 0:
            return [(x - 1, y + 1), (x, y + 1), (x - 1, y)]

        elif x == 9:
            return [(x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1)]

        elif x == 0:
            return [(x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1)]

        elif y == 0:
            return [(x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y), (x + 1, y + 1)]

        elif y == 9:
            return [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y), (x + 1, y - 1)]

        else:
            return \
                [(x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x + 1, y), (x - 1, y + 1), (x - 1, y),
                 (x - 1, y - 1)]

    def bombs_around(self, table: list, x, y):
        around = self.poles_around(x, y)
        bombs = []

        for i in around:
            if table[i[0]][i[1]] == 'B' or table[i[0]][i[1]] == 'F':
                bombs.append(i)

        return bombs

    def make_field(self, x, y):
        around_first = self.poles_around(x, y)
        while len(self.bombs_coordinates) != 10:
            bomb_x = randrange(0, 10)
            bomb_y = randrange(0, 10)
            if (bomb_x != x and bomb_y != y) and (bomb_x, bomb_y) not in around_first and (
                    bomb_x, bomb_y) not in self.bombs_coordinates:
                self.field[bomb_x][bomb_y] = 'B'
                self.bombs_coordinates.append((bomb_x, bomb_y))
                self.flags_col += 1

        self.field[x][y] = '0'

        for i in range(10):
            for j in range(10):
                if self.field[i][j] != 'B':
                    self.field[i][j] = str(len(self.bombs_around(self.field, i, j)))
        self.moves += 1

        self.player_field[x][y] = '0'
        for i in around_first:
            self.dig(i[0], i[1])

    def dig(self, x, y):
        self.player_field[x][y] = self.field[x][y]

    def put_flag(self, x, y):
        if not self.player_field[x][y]:
            self.player_field[x][y] = 'F'
            self.flags_col -= 1
            self.flags_coordinates.append((x, y))

    def remove_flag(self, x, y):
        if self.player_field[x][y] == 'F':
            self.player_field[x][y] = ''
            self.flags_col += 1
            self.flags_coordinates.remove((x, y))

    def check(self, x, y):
        bombs = self.bombs_around(self.field, x, y)
        flags = self.bombs_around(self.player_field, x, y)
        if self.player_field[x][y] == '0' and len(flags):
            return None

        if len(flags) < int(self.player_field[x][y]):
            return None

        if len(flags) > len(bombs):
            self.lose()
            return False

        for i in range(len(bombs)):
            if bombs[i] != flags[i]:
                self.lose()
                return False
        return True

    def make_check(self, x, y):
        for x, y in self.poles_around(x, y):
            if self.player_field[x][y] != 'F':
                self.player_field[x][y] = self.field[x][y]

    def win_or_lose(self):
        for i in self.player_field:
            if 'B' in i:
                self.lose()
                return False
        if len(set(self.flags_coordinates) & set(self.bombs_coordinates)) == len(self.bombs_coordinates):
            return True
        return None

    def pretty_field_print(self, table: list):
        for i in range(10):
            print(
                f'{table[0][i]}|{table[1][i]}|{table[2][i]}|{table[3][i]}|{table[4][i]}|{table[5][i]}|{table[6][i]}|'
                f'{table[7][i]}|{table[8][i]}|{table[9][i]}')

    def lose(self):
        for x, y in self.bombs_coordinates:
            if self.player_field != 'F' and (x, y) not in self.flags_coordinates:
                self.player_field[x][y] = 'B'


if __name__ == '__main__':
    s = Sweeper()
    s.make_field(4, 4)
    s.pretty_field_print(s.field)
