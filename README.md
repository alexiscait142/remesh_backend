# Setting up this Python/Django backend

In order to set up this backend, you will need the most recent versions of Python and Pip (I use Python3 and Pip3).

Create a directory for your project (which will hold both the backend and frontend folders). The first step will be to create a virtual environment for the Django project.

Within the directory you just made, run the command:
```
python3 -m venv venv
```
and replace the second venv with whatever you want to name it (in my case, I named it remesh_venv). Then you want to activate it so you can start working and installing packages:
```
. ./remesh_venv/bin/activate
```
where again, replace remesh_venv with whatever you decided to name your venv.

Now, fork and clone this repo into that same directory you initally created, so then you should see two folders: the venv folder, and the project folder. CD into that cloned folder and open it in your favorite text editor.
We need to install all the required packages, so simply run the command:
```
pip3 install -r requirements.txt
```
which will install the proper libraries. You can also run
```
pip freeze
```
to make sure they're all there. That should match exactly what it says in the requirements.txt file.

Next you'll have to retrieve a secret key. This is called from the settings.py setting by using the python-decouple library, but the secret key will actually be placed in a .env file.
Since I included my .env file in my .gitignore, go ahead and `touch .env` in the directory where the manage.py file is. Then you can go to this website
https://miniwebtool.com/django-secret-key-generator/ to generate a secret key. Navigate to your .env file and type SECRET_KEY=[enter your key here] (replace [your key here] with the secret key that was generated. No brackets, no quotes).

Then, within this main directory (very important you run these commands within the directory that has the manage.py file), run `python3 manage.py migrate` for good measure, you'll be able to run `python3 manage.py runserver` and navigate to http://localhost:8000 (unless you specify another port for some reason) and it'll be up and running!

In this backend, you will be able to use the endpoints (/conversations, /messages, /thoughts) to view objects. These have full CRUD, and you can test them in programs like Postman or Insomnia. Keep in mind, for POST and PUT/PATCH, you will need to include a final '/' at the end of the URL for it to succeed. And, if you're POSTing an object that requires a foreign key (e.g. a message requires a conversation and a thought requires a message), you will need to include the id of the related object you want to use, and set it up as such:
```
{
    ...
    "conversation": 1,
    ...
}
```
And of course, if you want to PUT/PATCH or DELETE, you will need the object's id in the url (e.g. /messages/2).

Then you can fork and clone the frontend repo here: https://github.com/alexiscait142/remesh_frontend

Additional packages used in this project:

python-decouple (https://pypi.org/project/python-decouple/)

djangorestframework (https://www.django-rest-framework.org/)

django-cors-headers (https://pypi.org/project/django-cors-headers/0.01/)
