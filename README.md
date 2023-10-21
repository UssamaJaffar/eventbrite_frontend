# eventbrite_frontend



# eventbrite


This is forent server of the Eventbrite project

so Setup the project there is few steps

It is recommended to use python 3.11

1) First create a virtual env
by using this command in project

*python -m venv venv*

2) In lunix use this command 
    "source ./venv/script/activate"

In windows use this command
"./venv/script/activate"

3) run this command "pip install -r requirements.txt"

4) copy the file .Example.env into .env in same directory

5) run command "python manage.py makemigrations"

6) run command "python manage.py migrate"

7) run command "python manage.py runserver 0.0.0.0:9000"

8) open browser and run the project by write this in url 127.0.0.1:9000

*Make sure before running the frontend server the backend server is in running state.*