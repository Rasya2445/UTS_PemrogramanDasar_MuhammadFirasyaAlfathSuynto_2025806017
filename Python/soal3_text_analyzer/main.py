from analyzer import analyze_text


def main():
    try:
        analyze_text("input.txt", "report.txt")
    except FileNotFoundError:
        print("File input.txt tidak ditemukan.")
    except Exception as e:
        print("Terjadi error:", e)


if __name__ == "__main__":
    main()