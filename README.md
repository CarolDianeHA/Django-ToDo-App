# ToDo Application


## Overview

ToDo Application is a Django-based web application designed to help users manage their tasks efficiently. It provides features for creating, updating, and deleting tasks, as well as tracking task completion.

## Distinctiveness and Complexity

I believe my project meets the distinctiveness and complexity requirements because it is fundamentally different from the other course projects. Throughout the course, we developed:

* A Google search clone
* A Wikipedia-like project that allows users to create and edit articles using a markdown system
* A bid auction website
* A mail application
* A network application similar to Twitter, where users can create, like, and edit posts, as well as follow and unfollow others

In contrast, this project stands out due to its comprehensive task management features, including user authentication, task categorization, and a responsive design. The complexity is evident in the integration of Django’s authentication system, and the use of class-based views.

## Features

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


## Code overview
The project was developed using Python and the Django framework, leveraging SQLite as the database. The front-end was crafted with HTML, enhanced by Bootstrap and CSS for styling. JavaScript was employed to enable the functionality for editing tasks.

### File Contributions

|File|Content|
|:---|:------|
|`settings.py`|Contribute project settings, include database setup and installed apps.|
|`urls.py`|Defines the URL patterns for the application.|
|`views.py`|Implemented class-based views for handling task operations.|
|`models.py`|Created models for tasks and categories.|
|`templates/`|Designed HTML templates for the different pages.|
|`static/`|Added CSS file for styling and interactivity.|

### Application File Structure

The VSCode File Tree Generator shows the following file structure:

```
todo
┣ 📂__pycache__
┃ 
┣ 📂migrations
┃ 
┣ 📂static
┃ ┣ 📂images
┃ ┃ ┣ 📜00Web-LoginPage.png
┃ ┃ ┣ 📜01Web-RegisterPage.png
┃ ┃ ┣ 📜02Web-Pending TasksPage.png
┃ ┃ ┣ 📜03Web-CompletedTasksPage.png
┃ ┃ ┣ 📜04Mobile-LoginPage.png
┃ ┃ ┣ 📜05Mobile-RegisterPage.png
┃ ┃ ┣ 📜06Mobile-PendingTasksPage.png
┃ ┃ ┣ 📜07Mobile-CompletedTasksPage.png
┃ ┃ ┗ 📜favicon.ico
┃ ┣ 📂todo
┃ ┃ ┣ 📜.DS_Store
┃ ┃ ┗ 📜styles.css
┃ ┗ 📜.DS_Store
┣ 📂templates
┃ ┗ 📂todo
┃   ┣ 📜completed_tasks.html
┃   ┣ 📜layout.html
┃   ┣ 📜login.html
┃   ┣ 📜register.html
┃   ┗ 📜todo.html
┣ 📜__init__.py
┣ 📜.DS_Store
┣ 📜admin.py
┣ 📜apps.py
┣ 📜models.py
┣ 📜tests.py
┣ 📜urls.py
┗ 📜views.py

```

### Project File Structure

```
tools
┣ 📂__pycache__
┃ 
┣ 📜__init__.py
┣ 📜.DS_Store
┣ 📜asgi.py
┣ 📜settings.py
┣ 📜urls.py
┗ 📜wsgi.py

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

| Loging Page |
|:-----------:|
|![Login Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/04Mobile-LoginPage.png)|

| Register Page |
|:-------------:|
|![Register Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/05Mobile-RegisterPage.png)|

| Tasks Page |
|:----------:|
|![Tasks Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/06Mobile-PendingTasksPage.png)|

| Completed Tasks Page |
|:--------------------:|
|![Completed Tasks Page](https://github.com/CarolDianeHA/Django-ToDo-App/blob/main/todo/static/images/07Mobile-CompletedTasksPage.png)|

## Application Demo Video

[Visit YouTube Link here!!](https://youtu.be/aTuUTbH0rmM)

## Installation

1. Clone the repository:
```
git clone git@github.com:CarolDianeHA/Django-ToDo-App.git
```
2. Recommended: Create a virtual environment, for more information use this [link](https://www.w3schools.com/django/django_create_virtual_environment.php)

Windows:
```
py -m venv env
```
Unix/MacOS:
```
python3 -m venv env
```
This will set up a virtual environment, and create a folder named "env" with subfolders and files, like this: 
```
env
  bin(linux/MacOS)
  include
  lib
  script(Windows)
  pyvenv.cfg
```

* Activate the environment:

Windows:
```
env\Script\activate.bat
```

Linux/MacOS:
```
source env/bin/activate
```
Once the environment is actived, you will see this result in the command prompt:

Windows:
`(env) C:\Users\Your Name>`

Linux/MacOS:
`(env) ... $`

3. Install dependencies:
```
pip install -r requirements.txt
```
If you make changes to the project, you can always update the requirements with this command:
```
pip freeze > requirements.txt
```

4. Run the migration
```
python manage.py makemigrations
```

5. Run the migrate
```
python manage.py migrate
```

6. Create the Super User
```
python manage.py createsuperuser
```

7. Run the server
```
python manage.py runserver
```

## Authors

* Carol Diane Hernández |   <img alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" /> [GitHub](https://github.com/CarolDianeHA) |