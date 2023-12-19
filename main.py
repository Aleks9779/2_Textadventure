class Game:
    MAX_ATTEMPTS = 3  # Statisches Attribut

    def __init__(self):
        self.current_room = None

    def start_game(self):
        # Spiellogik hier
        pass

def main():
    game = Game()
    game.start_game()

if __name__ == "__main__":
    main()
