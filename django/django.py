#Django
"""Django is a back-end server side web framework.
Django is free, open source and written in Python.
Django makes it easier to build web pages using Python."""

#How does Django Work?
"""Django follows the MVT design pattern (Model View Template).
Model - The data you want to present, usually data from a database.
View - A request handler that returns the relevant template and content - based on the request from the user.
Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data."""

#Model
"""The model provides data from the database.
In Django, the data is delivered as an Object Relational Mapping (ORM),
 which is a technique designed to make it easier to work with databases."""

#View
"""A view is a function or method that takes http requests as arguments,
 imports the relevant model(s), and finds out what data to send to the template, and returns the final result.
The views are usually located in a file called views.py.
Django views are Python functions that takes http requests and returns http response, like HTML documents."""

#Template
"""A template is a file where you describe how the result should be represented.
Templates are often .html files, with HTML code describing the layout of a web page,
 but it can also be in other file formats to present other results, but we will concentrate on .html files."""

#URLs
"""Django also provides a way to navigate around the different pages in a website.
When a user requests a URL, Django decides which view it will send it to.
This is done in a file called urls.py."""

#django-admin startproject my_tennis_club
#py manage.py runserver


#What are Django's most prominent features?
"""
Programmers like Django mostly for its convenient features like:
Optimized for SEO
Extremely fast
A loaded framework that features authentications, content administrations and RSS feeds
Exceptionally scalable to meet the heaviest traffic demand
Highly secure
Versatility, enabling you to create many different types of websites"""

#What is an App?
"""An app is a web application that has a specific meaning in your project, like a home page,
 a contact form, or a members database.
we will create an app that allows us to list and register members in a database.
But first, let's just create a simple Django app that displays "Hello World!"."""

#make a migration to tell Django that it has to update the database:
#py manage.py makemigrations members
#py manage.py migrate


#Why do web developers prefer Django?
""" 
Web developers use Django because it:

Allows code modules to be divided into logical groups, making them flexible to change
Provides an auto-generated web admin module to ease website administration
Provides a pre-packaged API for common user tasks
Enables developers to define a given function’s URL
Allows users to separate business logic from the HTML
Is written in Python, one of the most popular programming languages available today
Gives you a system to define the HTML template for your web page, avoiding code duplication"""

 #What is CRUD?
I"""t has nothing to do with dirt or grime.
 It’s a handy acronym for Create, Read, Update, and Delete. 
 It’s a mnemonic framework used to remind developers on how to construct
usable models when building application programming interfaces (APIs)."""


#Does Django have any drawbacks?
"""
Django’s disadvantages include:
Its monolithic size makes it unsuitable for smaller projects
Everything hinges on Django’s ORM (Object-Relational Mapping)
Everything must be explicitly defined due to a lack of convention"""

#What does Django architecture look like?
"""
Django architecture consists of:
Models. Describes the database schema and data structure
Views. Controls what a user sees. The view retrieves data from appropriate models,
\ executes any calculations made, and passes it on to the template
Templates. Controls how the user sees the pages. 
It describes how the data received from the views need to be altered or formatted to display on the page
Controller. Made up of the Django framework and URL parsing"""

#Explain the Django project directory structure.
"""
Django organizes the various sections of the web application using a 
directory structure by generating a project and an app folder. 
Creating and arranging a proper project aids in keeping the project 
DRY (Don't Repeat Yourself) and clean. When you create a Django project, 
Django creates a root directory for the project using the project name you provide. 
It contains the files required to provide basic functionality to your web applications."""

#What is Django ORM? 
"""
Django ORM is a database abstraction API using which we can interact with its database models i.e., 
perform actions like add, delete, modify and query objects."""

#Define static files and explain their uses
""" .
​​The word "static files" refers to files in a web app that do not change, 
such as CSS, JavaScript, or pictures. They remain still.
 Static files are served up by the local Django web server for local development, 
and minimal configuration is required."""

# What are Django-admin and manage.py and explain their commands?
"""“Django-admin” is the command line utility of Django to perform administrative tasks.
 And manage.py is created automatically in every Django project.
 It performs the same functions as Django-admin, 
 but it also modifies the DJANGO SETTINGS MODULE environment variable
   to point to your project's settings.py file."""

#What is Jinja templating?
"""Jinja is a modern, designer-friendly Python templating language that was 
inspired by Django templates and is frequently
 used for execution."""

#What are the different model inheritance styles in Django?
"""
In Django, there are three types of inheritance. 

Abstract base classes - When the parent class contains common 
fields and the parent class table is undesirable,use this.

Multi-table inheritance - When the parent class has common fields,
but the parent class table already exists in the database on its own, use this.

Proxy models - Use this when you want to change the parent class's behavior,
 for as by modifying the order or adding a new model manager."""


Intermediate Django Interview Questions

#what’s the difference between a project and an app?
"""
The project covers the entire application, while an app is a module or application within 
the project that deals with one dedicated requirement.
 So, a project consists of several apps, while an app features in multiple projects."""

#How to filter items in the Model?
"""Depending on the user's interests, it is a very normal need for the web application to 
display data on the web page. The application is made more user-friendly by its search feature.
 The filter() method of the Django framework can be used to filter data from database tables.
A table may have numerous records, and depending on the specific criteria, 
it may be necessary to determine some specific data. By utilizing the filter() technique in numerous ways,
this process gets simpler.  There are four types of filtering: Simple filtering, filter data with multiple fields, 
filter data with Q objects, and Filter data using filter chaining"""




#How to view all items in the Model?
"""In Django, to view all items in a model, you can simply use the .all() method on the model's manager.
"""
from myapp.models import MyModel
all_items = MyModel.objects.all()

# What's the significance of the settings.py file?
"""This file, as the name implies, stores our Django project's configurations or settings,
 such as database configuration, backend engines, middlewares, installed applications, main URL configurations,
   static file addresses, templating engines, security keys, allowed hosts etc."""

#What are Django.shortcuts.render functions?
"""
The render function is a shortcut function that allows the developer to quickly pass the data dictionary
together with the template.
The template is then combined with the data dictionary using the templating engine in this function.
Finally, the render() function provides a HttpResponse containing the rendered text,
 which is the data returned by the models.
As a result, Django render() saves the developer time and
 allows him to utilize multiple template engines."""

#. What is the context in Django?
"""
In Django, a context is a dictionary where the keys are the names of the variables and
 the values are the values of those variables. The template receives this dictionary (context), 
 which it uses along with the variables to output the dynamic content."""

#What's the use of a session framework?
"""The session structure enables per-site-visitor storage and retrieval of any type of data. 
It abstracts the sending and receiving of cookies and keeps data on the server side."""


#What databases are supported by Django?
""" 
The following databases are that Django formally supports:

PostgreSQL
MariaDB
MySQL
Oracle
SQLite"""

#Explain user authentication in Django.
"""Django includes a user authentication system that handles
 objects such as users, groups, user permissions,
 and some cookie-based user sessions."""

# What are signals in Django?
"""Signals are pieces of code containing information about what is currently going on.
 A dispatcher is used to both send and listen for signals."""
Python-m Django–version

#What is the Django Admin interface?
"""
Django comes equipped with a fully customizable, built-in admin interface. 
This portal lets developers see and make changes to all the data residing in the database that contains
 registered apps and models. The model must be registered in the admin.py
   file to use a database table with the admin interface."""

#Discuss Django’s Request/Response Cycle.
"""Starting the process off, the Django server receives a request. 
The server then looks for a matching URL in the URL patterns defined for the project.
If the server can’t find a matching URL, it produces a 404-status code.
If the URL matches, it executes the corresponding code in the view file
 associated with the URL and sends a response."""

#In Django’s context, what’s the difference between a project and an app?
"""
The project covers the entire application, while an app is a module or application within the project
that deals with one dedicated requirement. So, a project consists of several apps, while an app features
in multiple projects."""

#Django QuerySet
"""A QuerySet is a collection of data from a database.
A QuerySet is built up as a list of objects.
QuerySets makes it easier to get the data you actually need, 
by allowing you to filter and order the data at an early stage."""

# What are Django's most prominent features?
"""Optimized for SEO
Extremely fast
A loaded framework that features authentications, content  and RSS feeadministrationsds
Exceptionally scalable to meet the heaviest traffic demand
Highly secure
Versatility, enabling you to create many different types of websites"""

#Q objects in Django ORM.
"""In Django ORM, Q objects provide a way to encapsulate a complex query logic using logical operators 
like AND, OR, and NOT. They allow you to construct more advanced database queries 
than what is possible with simple keyword arguments to query functions such as .filter() and .exclude().
"""
from django.db.models import Q
from myapp.models import Product

# Example query using Q objects
query = Q(price__gte=100) & Q(category='Electronics')
results = Product.objects.filter(query)





Advanced Django Interview Questions

#What are Django exceptions?
"""exceptions are errors or exceptional conditions that occur during the execution of a web application. 
Django provides a set of predefined exception classes that cover a wide range of potential errors that can
 occur during the development and operation of a Django project. These exceptions help developers handle errors
gracefully and provide meaningful feedback to users when something goes wrong. 
"""
#Difference between select_related and prefetch_related?
"""Django's select-related and prefetch-related functions are intended to reduce
 the number of database queries that are generated when related objects are accessed. 
When a query is executed,
select related() "follows" foreign-key relationships and choose extra related-object data.
Prefetch related() performs the "joining" in Python by performing a separate lookup for each relationship."""

# Retrieve all books and their related authors in a single query
books = Book.objects.select_related('author').all()
# Retrieve all authors and prefetch their related books
authors = Author.objects.prefetch_related('book_set').all()

#Mention the ways used for the customization of the functionality of the Django admin interface.
"""

Customizing the functionality of the Django admin interface can be achieved through various methods,
 providing developers with flexibility in tailoring the admin interface to suit specific project requirements.
Here are some of the common ways to customize the Django admin interface:

Admin Site Configuration
ModelAdmin Class
Customizing Templates
Admin Actions
"""

#How to combine multiple QuerySets in a View?
"""
you can combine multiple QuerySets in a view using various techniques,
 depending on your specific requirements and the relationship between the QuerySets.

Using chain() from itertools:
If you have multiple QuerySets that you want to combine into a single iterable without
 merging or altering their contents, you can use the chain() function from the itertools module.

from itertools import chain
queryset1 = Model1.objects.all()
queryset2 = Model2.objects.all()
combined_queryset = chain(queryset1, queryset2)
 
 """

#Difference between Django OneToOneField and ForeignKey Field?
"""ForeignKey Field:
Purpose: A ForeignKey field is used to define a many-to-one relationship between two models.
 It is used when a model instance can be associated with multiple instances of another model."""
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

"""OneToOneField:
Purpose: A OneToOneField is used to define a one-to-one relationship between two models.
It is used when each instance of one model corresponds to exactly one instance of another model."""

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

class UserProfile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    bio = models.TextField()

# Why is permanent redirection not a good option?
"""Permanent redirection (HTTP 301 status code) is a useful tool for 
indicating to clients and search engines that a resource has moved permanently to a new location. 
However, it may not always be the best option for certain scenarios due to the following reasons:
Caching
SEO Implications
User Experience
Loss of Analytics
"""
#What is Django Field Class?
"""In Django, a Field class represents a database field in a model.
It encapsulates the metadata and behavior associated with a particular database column,
such as its data type, constraints, default values, and validation rules.
Field classes are defined within Django's django.db.models.fields module and 
are used to define the structure of database tables when defining models."""

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# What is mixin?
"""In Django, a mixin is a Python class that is inherited by another class to carry out extra functions.
Classes that can be reused and scaled are mixins.
 A unique form of multiple inheritances is a mixin. 
 Mixins are typically employed in two contexts:
You wish to give a class several optional features.
You wish to apply a specific feature to numerous classes."""

class LoggingMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class MyClass(LoggingMixin):
    def do_something(self):
        self.log("Doing something...")

#How to use file-based sessions?
"""To use a file-based session, you must set the SESSION_ENGINE settings to
 "Djangoo.contrib.sessions.backends.file"""

# What do you use django.test.Client class for?
"""The Client class acts like a dummy web browser,
 enabling users to test views and interact with Django-powered applications programmatically.
   This is especially useful when performing integration testing."""

# What is a QuerySet in the context of Django?
"""QuerySet is a collection of SQL queries. 
The command print(b.query) shows you the SQL query created from the Django filter call.
"""
#39. List several caching strategies supported by Django.
"""Database caching
In-memory caching
File System Caching
Memcached """

# Does Django support multiple-column primary keys?
"""No, Django supports only single-column primary keys.
"""
#What does a URLs-config file contain?
"""The URLs-config file in Django contains a list of URLs and mappings created to view those URLs' functions.
 The URLs can map to view functions, class-based views, and the URLs-config of other applications."""

#What do you use middleware for in Django?
"""
Content Gzipping
Cross-site request forgery protection
Session management
Use authentication
Authentication
Logging and Debugging
Caching
URL Rewriting
"""
#What is the Django Rest Framework?
"""The Django Rest Framework (DRF) is a framework that helps you quickly create RESTful APIs.
 They are ideal for web applications due to low bandwidth utilization."""






        










