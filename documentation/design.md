# Django Design Principles 📐📏

## Loose coupling and tight cohesion

![image](https://drive.google.com/uc?export=view&id=1akH6ytCH4pcvuo1a74hYE2uZP6HHUnoD "Cohesion")

*extracted from:
[https://www.coursera.org/lecture/object-oriented-design/1-3-1-coupling-and-cohesion-q8wGt]*

_One of the core features of Django's stack is loose coupling and tight cohesion, following Encapsulation principles._

In Computer Science, coupling is related to the degree of interdependence that exists between software modules and how closely they are connected to each other.

Tight coupling means the modules are deeply connected and interdependent. This is considered bad design, like a puzzle system. Loose coupling, means the components know little or only enough about each other when absolutely necessary and yet can work well together, like a lego system.

Cohesion is related to the interdependency within the module, amongst its elements, forming a single cohesive unit.

Quoted from "Boulder Patterns Group Minutes Old"
>the correct terminology is "tight internal cohesion" and "loose external coupling". This basically means that each method in a class should have one task and the class as a whole should have one major responsibility (tight internal cohesion) and that other classes should not depend on the inner workings of this class but should be designed to the "interface" of the class (loose external coupling). See a recent post by AlanShalloway on this: [http://groups.yahoo.com/group/dpexplained/message/108]

More on that topic can be found at: [http://wiki.c2.com/?CouplingAndCohesion]

_An example of loose coupling and tight cohesion in Django is that the template system doesn't know about Web requests, the database layer knows nothing about how the data will be displayed and the view system allows for any template system a programmer uses._

If one wants to use the REST framework approach, that is possible and the view can be handled by another application written in React or Vue, for example.

This allows Django to be flexible, reusable and maintainable. Keeping modules simple is fundamental.

## Creating a virtual environment

Create a virtual environment by running `pip install virtualenv`. Then if you pick a name like _myenv_, run `virtualenv myenv`

## Activating your virtual environment

If you are a Mac user, activate your environment by running `source myenv/bin/activate`   
If you are a Windows user, activate your environment by running `source myenv/Scripts/activate`   

## Installing dependencies

After activating the environment, run `pip install -r requirements.txt` to install all dependencies needed for this project. 🍾

More about the *requirements.txt* and *pip freeze* can be found at: (https://pip.pypa.io/en/stable/reference/pip_freeze/) 🎯

## Starting Django on your local server

So, a project was created with Django. The main project folder is called `code_resource_center`.
Run `cd code_resource_center` and run `python manage.py runserver`. If everything works correctly you should see a Welcome page by Django on: `http://127.0.0.1:8000/`

Remember to run `python manage.py migrate` to apply migrations.

_Important_: `django startproject` creates a root app folder for the project (`code_resource_center`). Inside, you can edit your settings. Your other apps will live inside the project, as 'sisters' of the 'crc' folder. Remember that if you want to commit anything or make changes to push to Git, you'll always have to go back to the parent folder which is where our repo lives (`code-resource-center`)

## Django Admin

To run the admin panel and make sure the DB is working fine, go to your root folder `code_resource_center` and run `python manage.py runserver`. Then, go to `localhost:8000/admin/`. Login with the superuser ('crcuser') and password ('myresources')

## Bootstrap

Check this documentation in order to add Boostrap to the project. (https://pypi.org/project/django-bootstrap3/)
For full documentation, check:
(https://django-bootstrap3.readthedocs.io/en/latest/)
