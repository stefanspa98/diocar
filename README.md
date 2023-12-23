**People Data Management Web App**

This Python Django web application serves as a platform for managing a database of people. It provides functionalities such as searching, adding, editing, and deleting individual records within the database. The database schema includes fields for First Name, Last Name, and Passport ID.

**Features**

- **Search:** Users can search for specific individuals within the database using the search bar. The search functionality is designed to accept any input provided by the user.
- **Add New Person:** Users have the capability to add new individuals to the database. They can input the First Name, Last Name, and Passport ID for the new entry.
- **Edit Record:** Every record in the database can be modified. Users can edit the First Name, Last Name, and Passport ID fields for any person in the database.
- **Delete Record:** Individual records can be deleted from the database.

**Installation**

1. Clone this repository: `git clone https://github.com/stefanspa98/diocar.git`
2. Run migrations: `python manage.py migrate`
3. Start the development server: `python manage.py runserver`
