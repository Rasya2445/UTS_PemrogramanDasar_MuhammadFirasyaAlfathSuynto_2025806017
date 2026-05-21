from game import play_game
from scoreboard import save_score, show_top5

def main():
    print("===== GUESS BATTLE =====")

    name = input("Masukkan nama pemain: ")

    total_score = 0

    for level in range(1, 4):
        score = play_game(level)
        total_score += score

        if score == 0:
            print("Anda gagal pada level ini.")
            break

    print(f"\nTotal skor {name}: {total_score}")

    save_score(name, total_score)
    show_top5()

if __name__ == "__main__":
    main()