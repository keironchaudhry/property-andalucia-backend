# **Property Andalucia API**

Property Andalucia is a web application made for the advertisement of properties around Andalucia, Southern Spain. It is a space in which users can advertise and sell their property listing, as well as allowing users to register as buyers only.

This repository contains the API part of the project, created using Python and the Django REST Framework and used to contain and store data, and authentication functionality to the frontend part of the project. 

API Deployment can be found [here](https://property-andalucia-backend.herokuapp.com/).

Frontend Deployment can be found [here](https://property-andalucia-frontend.herokuapp.com/).

Frontend Repository can be found [here](https://github.com/keironchaudhry/property-andalucia-frontend).


## **Table of content**

* [User Stories](#user-stories)
* [Database](#database)
* [Testing](#testing)
* [Bugs](#bugs)
    * [Fixed Bugs](#fixed-bugs)
    * [Remaining Bugs](#remaining-bugs)
* [Technologies and libraries used](#technologies-and-libraries-used)
    * [Languages](#languages)
    * [Database Platform and Cloud Storage](#database-platform-and-cloud-storage)
    * [Libraries and other resources](#libraries-and-other-resources)
* [Development and Deployment](#development-and-deployment)
    * [Local Deployment](#local-deployment)
    * [Deployment to Heroku](#deployment-to-heroku)
* [Credits](#credits)
    * [Code](#code)
    * [Acknowledgments](#acknowledgments)


# **User Stories**

User Stories for the Frontend project can be found [here](https://github.com/keironchaudhry/property-andalucia-frontend/issues?q=is%3Aissue+is%3Aclosed). In coordination with these stories, tasks were developed to carry out the API work needed to support and sustain the principal user stories.

Therefore the tasks developed for the creation of the project API were made as issues and linked to the projects Kanban board which can be accessed [here](https://github.com/keironchaudhry/property-andalucia-backend/issues?q=is%3Aissue+is%3Aclosed).

# **Database**

* The project uses a relational database (PostgreSQL)

* The following diagram represents the relational database model design for this web application. It was made using Quick Database Diagrams:

![database-diagram](/documents/images/updated%20database%20diagram%20.png)

* **User**
    * The User model contains information about each user that registers an account
    * It is part of the Django allauth library
    * It contains a custom field called *seller_status* which was made using the AbstractUser feature. This additional field was added to be able to distinguish between regular profiles and profiles that sell property
    * The fields used for this project are: *username*, *email*, *password*, *seller_status*

* **Save**
    * The Save model contains information about which property has been saved by which user.
    * All authenticated users are able to interact with the save model, allowing them to save a property which creates a relational link between the save id, the owner and the property.
    * Users not authenticated or first-time visitors are unable to interact with the save model.
    * The model contains the following fields: *save_id*, *owner*, *property*, *created_at*.

* **Notes**
    * The Notes model contains information about which property a private note has been left by which user.
    * All authenticated users are able to interact with the notes model, allowing them to leave written content on a property object.
    * A relational link is created between the note id, the owner and the property.
    * Users not authenticated or first-time visitors are unable to interact with the note model.
    * Notes are private and cannot be seen by other users.
    * The model contains the following fields: *note_id*, *owner*, *property*, *created_at*, *updated_at*, *content*.

* **Followers**
    * The Followers model contains information about which user profile is being followed by which user.
    * All authenticated users are able to interact with the followers model, allowing them to follow a profile.
    * A relational link is created between the follower id, the owner and the followed profile.
    * Users not authenticated or first-time visitors are unable to interact with the follow model.
    * All users and authenticated users are able to view the following and followed count of a profile.
    * The model contains the following fields: *follower_id*, *owner*, *followed*, *created_at*.

* **Profile**
    * The Profile model is used to store information regarding any registered user
    * A profile object is created upon creating an account
    * A relational link is created between the profile id and the owner
    * Users can modify profile information at any time
    * Contains the following fields: *profile_id*, *owner*, *name*, *bio*, *email*, *telephone*, *image*, *created_at*, *updated_at*.

 * **Property**
    * The Property model is used to store information regarding any property object created by an authenticated user.
    * The property object is intended to be created only by users who are sellers, which is reflected on the frontend application depending on the *seller_status* boolean field of the current user.
    * A relational link is created between the property id, the owner, the save id and the note id.
    * Contains the following fields: *property_id*, *owner*, *property_type*, *province*, *street*, *municipality*, *post_code*, *price*, *size*, *bedroom_count*, *bathrooms_count*, *garage*, *garden*, *is_south_facing*, *description*, *image*, *sold*, *latitude*, *longitude*,*created_at*, *updated_at*.


# **Testing**

Separate documentation for testing can be found [here](/documents/testing.md).

# **Bugs**

## **Fixed bugs**

All bugs encountered and fixed during the development process can be found [here](https://github.com/keironchaudhry/property-andalucia-backend/pulls?q=is%3Apr+label%3Abug+is%3Aclosed).

Bugs across the entire Property Andalucia were generally from the API section portion of the subject, such as improper data field implementation that needed correcting or irregular permissions. These sort of errors impeded data requests and as such drew the attention of these irregularities.

## **Remaining bugs**

There are currently no known bugs.

# **Technologies and libraries used**

## **Languages**

The languages used are:

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)

## **Database Platform and Cloud Storage**

* [ElephantSQL Postgres](https://www.elephantsql.com/): SQL database service provided by ElephantSQL for data storage.
* [SQLite](https://www.sqlite.org/index.html): SQL database engine used by default as part of Django Framework and used during development.
* [Cloudinary](https://cloudinary.com/home-102622): to store images and static files.
* [Heroku](https://id.heroku.com/login): to deploy and run the application.

## **Libraries and other resources**

This project contains the following resources:

* [Django](https://www.djangoproject.com/): Python-based framework for rapid website development.
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html): used for user account registration and user authentication.
* [Django Cloudinary Storage](https://djangopackages.org/packages/p/django-cloudinary-storage/): provides Cloudinary storages for both media and static files
* [Django Base URL](https://pypi.org/project/dj-database-url/0.5.0/): for the use of 'DATABASE_URL' environmental variable in the Django project settings file to connect to a PostgreSQL database.
* [Django Filter](https://django-filter.readthedocs.io/en/stable/): allows users to filter down a queryset based on a models particular field.
* [Django REST Framework simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/): provides a JSON Web Token authentication backend for the Django REST Framework.
* [Django CORS Headers](https://pypi.org/project/django-cors-headers/): adds Cross-Origin Resource Sharing (CORS) headers to responses.
* [Pillow](https://pillow.readthedocs.io/en/stable/installation.html): Python Imaging Library which contains all the basic image processing functionality.
* [psycopg2](https://pypi.org/project/psycopg2/): Python PostgreSQL database adapter.
* [Gunicorn](https://gunicorn.org/): Python WSGI HTTP Server.
* [Coverage.py](https://coverage.readthedocs.io/en/6.3.2/): used for coverage testing of Python programs. 
* [PEP8 Validation](http://pep8online.com/): used to validate Python code syntax.
* [Quick Database Diagrams](https://www.quickdatabasediagrams.com/): used to create the database model chart.
* [GitHub](https://github.com/): used to store, develop and maintain project code.


# **Development and deployment**

The development environment used for this project was GitPod. Regular commits, pushes and merges to 'main' branch in GitHub via a 'development' branch were employed to be able to track and trace the development process of the website. All merges have been linked to their corresponding issues. The Gitpod environment for this particular project was created using a template provided by Code Institute.

For local deployments instructions shall be written below, along with instructions with deployment to Heroku, the hosting service used to deploy this particular website. Heroku was chosen as the hosting service due to its database maintenance capabilities. 

## **Local Deployment**

This repository can be cloned and run locally with the following steps:

1. Login to [GitHub](https://www.github.com).
2. Select repository named: [keironchaudhry/property-andalucia-backend](https://github.com/keironchaudhry/property-andalucia-backend).
3. Click code toggle button and copy the url (i.e., https://github.com/keironchaudhry/property-andalucia-backend.git).
4. In your IDE, open terminal and run the git clone command (i.e., `git clone https://github.com/keironchaudhry/property-andalucia-backend.git`).
5. The repository will now be cloned in your workspace.
6. Create an [env.py file](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1) (this file should normally be included in .gitignore, therefore it'll not be committed publicly in the root folder of your project) and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values. For example:

`import os`

`os.environ['SECRET_KEY'] = 'ADDED_BY_YOU'`

`os.environ['DATABASE_URL'] = 'ADDED_BY_YOU'`

`os.environ['CLOUDINARY_URL'] = 'ADDED_BY_YOU'`

7. Install the relevant packages as per the requirements.txt file
8. In `settings.py` file, ensure the connection is set to either the Heroku Postgres Database or the local SQLite database
9. Ensure debug is set to true in the `settings.py` file for local development
10. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in `settings.py`
11. Run `python3 manage.py showmigrations` to check the status of the migrations
12. Run `python3 manage.py migrate` to migrate the database
13. Run `python3 manage.py createsuperuser` to create a super/admin user
14. Start the application by running `python3 manage.py runserver`

## **Deployment to Heroku**

Deployment to Heroku can be done with the following guideline:

1. Create an account on Heroku
2. Create an app and give it the desired name and select a region
3. Create an account on ElephantSQL.
4. Click on 'Create an instance'
5. Give your plan a Name, select the appropriate Plan and then select a region and data-center closest to your location.
6. Once details are completed, click 'Create instance'. 
7. Copy and paste dashboard `DATABASE_URL` and copy and paste into Heroku Config Vars in Settings, and be sure to set your `env.py` in your project IDE to the same URL. 
8. The `DATABASE_URL` needs to be set as an environment variable in both Heroku and in the IDE local environment variables
9. Create a `Procfile` with the following text: `web: gunicorn project_name.wsgi`
10. Make sure you add your environment variables (env.py) to Heroku's Config Vars
11. Ensure `Debug` is set to `False` in the settings.py file
12. Add 'localhost', and 'project_name.herokuapp.com' to the `ALLOWED_HOSTS` variable in `settings.py`
13. Run `python3 manage.py showmigrations` to check the status of the migrations
14. Run `python3 manage.py migrate` to migrate any necessary data to the database
15. Run `python3 manage.py createsuperuser` to create an admin user
16. Connect the app to GitHub, and enable automatic deploys from main (or you can manually deploy).
17. Click 'deploy' to deploy your application to Heroku for the first time


# **Credits**

## **Code**

The following websites proved to be both insightful and helpful during development of this project:

* [Django REST Framework documentation](https://www.django-rest-framework.org/)
* [Stack Overflow](https://stackoverflow.com/)
* [GeeksForGeeks](https://www.geeksforgeeks.org/)
* [YouTube](https://www.youtube.com/)

# **Acknowledgments**

For inspiration, guidance and inputs, thank you to:

* Sandeep Aggarwal

    Absolutely fantastic mentor at Code Institute with brilliant insight into Full Stack Software Development and programmatic skills.
    
* Jack Crymble

    Friend and guide, thank you for your knowledge and insight!

* Jody Murray

    Fellow student and colleague, thank you for your input and constant support!
