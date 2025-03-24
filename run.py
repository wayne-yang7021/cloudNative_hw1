from presentation.command_processor import CommandProcessor
from persistence.database import init_db

def main():
    processor = CommandProcessor()
    init_db()
    while True:
        try:
            command = input("# ").strip()
            if not command:
                continue
            result = processor.process_command(command)
            print(result)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
