# Django Project
Performing CRUD operations along with paging
## Installation

### Prerequisites

#### 1. Install Python
Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Install MySQL
Install ```mysql-8.0.15```. Follow the steps form the below reference document based on your Operating System.
Reference: [https://dev.mysql.com/doc/refman/5.5/en/](https://dev.mysql.com/doc/refman/5.5/en/)
#### 3. Setup virtual environment
```bash
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir envs

# Create virtual environment
virtualenv ./envs/

# Activate virtual environment
source envs/bin/activate
```

#### 4. Clone git repository
```bash
git clone "git@github.com:zishanjawed/Django-Project.git"
```

#### 5. Install requirements
```bash
cd Django-Project/
pip install -r requirements.txt
```

#### 6. Load sample data into MySQL
```bash
# open mysql bash
mysql -u <mysql-user> -p

# Give the absolute path of the file
mysql> source ~/Django-Project/database_dump.sql
mysql> exit;

```
#### 7. Edit project settings
```bash
# open settings file
vim panorbit/settings.py

# Edit Database configurations with your MySQL configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'world',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}



# save the file
```
#### 8. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver 0:8001

# your server is up on port 8001
```
Try opening [http://localhost:8001](http://localhost:8001) in the browser.
Now you are good to go.

### 9. URLs
#### Add People : [http://localhost:8001/people](http://localhost:8001/people)
![](https://i.imgur.com/xbnAaa9.png)
#### Fill The Imformation and click Add botton
![](https://i.imgur.com/2IT0RBC.png)
##### Now you will be redirected to /people/list  page
#### Add People : [http://localhost:8001/people/list](http://localhost:8001/people/list)
![](https://i.imgur.com/YLwkwW8.png)
##### Here you can use the pagination below. Click on the New button to add another record
