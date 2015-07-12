Installation
============

(Tested on Windows 8.1)

1. Download evalproject from Git

2. Download Python 2.7.10

3. Go to terminal

4. Change to project home directory (folder with **run.py** file)

5.  Create a virtual environment in home directory
    - Install virtualenv tool - *pip install virtualenv*
    - Create a virtual directory called 'env' - *virtualenv env*

6.  Run the virtual environment - *env\Scripts\activate.bat*
    - For Linux/Mac - *source env\bin\activate*

7. For windows only - Download Microsoft Visual C++ Compiler for Python 2.7

8. Install the following software in the virtual environment:
  - Flask
    - *pip install flask*
  - Flask-Login
    - *pip install flask-login*
  - Flask-WTF
    - *pip install flask-wtf*
  - SQLAlchemy
    - *pip install flask-sqlalchemy*
  - Postgresql
    - Download PostgreSQL from 
      http://www.enterprisedb.com/products-services-training/pgdownload#windows
  - Psycopg2
    - Go to http://www.stickpeople.com/projects/python/win-psycopg/
    - Download Python 2.7 psycopg2 exe file
    - Move exe file from downloaded folder to project home folder
    - Run command *easy_install psycopg2-2.6.1.win-amd64-py2.7-pg9.4.4-release.exe*
  - Requests module
    - *pip install requests*
  - Flask-Restful
    - *pip install flask-restful*
9. Open up pgAdmin III
  - Create database user w/ sufficient roles - u= evaldba, p= hello911
  - Create database "evaldb"
10. Run the project (*python run.py*)
11. Go back to pgAdmin III and run the test data insert scripts in projecteval\scripts\
12. Test the app 
  - Go to **http://localhost:8080/login** for a html template 
  - Go to **http://localhost:8080/games** for a sample api response for first ten games in db
13. If anything is missing (in regards to installation), add 
   it to this file.
