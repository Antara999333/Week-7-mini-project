from . import database

def main():
    print("Run the tool!")

    database.create_tables()
    database.insert_sample_data()

    print("Operation completed!")

if __name__ == '__main__':
    main()