```
$$$$$$\                       $$\                         $$\                   $$$$$$\                                
\_$$  _|                      $$ |                        \__|                 $$  __$$\                               
  $$ |  $$$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$\  $$$$$$$\        $$ /  \__| $$$$$$\   $$$$$$\ $$\    $$\ 
  $$ |  $$  __$$\ $$  _____|\_$$  _|   \____$$\ $$  __$$\ $$ |$$  _____|$$$$$$\\$$$$$$\  $$  __$$\ $$  __$$\\$$\  $$  |
  $$ |  $$ |  $$ |\$$$$$$\    $$ |     $$$$$$$ |$$ /  $$ |$$ |$$ /      \______|\____$$\ $$$$$$$$ |$$ |  \__|\$$\$$  / 
  $$ |  $$ |  $$ | \____$$\   $$ |$$\ $$  __$$ |$$ |  $$ |$$ |$$ |             $$\   $$ |$$   ____|$$ |       \$$$  /  
$$$$$$\ $$ |  $$ |$$$$$$$  |  \$$$$  |\$$$$$$$ |$$$$$$$  |$$ |\$$$$$$$\        \$$$$$$  |\$$$$$$$\ $$ |        \$  /   
\______|\__|  \__|\_______/    \____/  \_______|$$  ____/ \__| \_______|        \______/  \_______|\__|         \_/    
                                                $$ |                                                                   
                                                $$ |                                                                   
                                                \__|                                                                   
```

### Getting started
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.
    
    > python manage.py db init

    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade


### Viewing the app

    Open the following url on your browser to view swagger documentation
    http://localhost:8000/api

### Frontend

    Instapic-Serv has a submodule called Instapic that serves as the frontend for this application. We serve these static files at the root of the application. In order to change 

### Using Postman

    Authorization header is in the following format:

    Key: Authorization
    Value: Bearer {token_generated_during_login}

### Production

    A production build of this app is currently running at http://serv.instapic.site/

    In development, we develop against a SQLite database, but in production, we use PostgreSQL.

    This app is designed to be deployed with Heroku, feel free to check out the Procfile to see how this app is run in production.

### Architecturally based on this project
https://medium.freecodecamp.org/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563