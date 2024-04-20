from database import initialize_database, get_all_disciplines, add_discipline, update_discipline_status, \
    get_approved_disciplines, get_pending_disciplines
from utils import calculate_percentage


def display_menu():
    print("Menu:")
    print("1. Add a new discipline")
    print("2. Update discipline status")
    print("3. View all disciplines")
    print("4. View approved disciplines")
    print("5. View pending disciplines")
    print("6. Add a list of disciplines")
    print("7. Percentage of approved / pending disciplines")
    print("8. Exit")


def add_disciplines_from_list(session):
    discipline_list = input("Enter the list of disciplines and statuses (name:status, separated by comma): ")
    disciplines = discipline_list.split(',')
    for item in disciplines:
        name_status = item.strip().split(':')
        name = name_status[0].strip().upper()
        status = name_status[1].strip().upper() if len(name_status) > 1 else 'PENDENTE'
        add_discipline(session, name, status)


def main():
    session = initialize_database()

    disciplines = get_all_disciplines(session)
    pending_disciplines = get_pending_disciplines(session)
    approved_disciplines = get_approved_disciplines(session)

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the discipline: ")
            status = input("Enter the status of the discipline: ")
            add_discipline(session, name, status)
        elif choice == '2':
            discipline_id = input("Enter the ID of the discipline you want to update: ")
            status = input("Enter the new status of the discipline: ")
            update_discipline_status(session, discipline_id, status)
        elif choice == '3':
            print("All disciplines:")
            for index, discipline in enumerate(disciplines, start=1):
                print(f'{index}: {discipline}')
        elif choice == '4':
            print("Approved disciplines:")
            for index, discipline in enumerate(approved_disciplines, start=1):
                print(f'{index}: {discipline}')
        elif choice == '5':
            print("Pending disciplines:")
            for index, discipline in enumerate(pending_disciplines, start=1):
                print(f'{index}: {discipline}')
        elif choice == '6':
            add_disciplines_from_list(session)
        elif choice == '7':
            total_disciplines = len(disciplines)
            approved_per = calculate_percentage(len(approved_disciplines), total_disciplines)
            pending_per = calculate_percentage(len(pending_disciplines), total_disciplines)
            print(f'Percentage of approved disciplines is: {approved_per} and pending is: {pending_per}')
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
