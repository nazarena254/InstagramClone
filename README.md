## InstagramClone

## Description
This is a Django web application. It is a clone of the instagram website. A user can upload images, follow and unfollow other users, like and unlike posts and visit their profiles as well as other users.The user can also search for a specific user.

## Author
Nazarena Wambura.</br>
[Github Account](https://github.com/nazarena254)

<!-- ### Homepage
![nazzblog](./picture/static/images/nazgallery.png)
### Wireframe sample
![nazzblog](./picture/static/images/wirefrm.jpeg)
### Admin panel
![nazzblog](./picture/static/images/djangoAdmin.png) -->

## User Story
1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

## Behaviour Driven Development (BDD)
1. Sign up to the application

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on sign up under login form   | username,password,email | user account and profile is created  | 

2. log into the application 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Enter details in the log in form   | username, password| Landing page is loaded is login is successful else an error message is shown  | 


3. See profiles 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| For user profile, click on the profile icon on navbar,or click on other users username | Username| User is redirected to the profile pages  |  

4. Follow and unfollow other users

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on button follow on their profiles | follow status| Increase number of followers by 1  | 


5. Like and unlike a post

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on like icon on a post  | like status| Increase number of likes by 1 else reduces the number of likes by 1  |

6. Comment on post

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on icon comment on the posts | comment| The added comment is displayed  |


## Setup/Installation Requirements
1. Create a folder and cd to it.
2. Clone the repository below with the command `git clone <https option url> .`  <br>
    https://github.com/nazarena254/InstagramClone  
3. Install dependencies in the requirements.txt file `pip install -r requirements.txt` .
4.  Type code . or atom . based on the text editor you have and work on it.   

## Database
1. Set up Database,and put your username and password in the code
2. Make migrations
    python3 manage.py makemigrations picture
3. Migrate
   python3 manage.py migrate 
       
## Running the Application
1. Run main aplication  ###### python version will vary in future
   * python3.9 manage.py runserver

## Creating Admins
1. Creating Admin Locally
    python manage.py createsuperuser. Then set username, email & password

2. Creating Django Admin   
     heroku run python manage.py createsuperuser. Then set username, email & password

## Technologies Used
* Python3.9.2 - as backend language
* Django4.0.5 - as a Framework
* Bootstrap4 - for responsiveness & styling 
* Sqlite - as database
* Cloudinary - as cloud-based image storage server
* Heroku - for deploying app

## Support & Contact Information
For any further inquiries, bugs, contributions or comments, reach me at:<br>
Email:<nancyngunjiri1@gmail.com>

## License
[MIT License](https://github.com/nazarena254/InstagramClone/blob/master/LICENSE)<br>
Copyright (c) 2021 **Nazarena Wambura**