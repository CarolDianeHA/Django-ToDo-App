# Capstone Project - ToDo

## Description

This is the final project for the course CS50’s Web Programming with Python and JavaScript. It is built using Django, HTML, CSS, JavaScript, Python, and Bootstrap.

The main concept of the application is to allow users to create a list of pending and completed tasks. Users have the option to edit, delete, and mark tasks as completed or incomplete. After registering and logging into the application, users have the opportunity to manage their tasks efficiently.

This web application offers the following features:

**Navigation Bar Options:**

* Before Login:
    * Login:
        * Users can log in using their username and password.
        * Displays error messages if the username or password is incorrect.
    * Register:
        * Users can register with a username, email, password, and password confirmation.
        * Displays error messages if the username is already taken or if the password confirmation does not match the password.

* After Login:
    * Tasks: View and manage pending tasks.
    * Completed Tasks: View tasks that have been marked as completed.
    * Logout: Log out of the application.

**Task Management:**
* `Record Tasks`: Users can add new tasks.
* `Mark Tasks as Finished`: This action moves the task to the Completed Tasks page.
* `Edit Tasks`: Users can modify existing tasks.
* `Delete Tasks`: Users can remove tasks.

This web application is mobile responsive, ensuring a seamless experience on various devices.

The primary objective of developing this application is to create a comprehensive and centralized platform for task management. By consolidating all pending tasks in one place, the application aims to enhance users’ organizational skills and boost their overall efficiency. Users can easily add, edit, delete, and mark tasks as completed or incomplete, ensuring they stay on top of their responsibilities. Additionally, the application supports user registration and login, providing a personalized and secure experience for each user.

## Distinctiveness and Complexity

I believe my project meets the distinctiveness and complexity requirements because it is fundamentally different from the other course projects. Throughout the course, we developed:

* A Google search clone
* A Wikipedia-like project that allows users to create and edit articles using a markdown system
* A bid auction website
* A mail application
* A network application similar to Twitter, where users can create, like, and edit posts, as well as follow and unfollow others

In contrast, my project offers a unique centralized platform for task management, which is not covered by any of the aforementioned projects. Regarding complexity, my project leverages Django for the backend and HTML, CSS, JavaScript for the frontend. Additionally, it is mobile responsive.

## Technical Details

This web application was developed using the following technology:

* `Django version 5.0.3`
* Backend: `Python`, `SQLite`
* Front End: `HTML`, `CSS`, `JavaScript`
* Tu run the project, locate in the root folder and use the following command:
```
python manage.py runserver
```
or
```
python3 manage.py runserver
```

## Application Screenshots

### Web Application Pages

* Login Page

Users have the opportunity to log in to the application using their username and password.

![Login Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/00Web-LoginPage.png)

* Register Page

Users can register for the application by providing a username, email address, and setting up a password.

![Register Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/01Web-RegisterPage.png)

* Tasks Page

On the tasks page, users can create new tasks, view all their pending tasks, as well as edit, delete, and mark them as completed.

![Tasks Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/02Web-Pending%20TasksPage.png)

* Completed Tasks Page

On the completed tasks page, users can view all their completed tasks. They can also mark tasks as incomplete or delete them.

![Completed Tasks Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/03Web-CompletedTasksPage.png)

### Mobile Application Pages

In the mobile version, users have the same functionalities as in the web version. The only difference is the appearance of the navigation bar.

* Loging Page

![Login Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/04Mobile-LoginPage.png)

* Register Page

![Register Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/05Mobile-RegisterPage.png)

* Tasks Page

![Tasks Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/06Mobile-PendingTasksPage.png)

* Completed Tasks Page

![Completed Tasks Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/07Mobile-CompletedTasksPage.png)

## Application Demo Video

[Visit YouTube Link here!!](https://youtu.be/aTuUTbH0rmM)

## Authors

* Carol Diane Hernández |   <img alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" /> [GitHub](https://github.com/CarolDianeHA) |