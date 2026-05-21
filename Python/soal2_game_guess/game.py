import random

def play_game(level):
    if level == 1:
        max_number = 10
        attempts = 3
    elif level == 2:
        max_number = 50
        attempts = 5
    elif level == 3:
        max_number = 100
        attempts = 7
    else:
        print("Level tidak valid!")
        return 0

    secret_number = random.randint(1, max_number)

    print(f"\n=== LEVEL {level} ===")
    print(f"Tebak angka antara 1 sampai {max_number}")
    print(f"Kesempatan: {attempts} kali")

    for i in range(attempts):
        try:
            guess = int(input(f"Tebakan ke-{i+1}: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if guess == secret_number:
            score = (attempts - i) * 10
            print(f"Benar! Angka yang dicari adalah {secret_number}")
            print(f"Skor Anda: {score}")
            return score
        elif guess < secret_number:
            print("Terlalu kecil!")
        else:
            print("Terlalu besar!")

    print(f"Game over! Angka yang benar adalah {secret_number}")
    return 0