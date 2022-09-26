# Technical Test
### Main Knowledge:
The project has two deployments:
* server.py: main app to call the APIs.
* add_ram_details_to_db.py: script to run a jub every 60 seconds to get ram details from os


### Database:
Place your own database and username and password in .env file in project's root directory. (make sure the privileges is granted to the username )

Also edit hardcoded (shame on me!) username, password and database name in  add_ram_details_to_db.py.


### Migration Commands:

```
export FLASK_APP = server.py
flask db init
flask db migrate
flask db upgrade
```


