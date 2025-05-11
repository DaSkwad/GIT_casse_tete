from utils import add_numbers
from data_loader import load_data

def main():
    data = load_data()
    result = add_numbers(2, 3)
    print(f"Result: {result}")
    print(f"Data loaded: {data}")

if __name__ == "__main__":
    main()