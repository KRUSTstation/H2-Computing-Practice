import random

class Player:
    def __init__(self, nickname):
        self.name = str(nickname)
        self.start_loc = (0, 0)
        self.curr_loc = self.start_loc
        self.score = 0
        self.turns_taken = 0
        self.has_shield = False

    def update_score(self, points):
        self.score += points

    def reset_loc(self):
        self.curr_loc = self.start_loc

    def status(self):
        row, col = self.curr_loc
        return f"At ({row}, {col}) | Score: {self.score} | Turns: {self.turns_taken} | Shield: {self.has_shield}"

    def move(self, direction):
        direction = direction.upper()
        row, col = self.curr_loc

        if direction == "UP":
            new_loc = (row - 1, col)
        elif direction == "DOWN":
            new_loc = (row + 1, col)
        elif direction == "LEFT":
            new_loc = (row, col - 1)
        elif direction == "RIGHT":
            new_loc = (row, col + 1)
        else:
            return False

        # Validate grid boundaries (5x5 grid: indices 0 to 4)
        if 0 <= new_loc[0] <= 4 and 0 <= new_loc[1] <= 4:
            self.curr_loc = new_loc
            return True
        else:
            return False


class GridObj:
    def __init__(self, row, col):
        self.location = (row, col)


class Energiser(GridObj):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.symbol = 'E'

    def effect(self, player):
        player.update_score(10)


class Shield(GridObj):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.symbol = 'S'

    def effect(self, player):
        player.has_shield = True


class Toxin(GridObj):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.symbol = 'T'

    def effect(self, player):
        if player.has_shield:
            player.has_shield = False
        else:
            player.update_score(-5)


class Trap(GridObj):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.symbol = 'X'

    def effect(self, player):
        player.reset_loc()

class Game:
    GRID_SIZE = 5

    def __init__(self, nickname):
        self.player = Player(nickname)
        self.items = []
        self.max_turns = 8

    def generate_items(self):
        # Create all possible locations except start_loc (0,0)
        available_locations = [
            (r, c) for r in range(self.GRID_SIZE) for c in range(self.GRID_SIZE) if (r, c) != (0, 0)
        ]

        # Randomly select 6 locations
        chosen_locations = random.sample(available_locations, 6)

        # Quantities: 2 Energisers, 1 Shield, 2 Toxins, 1 Trap
        self.items.append(Energiser(*chosen_locations[0]))
        self.items.append(Energiser(*chosen_locations[1]))
        self.items.append(Shield(*chosen_locations[2]))
        self.items.append(Toxin(*chosen_locations[3]))
        self.items.append(Toxin(*chosen_locations[4]))
        self.items.append(Trap(*chosen_locations[5]))

    def process_move(self, direction):
        if self.player.move(direction):
            self.player.turns_taken += 1

            # Check if any item is at the player's new location
            for item in list(self.items):
                if item.location == self.player.curr_loc:
                    item.effect(self.player)
                    self.items.remove(item)
                    break

            return True
        else:
            print("Invalid move made.")
            return False