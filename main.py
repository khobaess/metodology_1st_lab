from games.lcm import play_lcm
from games.progression import play_progression


def main():
    games = {
        "1": ("LCM Game", play_lcm),
        "2": ("Geometric Progression", play_progression),
    }

    print("Choose a game:")
    for key, (name, _) in games.items():
        print(f"{key} - {name}")

    choice = input("Enter choice: ")

    if choice in games:
        _, game_function = games[choice]
        game_function()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
