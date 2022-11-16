# NutraAPI
This application is developed as an api to integrate easily with other platforms

&nbsp;

## Platfrom Tested
| platform | Version |
|:---------|:-------:|
| Ubuntu   | 20.04   |
| Docker   | 20.10.21|

## Software Requirement
- Python 3

## Hardware Requirement
- PC or Laptop
- Minimum of 4gb ram for PC and Laptop 

&nbsp;

&nbsp;

# Using application locally

&nbsp;

### Check Python Installation
- Linux (Ubuntu)
    ```bash
    python3 --version
    ```

&nbsp;

### Install Python Library
- Linux (Ubuntu)
    ```bash
    sudo apt install python-venv
    ```

&nbsp;

### Create Virtual Environment
- Linux (Ubuntu)
    ```bash
    python3 -m venv env
    ```

&nbsp;

### Activate Environment
- Linux (Ubuntu)
    ```bash
    source env/bin/activate
    ```

&nbsp;

### Install required libraries
- Linux (Ubuntu)
    ```python
    pip3 install -r requirements.txt
    ```
- Linux & Windows
    ```python
    pip install -r requirements.txt
    ```

&nbsp;

### Follow below commands to create .env file
- Create .env file
    - Linux (Ubuntu)
        ```bash
        touch .env
        ```
- Write necessary data in to .env file
    - Linux (Ubuntu)
        ```bash
        nano .env
        ```
        copy and paste below code to run the application
        ```bash
        SECRET_KEY=django-insecure-w9o4k3+u%ai*#*452fs3j2lh3#3_(m362=)0q)0681s2nbd=9g
        ```

&nbsp;

### Migrate database files
- Make migrations
    ```python
    python manage.py makemigrations
    ```
- Migrate required files to database
    ```python
    python manage.py migrate
    ```

&nbsp;

### Migrate necessary data into the database
- This data are taken from opensource [*Food Data Central*](https://fdc.nal.usda.gov/download-datasets.html)
    ```bash
    python nutra_app/functions/database_manual_functions.py
    ```

&nbsp;

### Create Static files
```python
python manage.py collectstatic
```

&nbsp;

### Create Admin
```python
python manage.py createsuperuser
```

&nbsp;

&nbsp;

# Products Used
<img src='https://code.visualstudio.com/assets/images/code-stable.png' style='width:80px'></img>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src='https://www.google.com/chrome/static/images/chrome-logo-m100.svg' style='width:80px'></img>

&nbsp;

&nbsp;

# Packages Used
<img src='https://static.djangoproject.com/img/logos/django-logo-positive.png' style='width:160px'></img>
&nbsp;&nbsp;&nbsp;&nbsp;
<img src='https://www.django-rest-framework.org/img/logo.png' style='width:160px'></img>
&nbsp;&nbsp;&nbsp;&nbsp;
<img src='https://www.gstatic.com/devrel-devsite/prod/v8b5224dd5a12318d5f6ab78c52530208ebc55112b691b517d54e8b153c58ecd1/tensorflow/images/lockup.svg' style='width:200px'></img>

&nbsp;

&nbsp;


# Reference
- [*Python*](https://www.python.org/)
- [*TensorFlow*](https://www.tensorflow.org/)
- [*Django*](https://www.djangoproject.com/)
- [*Django REST Framework*](https://www.django-rest-framework.org/)
- [*Food Data Central*](https://fdc.nal.usda.gov/download-datasets.html)


# Thank Card
- Thankyou very much for all OpenSoruce Libraries and softwares
- Thankyou very much to `Food Data Central` for providing dataset as opensource for accessing.



