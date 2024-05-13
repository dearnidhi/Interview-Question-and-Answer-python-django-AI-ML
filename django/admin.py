#1.admin
"""Django Admin is a really great tool in Django, it is actually a CRUD* user interface of all your models!"""
#*CRUD stands for Create Read Update Delete.

#2.Create User
"""To be able to log into the admin application, we need to create a user.
py manage.py createsuperuser
"""
#3.Django Admin - Include Member
"""To include the Member model in the admin interface, we have to tell Django that this model should be visible in the admin interface.
This is done in a file called admin.py, and is located in your app's folder, which in our case is the members folder."""