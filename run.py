from persistence.database import init_db

def main():
    init_db()
    while True:
        try:
            command = input("# ").strip()
            if not command:
                continue
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
