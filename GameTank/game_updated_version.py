import random

class Tank:
    def __init__(self):
        self.coord = [2, 2]
        self.direction = 'North'
        self.shot_count = 0
        self.shot_direction = {'North': 0, 'East': 0, 'South': 0, 'West': 0}
        self.target = self.generate_target()
        self.positions = []
        self.score = 100
        self.destroyed_targets = 0
        print(f"Bravo Six, where are we going? ➡️ x[{self.target[0]}] y[{self.target[1]}]")
        print(f'You are here ➡️ x[{self.coord[0]}] y[{self.coord[1]}]')
        self.print_grid()

    def generate_target(self):
        return [random.randint(0, 4), random.randint(0, 4)]

    def move(self, new_direction):
        self.direction = new_direction
        self.positions.append(tuple(self.coord))
        if self.direction == 'North' and self.coord[1] > 0:
            self.coord[1] -= 1
        elif self.direction == 'East' and self.coord[0] < 4:
            self.coord[0] += 1
        elif self.direction == 'South' and self.coord[1] < 4:
            self.coord[1] += 1
        elif self.direction == 'West' and self.coord[0] > 0:
            self.coord[0] -= 1
        self.score -= 10
        self.print_grid()
        self.check_game_end()

    def shoot(self):
        self.shot_count += 1
        self.shot_direction[self.direction] += 1
        if self.check_shot():
            print("✅ Bullseye! New target:")
            self.destroyed_targets += 1
            self.score += 30
            self.target = self.generate_target()
            self.positions.clear()
        else:
            self.score -= -20
            print("He... he missed...!😦")
        self.print_grid()
        self.check_game_end()

    def check_shot(self):
        dx = self.target[0] - self.coord[0]
        dy = self.target[1] - self.coord[1]
        if self.direction == 'North' and dx == 0 and dy < 0:
            return True
        elif self.direction == 'South' and dx == 0 and dy > 0:
            return True
        elif self.direction == 'East' and dy == 0 and dx > 0:
            return True
        elif self.direction == 'West' and dy == 0 and dx < 0:
            return True
        return False

    def print_grid(self):
        grid = []
        for _ in range(5):
            row = []
            for _ in range(5):
                row.append('⬛')
            grid.append(row)
        grid[self.target[1]][self.target[0]] = '🎯'
        for x, y in self.positions:
            grid[y][x] = '◻️'
        grid[self.coord[1]][self.coord[0]] = '🚜'
        for line in grid:
            print(" ".join(line))
        print()

    def info(self):
        print(f"\n❤️ Life points: {self.score}")
        print(f"🧭 Tank direction: {self.direction}")
        print(f"🗺️ Tank coord x[{self.coord[0]}] y[{self.coord[1]}]")
        print(f"🗺️ Target coord x[{self.target[0]}] y[{self.target[1]}]")
        print(f"🎯 Hit targets: {self.destroyed_targets}")
        print(f"💥 Total shots count: {self.shot_count}")
        for direction, number in self.shot_direction.items():
            print(f"💥 Total shots to {direction}: {number}")
        self.print_grid()

    def check_game_end(self):
        if self.score <= 0:
            print("Game Over!☠️")
            print(f"🎯 Total destroyed targets: {self.destroyed_targets}")
            username = input("Enter your nickname: ")
            with open("high_scores.txt", "a") as file:
                file.write(f"{username}: {self.destroyed_targets}\n")
            print("Game result was recorded!✅")
            exit()

def menu():
    tank = Tank()
    while True:
        print("〰️〰️ MENU 〰️〰️")
        print("🎮 Controls:")
        print("🔼 Move UP     →  Press W")
        print("▶️ Move RIGHT  →  Press D")
        print("🔽 Move DOWN   →  Press S")
        print("◀️ Move LEFT   →  Press A")
        print("\n🎯 Actions:")
        print("🔥 SHOOT       →  Press E")
        print("ℹ️ INFO        →  Press F")
        print("🏆 Top Players →  Press T")
        print("🚪 Quit Game   →  Press Q")
        menu_option = input("\nPress a key to choose an action (W/A/S/D/E/F/T/Q): ")
        if menu_option.lower() == "w":
            tank.move('North')
        elif menu_option.lower() == "d":
            tank.move('East')
        elif menu_option.lower() == "s":
            tank.move('South')
        elif menu_option.lower() == "a":
            tank.move('West')
        elif menu_option.lower() == "e":
            tank.shoot()
        elif menu_option.lower() == "f":
            tank.info()
        elif menu_option.lower() == "t":
            try:
                with open("high_scores.txt", "r") as file:
                    print("\n〰️〰️ Top Results 〰️〰️")
                    print(file.read())
                    tank.print_grid()
            except FileNotFoundError:
                print("\n📃 No top players found!\n")
        elif menu_option == 'q':
            print("Fought bravely!🫡")
            print(f"🎯 Total destroyed targets: {tank.destroyed_targets}")
            username = input("Enter your nickname: ")
            with open("high_scores.txt", "a") as file:
                file.write(f"{username}: {tank.destroyed_targets}\n")
            print("Game result was recorded!✅")
            break
        else:
            print("⚠️ Wrong Input! Please try again...")

if __name__ == "__main__":
    menu()
