from database import initialize_database, find_discipline_by_word, add_or_update_discipline, \
    get_disciplines_by_status, finish_semester
from status import Status
from utils import calculate_percentage


def display_menu():
    print("""
    Menu:
    1. Add a new discipline
    2. Update discipline status
    3. View all disciplines
    4. View approved disciplines
    5. View pending disciplines
    6. Add a list of disciplines
    7. Percentage of approved / pending disciplines
    8. Find discipline by word
    9. Finish Semester
    10. Exit
    """)


def display_disciplines(disciplines, title):
    print(f"{title}:")
    for index, discipline in enumerate(disciplines, start=1):
        print(f'{index}: {discipline}')


def add_disciplines_from_list(session):
    discipline_list = input("Enter the list of disciplines and statuses (name:status, separated by comma): ")
    disciplines = discipline_list.split(',')
    for item in disciplines:
        name_status = item.strip().split(':')
        name = name_status[0].strip().upper()
        status = name_status[1].strip().upper() if len(name_status) > 1 else 'PENDENTE'
        add_or_update_discipline(session, name, status)


if __name__ == "__main__":
    session = initialize_database()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        choices = {
            '1': lambda: add_or_update_discipline(session, input("Enter the name of the discipline: "),
                                                  input("Enter the status of the discipline: ")),
            '2': lambda: add_or_update_discipline(session, input("Enter the name of the discipline you want to update: "),
                                                  input("Enter the new status of the discipline: ")),
            '3': lambda: display_disciplines(get_disciplines_by_status(session, 'ALL'), "All disciplines"),
            '4': lambda: display_disciplines(get_disciplines_by_status(session, 'APROVADO'), "Approved disciplines"),
            '5': lambda: display_disciplines(get_disciplines_by_status(session, 'PENDENTE'), "Pending disciplines"),
            '6': lambda: add_disciplines_from_list(session),
            '7': lambda: print(
                f'''Percentage of approved disciplines is: 
                {calculate_percentage(len(get_disciplines_by_status(session, Status.APROVADO)),
                                      len(get_disciplines_by_status(session, "ALL")))} 
                                      and pending is: {calculate_percentage(
                                      len(get_disciplines_by_status(session, Status.PENDENTE)), 
                                      len(get_disciplines_by_status(session, "ALL")))}'''),
            '8': lambda: (
                word := input("Enter the word to search for: "),
                display_disciplines(find_discipline_by_word(session, word),
                                    f"Disciplines containing {word}")
            ),
            '9': lambda: finish_semester(session, input("Enter the semester you finished:")),
            '10': lambda: exit()
        }

        if choice in choices:
            choices[choice]()
        else:
            print("Invalid choice. Please try again.")
