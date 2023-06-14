Welcome to the PUMP IT! Gym Management Application.

This is a Flask development server that provides a simply UI allowing a gym to manage classes and members.

This will access a database using postgresql. To activate everything, the database should be initiated in terminal as follows:
1. Navigate to the root folder of the application;
2. type 'createdb gym' to create a database on your system;
3. type 'psql -d gym -f db/gym.sql' to instantiate the tables in your database;
4. type 'flask run' to run the development server.

The app can be accessed by default at localhost:4999.


The home page is responsible for HYPE! Upon reading this each morning, users will be PUMPED and prepared for a day of gym management.

A nav bar to the left of the header title provides links to the home page for further PUMP or to index pages with lists of all members or classes.

The nav bar to the right of the header title provides links to basic functions that might be required most often, i.e. registering a customer for a class, adding a new members, or adding a new class to the respective databases.

The members index lists all members and their details, sorted by ID number. Each member "box" contains:
1. a link to a page showing all classes that member is registered to;
2. A link to an edit page where member details can be updated;
3. A delete button that will remove the member from the database.

The member's classes page contains a list of all classes registered and a dropdown menu to register for any more classes. Members can currently register multiple times for a single class, but duplicates can be manually deleted using the button provided.

The member edit page allows all attributes of a member to be amended. Existing values are input by default.

The class index has the same format as members, except inactive or past classes are visible as a separate list (allowing them to be reactivated or rescheduled). The app will detect whether a class is active and scheduled on today's date or later and move it to the active list.

'Show registered members' links to a page that shows all members registered to a specific class.


