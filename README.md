# THIS OR THAT API

' this or that' is a community for fashion enthusiasts. 
Users Can post their favourtie celebrity fashion outfit, 
Users can interact once creating a Profile, by liking posts and following each other. 

This project is the backend built to help support the REACTJS frontend, and it is powered by the DJANGO REST FRAMEWORK.

DEPLOYED BACK END API LINK - 

DEPLOYED FRONT END LIVE SITE -

DEPLOYED FRONT END REPO - 


# TABLE OF CONTENTS 

DATABASE FLOW CHART:

<img width="655" alt="Screenshot 2023-12-12 at 14 32 27" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/eb92a86c-9ca7-4c08-beb6-c500243fff78">



[FLOW CHART API PROJECT 5.pdf](https://github.com/sammaxfleet/THISORTHATAPI/files/13649295/FLOW.CHART.API.PROJECT.5.pdf)







USER STORIES


DATABASE



TESTING


MANUAL TESTING


## Frameworks, Libraries & Programs Used:

Django
Django RestFramework
Cloudinary
Heroku
Pillow
Django Rest Auth
PostgreSQL
Cors Headers

# DEPLOYMENT to Heroku 

The project was deployed to Heroku, the deployment process is as follows:

1. To begin with we need to create a GitHub repository from the Code Institute template by following the link and then click 'Use this template'.
2. Fill in the details for the new repository and then click 'Create Repository From Template'.
3. When the repository has been created, click on the 'Gitpod' button to open it in the GitPod Editor.
4. Now it's time to install Django and the supporting libraries that are needed, using the following commands:
5. pip3 install 'django<4' gunicorn
6. pip3 install 'dj_database_url psycopg2
7. pip3 install 'dj3-cloudinary-storage

When Django and the libraries are installed we need to create a requirements file.


1. pip3 freeze --local > requirements.txt - This will create and add required libraries to requirements.txt
1. Now it's time to create the project.
2. django-admin startproject YOUR_PROJECT_NAME . - This will create the new project.
3. When the project is created we can now create the applications.
4. My project consists of the following apps; Profiles, Comments, Posts, Profile, Followers, 
5. python3 manage.py startapp APP_NAME - This will create an application
6. We now need to add the applications to settings.py in the INSTALLED_APPS list.
7. Now it is time to do our first migration and run the server to test that everything works as expected. This is done by writing the commands below.
8. python3 manage.py makemigrations - This will prepare the migrations
  python3 manage.py migrate - This will migrate the changes
  python3 manage.py runserver - This runs the server. To test it, click the open browser button that will be visible after the command is run.
9. Now it is time to create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.
Once signed into your Heroku account, click on the button labeled 'New' to create a new app.

10. Choose a unique app name, choose your region and click 'Create app".

11. Next we need to connect an external PostgreSQL database to the app from ElephantSQL. Once logged into your ElephantSQL dashboard, you click 'Create New Instance' to create a new database. Give the database a:

    Name
    Tiny Turtle Free Plan
    Selected data center near you
    
    Click 'Create Instance'. Return to your ElephantSQL Dashboard, and click into your new database instance. Copy the Database URL and head back to Heroku.

12. Back in your Heroku app settings, click on the 'Reveal Config Vars' button. Create a config variable called DATABASE_URL and paste in the URL you copied from ElephantSQL. This connects the database into the app.



13. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

    import os - This imports the os library
    os.environ["DATABASE_URL"] - This sets the environment variables.
    os.environ["SECRET_KEY"] - Here you can choose whatever secret key you want.


14. Back in the Heroku Config Vars settings, create another variable called SECRET_KEY and copy in the same secret key as you added into the env.py file. Don't forget to add this env.py file into the .gitignore file so that it isn't commited to GitHub for other users to find.

15. Now we have to connect to our environment and settings.py file. In the settings.py, add the following code:

import os

import dj_database_url

if os.path.isfile("env.py"):

import env


16. In the settings file, remove the insecure secret key and replace it with: SECRET_KEY = os.environ.get('SECRET_KEY').
17. Now we need to comment out the old database settings in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).
    Instead, we add the link to the DATABASE_URL that we added to the environment file earlier.

18. Save all your fields and migrate the changes again.
    python3 manage.py migrate

19. Now we can set up Cloudinary (where we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

20. Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):

21  os.environ["CLOUDINARY_URL"] = "cloudinary://************************" Let's head back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our first deployment to Heroku to work.

22. Back in the settings.py file, we now need to add our Cloudinary Libraries we installed earlier to the INSTALLED_APPS list. Here it is important to get the order correct.

  - cloudinary_storage
  -  django.contrib.staticfiles
  - cloudinary

  23.  For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.
        To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to the ALLOWED_HOSTS list:
      ALLOWED_HOSTS = ['happening-api-kelz.herokuapp.com', 'localhost']

24. Now we just need to create the basic file directory in Gitpod. Create a file called *Procfile and add the line web: gunicorn PROJ_NAME.wsgi? to it.
    now you can save all the files and prepare for the first commit and push to Github by writing the lines below.
    
git add .
git commit -m "Deployment Commit
git push

25. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!
    



# How To Fork The Repository On GitHub
It is possible to make an independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to make changes in the copy without affecting the original repository. To fork the repository, follow these steps:

After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.
Cloning And Setting Up This Project
To clone and set up this project you need to follow the steps below.

When you are in the repository, find the code tab and click it.
To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.
To be able to get the project to work you need to install the requirements. This can be done by using the command below:
pip3 install -r requirements.txt - This command downloads and installs all required dependencies that is stated in the requirements file.
The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.
python3 manage.py migrate - This will do the necessary migrations.
python3 manage.py runserver - If everything i setup correctly the project is now live locally.



# Credits 


# Acknowledgements 



