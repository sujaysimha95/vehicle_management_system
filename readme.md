#### Summary:

Project Name:  Vehicle Service Management System (VSMS)\
Language Used:  Python 3.7.7\
Framework used: Flask\
Database:  MySQL\
User Interface Design:  HTML, CSS\
Web Browser with full functionalities:  Google Chrome\
Number of databases used: 1\
Number of tables used: 2

#### Modules used:

1. flask
2. mysql-connector-python
3. pymsgbox
4. openpyxl
4. tzlocal
5. simple_log
6. arrow
7. platform

#### Walk-through of how to setup mysql correctly for this project:

1. go to https://dev.mysql.com/downloads/installer/ and install the necessary
   installer
2. run the installer and select 'server only' and click 'next'
3. click next repeatedly with all default values.
4. wait a while while the database is initialized
5. click next
6. click add
7. in connectors -> connector/python, select the latest version
8. click install
9. wait till the program installs
10. click finish
11. run setup.py

#### What you could do:

There's a lot I've missed out. I haven't hashed the password, which is a very 
important security feature. I also haven't checked for sql injections, whether 
there is any other user with the same name, account or phone number. It's up to
you what you could add to the project!