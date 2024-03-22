

<img src="static/images/Calvin-Avoiding-1.jpg" >

# Title: Book Review Blog

## Overview:
- Foster a interest in reading highly recommended publications in relevant subject areas

## Features:

### Enable Followers to: 
- Access resources and services that promote mental and intellectual well-being. 


# Detailed Description

## User registration.
- User profiles: allow users to read reviews in areas of interest to them.


### 1. Technical Project Overview

Full Stack Web Development Hackathon: Application built using a Full Stack Django Framework.

Activities: Development using Django, Python, HTML, CSS and JavaScript, UX Design, and Agile Project Management.

Objectives:
- Use an Agile methodology to plan and design a Full-Stack Web application using an MVT framework and related contemporary technologies.
- Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
- Identify and apply authorisation, authentication and permission features in a Full-Stack web application solution.
- Create manual and/or automated tests for a Full-Stack Web application using an MVT framework and related contemporary technologies.
- Use a distributed version control system and a repository hosting service to document, develop and maintain a Full-Stack Web application using an MVC framework and related contemporary technologies.
- Deploy a Full-Stack Web application using an MVC framework and related contemporary technologies to a cloud-based platform

### 2. Explain the Design and Thinking Process

- feature name
- description of the feature
- screenshot

- Project Idea:	Book Review Blog
- Wireframing Tool: Balsamiq
- Project Management Kanban Board Tool: GitHub
- Leverage Bootstrap: Yes
- Leverage external APIs:	Cloudinary
- Define roles and responsibilities
--  Potential Roles: 
Developer (Frontend and Backend), 
Product Owner, 
Scrum Master,
Branch Manager (Forking), 
Documenter,
Environment Owner,
ERD Designer (Models).


### 3. UX with user stories
- site goals
- design thought process
- planning and wireframe design
- design choices
- user stories
- wireframes

## Project Board:
https://github.com/users/dmc-mcc/projects/7/views/1

### 4. Deployment
- demonstrate how to deploy project
- record to self and others of how to deploy and use our software
- detailed list of deployment steps
- heroku
- elephantsql
- cloudinary

## Heroku
- Activate your Heroku Student Pack
- Get the student offer
- Heroku dashboard
- Account settings
- Billings
- Subscribe to Eco
- Eco dyno
- Your Eco dyno subscription is now active
- DISABLE_COLLECTSTATIC key has a value of 1
- pip3 to install webserver gunicorn~=20.1
- Procfile: add a command using gunicorn and codestar wsgi: web: gunicorn codestar.wsgi
- DEBUG constant to False
- Heroku dashboard: go to your app. Click on the Deploy tab
- Reveal Config Vars in the Settings
- DATABASE_URL = add the value of the ElephantSQL URL

 ## Elephant SQL
- ElephantSQL is a PostgreSQL database hosting service that uses several cloud-hosted platforms
- Log into ElephantSQL to access your dashboard
- Create New Instance.
- Tiny Turtle plan
- Select a data centre near you
- Create instance
- Click on your newly named instance
- Click on STATS.
- Verify the version of PostgreSQL is 12 or higher
- Create a file named env.py,
- .gitignore file: add env.py
- os.environ.setdefault("DATABASE_URL", "<your-database-URL>")
- pip3 install dj-database-url~=0.5 psycopg2~=2.9, pip3 freeze --local > requirements.txt
- settings.py: import os; import dj_database_url if os.path.isfile('env.py'):     import env
- python3 manage.py createsuperuser

## Cloudinary
- A persistent file store
- Cloudinary is an API, so we will need an API key to connect the Django project to it securely
- pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15
- pip3 freeze --local > requirements.txt
- Sign up to Cloudinary
- env.py: os.environ.setdefault("CLOUDINARY_URL", "<URL copied from Cloudinary in last step>")
- settings.py: INSTALLED_APPS
- Update the app to use Cloudinary
- import the CloudinaryField from the cloudinary/models.py
- python3 manage.py makemigrations
- python3 manage.py migrate

## Deployment with static files
- whitenoise server
- pip3 install whitenoise~=5.3.0
- pip3 freeze --local > requirements.txt
- settings.py: 'whitenoise.middleware.WhiteNoiseMiddleware',

## Demonstrate Testing

Validator Testing
- Note: Regular HTML validators do not work well with DTL markup
- pip install django-html-validator
- It won't do anything until you chose how you want to use it and you also need to explicitly enable it with a setting.
- you have a choice of how you want to use this:
- As a middleware:
- In your unit tests (technically they're integration tests in Django)
- If you chose to set it up as a middleware and enable it accordingly it will run for every rendered template in the tests too. Not just when you run the server.

gitpod /workspace/book-review-blog (main) $ python3 manage.py test

Found 4 test(s).

Creating test database for alias 'default'...

System check identified no issues (0 silenced).

....
----------------------------------------------------------------------
Ran 4 tests in 0.624s

OK
Destroying test database for alias 'default'...


## Responsive Design:

Tablet:

<img src="static/images/tablet screen.png" >

Smartphone:

<img src="static/images/iphone se screen.png" >

## next steps
- Complete faq view
- provide link to purchase reviewed books on amazon


## Credit Sources
- images
- code
- text 
- link to relevant sites
- authors name









pip install -r requirements.txt
Successfully installed django-ckeditor-6.7.1 django-js-asset-2.2.0
pip install django-ckeditor

https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1


pip3 install Django~=4.2.1
pip3 freeze local > requirements.txt
django-admin startproject codeblog .
python3 manage.py startapp blog
python3 manage.py runserver

pip3 install gunicorn~=20.1
pip3 freeze local > requirements.txt
pip3 install dj-database-url~=0.5 psycopg2~=2.9
pip3 install django-summernote~=0.8.20.0
pip3 install whitenoise~=5.3.0
pip3 install django-allauth~=0.57.0
pip3 show django-allauth
https://docs.allauth.org/en/latest/installation/quickstart.html
/workspace/.pip-modules/lib/python3.9/site-packages
cp -r /workspace/.pip-modules/lib/python3.9/site-packages/allauth/templates/* ./templates/
pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7
pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~0.0.6
pip3 install urllib3~=1.26.15

python3 manage.py collectstatic
python3 -V
Python 3.9.17

pip3 freeze local > requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
https://book-review-blog-ff699e16bcc0.herokuapp.com/admin/auth/user/1/change/

python3 manage.py makemigrations blog
python3 manage.py migrate blog
python3 manage.py makemigrations --dry-run
python3 manage.py migrate blog zero   (unapply migrations)
git diff
mkdir -p blog/templates/blog
touch blog/templates/blog/post_list.html
python3 manage.py loaddata posts


dmc-m
dmcblog








