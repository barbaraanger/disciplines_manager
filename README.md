# Disciplines Manager

This is a simple Python application for managing disciplines. It allows users to add new disciplines, update their status, and view all disciplines or filter them by status.

## Features

1. **Add a New Discipline:** Add a new discipline to the database with its name and status.
2. **Update Discipline Status:** Update the status of an existing discipline.
3. **View All Disciplines:** Display all disciplines currently stored in the database.
4. **View Approved Disciplines:** Filter and display only the disciplines with an 'APROVADO' status.
5. **View Pending Disciplines:** Filter and display only the disciplines with a 'PENDENTE' status.
6. **Add a List of Disciplines:** Add multiple disciplines at once by providing a list of names and statuses.
7. **Percentage of Approved/Pending Disciplines:** Calculate and display the percentage of approved and pending disciplines.

## Code Structure

- **`initialize_database()`**: Initialize the database session and create necessary tables.
- **`add_discipline(session, name, status)`**: Add a new discipline to the database or update an existing one.
- **`update_discipline_status(session, discipline_id, new_status)`**: Update the status of a discipline by its ID.
- **`get_all_disciplines(session)`**: Retrieve all disciplines from the database.
- **`get_approved_disciplines(session)`**: Retrieve only approved disciplines from the database.
- **`get_pending_disciplines(session)`**: Retrieve only pending disciplines from the database.
- **`add_disciplines_from_list(session)`**: Helper function to add multiple disciplines from a comma-separated list.
- **`display_menu()`**: Display the main menu options for the user.
- **`main()`**: The main function that runs the application and handles user input.
- **`Status` Enum**: Define an enum for discipline statuses ('PENDENTE' and 'APROVADO').
- **`calculate_percentage(approved_count, total_count)`**: Calculate the percentage of approved and pending disciplines.

## Usage

1. Clone the repository.
2. Run the `main()` function to start the application.
3. Follow the on-screen prompts to interact with the application.

## Dependencies

- Python
- SQLAlchemy

## Note

This application uses an SQLite database (`disciplines-manager`) by default. You can change the database URI in the `initialize_database()` function to use a different database engine.

Feel free to contribute to this project and enhance its functionality!
