# THIS OR THAT API

# Description

This is the ReadMe for 'This or That's project's backend.
'This Or That' is a professional networking platform designed and created for fashion enthusiasts globally.
Users can interact once creating a Profile, by liking posts and following each others profiles. 
' this or that' is a community for fashion enthusiasts, users can post their favourtie celebrity fashion outfit, this inspiration can be taken for events. OOTD, general wear for birthdays/ concerts/ or just everyday wear. 
The page state changes depending on wether the User is logged 'in' or 'Out'. 
It works with full User CRUD functionality & allows the user to make its own posts which then can be liked by other users too. 
The 'thisorthat' API provides a backend database to create, view, edit and delete user's posts, likes & comments.
A user can publish a post, including description, an image, and keyword tags which then can be searched by the user. 
A user can search via celebrity.
The API also includes search and filter logic to improve user experience, and make it easier for users to find outfits and posts tailored to their own interests.


This project is the backend built to help support the REACTJS frontend, and it is powered by the DJANGO REST FRAMEWORK.

DEPLOYED BACK END API LINK - 

DEPLOYED FRONT END LIVE SITE -

DEPLOYED FRONT END REPO - 




# TABLE OF CONTENTS 
- [THIS OR THAT API](#this-or-that-api)
- [Description](#description)
- [TABLE OF CONTENTS](#table-of-contents)
- [DATABASE FLOW CHART:](#database-flow-chart-)
- [Strategy Plane](#strategy-plane)
- [User Stories link https://github.com/users/sammaxfleet/projects/7/views/1](#user-stories-link-https---githubcom-users-sammaxfleet-projects-7-views-1)
- [Stucture Plane](#stucture-plane)
  * [Homepage:](#homepage-)
  * [Profile Data:](#profile-data-)
  * [Posts](#posts)
- [TESTING](#testing)
- [DEPLOYMENT to Heroku](#deployment-to-heroku)
- [Local Deployment](#local-deployment)
- [How To Fork The Repository On GitHub](#how-to-fork-the-repository-on-github)
- [Languages](#languages)
- [Frameworks & Software](#frameworks---software)
  * [Libraries](#libraries)
- [Acknowledgements](#acknowledgements)


# DATABASE FLOW CHART:

<img width="655" alt="Screenshot 2023-12-12 at 14 32 27" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/eb92a86c-9ca7-4c08-beb6-c500243fff78">


# The Skeleton Plane 
[FLOW CHART API PROJECT 5.pdf](https://github.com/sammaxfleet/THISORTHATAPI/files/13649295/FLOW.CHART.API.PROJECT.5.pdf)



I have created the following models for the You.I Backend API:

Users (slightly customised from the Django standard User model)
Profiles (automatically created on User creation and customised)
Posts (a professional networking post publicised by a logged in user)
Likes (to indicate if a user likes another user's professional networking post)
Comments (to make a comment on a professional networking post)
Followers (For users to follow each other)
The relationships between all of these models is summarised in the followed entity relationship diagram:

# Strategy Plane

The Project was managed using Agile Methodology 

An Agile approach to creating this app has been applied. 
GitHub's projects was used to track user stories and implement ideas based on their level of importance for allowing use of the app with no loss of functionality or user experience.
FOUR categories were created indicating their level of importance, those were:

- MUST HAVE
- SHOULD HAVE
- COULD HAVE
- WON'T HAVE

By using AGILE methodology in this project I was able to deliver a site which had all required functionality and some more. 
Due to the time limit on this project I was not able to incorporate all initial listed features. but this is where an AGILE approach is great for app design. 
The project displays this by all projects being in the 'done' on the kaban board but with different labels. 



# User Stories link https://github.com/users/sammaxfleet/projects/7/views/1

<img width="1432" alt="Screenshot 2023-12-18 at 10 35 14" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/8faf4bf5-3200-4b9a-ba4c-39eab1b7b68f">



##User Stories 


Milestone Create Main App - thisorthat

Userstory: Create the following apps

PROFILES
POSTS
COMMENTS
LIKES 
FOLLOWERS
SEARCH & FILTER 



Milestone: Profiles App 

User Stories: 

1. As a developer/superuser I can view a list of all profiles so that I can see all the profiles that have been created. - 
2. As a developer/superuser I can view the details of one profile so that I can see individual profile data - SHOULD HAVE
3. As a developer/superuser I can edit a profile when I am logged in so that update my personal information - MUST HAVE
4. As a developer/superuser I can delete a profile that I own so that I can delete my user account from the API - MUST HAVE
5. AS a developer/superuser I can have multiple accounts - WON'T HAVE


Milestone: Posts

User Stories: 

1. As a developer/superuser I can view a list of all posts made by user in date order 
2. As a developer/superuser I can view a single post so that I can see single post details, including comments
3. As a developer/superuser I can create a new post so that this post will be displayed in the posts list
4. As a developer/superuser I can edit a post that I created so that I can amend any missing or incorrect information on the post
5. As a developer/superuser I can delete a post that I created so that I can delete post data from the API


Milestone: Comments

User Stories:

1. As a developer/superuser I can create a comment so that I can link a comment to a post
2. As a developer/superuser I can view a list of all comments so that I can see all comments created in the API
3. As a developer/superuser I can retrieve a single comment by ID so that I can edit or delete this comment
4. As a developer/superuser I can edit a comment that I created so that I can amend any missing or incorrect information
5. As a developer/superuser I can delete a comment which I created so that I can delete comment data from the API

Milestone: Likes

User Stories:

1. As a developer/superuser I can create a like a fashion post. 
2. As a developer/superuser I can delete a liked post which I created so that I can delete liked data from the API
3. As a developer/superuser I can not delete a liked object which I did not create
4. As a developer/superuser I can view a list of all likedobjects so that I can see all liked objects created in the API


Milestone: Followers

User Stories: 

1. As a developer/superuser I can create a follow so that I can follow another user
2. As a developer/superuser I can view a list of follows so that I can see all the follows that have been created
3. As a developer/superuser I can delete a follow so that I can unfollow another user profile


Milestone: Search and Filter

User Stories: 

1. As a developer/superuser I can see a search field in the events and posts list so that I can search for a specific event or post
2. As a developer/superuser I can search by celebrity 
3. As a developer/superuser I can view a list of posts I have posted a like id to so that I can see only the posts I like



Edit Profile :

Milestone: profile edit

user story: editing profile 

1. Celebrity search -
2. Outfit description -
3. fashion inspiration -
4. Image -
5.  Update/ Save 


# Stucture Plane


Features

## Homepage:


When you first enter the API site, you are directed to the Root Route homepage, with a message welcoming you to the API,

<img width="1435" alt="Screenshot 2023-12-18 at 14 31 16" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/0acf7ec6-c923-4c71-9c93-34d5e46ef488">



## Profile Data: 

Within the Profile List section, a user can view a list of all profiles in the API.

<img width="1320" alt="Screenshot 2023-12-18 at 14 32 43" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/3f0fc8fe-91d3-4ad0-8361-4d1cc3fac65d">

I also added the following fields to the Json DATA

"is_owner": 
"following_id": 
"posts_count":
"followers_count":
"following_count": 

If the user logs in, and views the detail of their own profile, additional Edit and Delete functionality becomes available. A pre-populated form is available to edit the profile model fields. A delete button is available to delete the profile from the API.

## Posts


Within the Posts List section, a user can view a list of all posts in the API.
<img width="1324" alt="Screenshot 2023-12-18 at 14 36 15" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/9da305ee-696f-49ea-833f-99663120f990">

I also added the following fields to the Json DATA

            "id": 
            "owner": 
            "is_owner": 
            "profile_id": 
            "profile_image":
            "created_at":
            "updated_at": 
            "title":
            "content": 
            "image": 
            "image_filter":
            "like_id":
            "likes_count": 
            "comments_count": 
            "fashion_inspiration": 





      
  Likes: 

  Within the Likes List section, a user can view a list of all likes made in the API.

  
<img width="1227" alt="Screenshot 2023-12-18 at 14 46 39" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/cd120197-c3a1-4ab1-909d-7a20e5ef47e9">

f the user logs in,  the ability to create a like becomes available if not they'll click but nothing will happen .

If a user tries to like the same post twice, they see an error message saying that they have already liked the selected post, and the duplicate like is not created. 
The user can like and unlike any posts on the page including their own. 


Comments:

Within the Comments List section, a user can view a list of all comments in the API.


<img width="378" alt="Screenshot 2023-12-18 at 14 47 29" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/2053f171-8bb9-434e-8739-efd3c09cdf54">



Once logged in THE USER can then comment on posts. They can make changes to a post or even delete it. 




Followers: 

Within the Follower List section, a user can view a list of all follower posts in the API.

<img width="514" alt="Screenshot 2023-12-18 at 14 47 50" src="https://github.com/sammaxfleet/THISORTHATAPI/assets/114914739/a71df09b-7399-4d82-be58-096e48e3f513">


The User when logged in will be able to follow and unfollow different profiles.

On the page popular users appears which enables to user to click on highly popular profiles straight away. 

If a user tries to follow the same profile twice, they see an error message saying that they are already following the selected profile, and the duplicate follow post is not created.

Once logged in, if the user views the details of a single follower post which they created additional Delete functionality becomes available. It is not possible to Edit a follower post.


# TESTING

- Code Validation
- Automated Testing
- Manual Testing



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


1. pip3 freeze --local > requirements.txt - This will create and add required libraries to requirements.txt, Now it's time to create the project.
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

12. Back in your Heroku app settings, click on the 'Reveal Config Vars' button. Create a config variable called DATABASE_URL and paste in the URL you copied from ElephantSQL. This connects the database into the      app.
13. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

    import os - This imports the os library
    os.environ["DATABASE_URL"] - This sets the environment variables.
    os.environ["SECRET_KEY"] - Here you can choose whatever secret key you want.

14. Back in the Heroku Config Vars settings, create another variable called SECRET_KEY and copy in the same secret key as you added into the env.py file. Don't forget to add this env.py file into the .gitignore      file so that it isn't commited to GitHub for other users to find.
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
21  os.environ["CLOUDINARY_URL"] = "cloudinary://************************" Let's head back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our         first deployment to Heroku to work.
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
26. Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!
    
# Local Deployment


# How To Fork The Repository On GitHub

It is possible to make an independent copy of a GitHub Repository by forking the GitHub account. 
The copy can be viewed & it's possible to make changes in the copy without affecting the original repository.

To fork the repository, follow these steps:

1. After logging in to GitHub locate the repository. 
2. On the top right side of the page there's a 'Fork' button. 
3. Click on the button to create a copy of the original repository.
4. Cloning And Setting Up This Project.
5. To clone and set up this project you need to follow the steps below.


Cloning And Setting Up This Project:

Steps:

1. When you are in the repository, find the code tab and click it.
2. To the left of the green GitPod button, press the 'code' menu, you will find a link to the repository then click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4. Type 'git clone', and then paste the URL that you copied from GitHub.
5. Press enter and a local clone will be created.
6. To be able to get the project to work you need to install the requirements, This can be done by using the command below:
7. pip3 install -r requirements.txt - This command downloads and installs all required dependencies that is stated in the requirements file.
8. The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work.
9. Environment variables are usually hidden due to sensitive information, it's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file).
10. The variables that are declared in the env.py file needs to be added to the Heroku config vars - Don't forget to do necessary migrations before trying to run the server.
11. Python3 manage.py migrate - This will do the necessary migrations.
12. Python3 manage.py runserver - If everything is setup correctly the project is now live locally.

# Languages

Python - Provides the functionality for the DRF backend framework.

# Frameworks & Software

Django RestFramework
PEP8 Validation
GitHub
Cloudinary
Heroku


## Libraries 

Cloudinary
dj - rest- auth
Django
django-allauth
django-cloudinary-storage 
django-cors-headers 
django-filter
django-taggit 
django-rest-framework 
gunicorn
pillow 
psycopg2
sqlparse




# Acknowledgements 

- My mentor at Code Institute Antonio Rodriguez, for code review, help and feedback. Very much appreciated!
- Also the tutors at code institute particularly helping with the API build. 
- My setpember code institute channel  for the support and weekly group chats. 


