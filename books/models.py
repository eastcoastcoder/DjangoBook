from __future__ import unicode_literals

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    def __str__(self):
        return self.name
        
    #Define Default Ordering for SELECT
    class Meta:
        ordering = ['name']

''' Equivalent SQL
CREATE TABLE "books_publisher" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL,
    "address" varchar(50) NOT NULL,
    "city" varchar(60) NOT NULL,
    "state_province" varchar(30) NOT NULL,
    "country" varchar(50) NOT NULL,
    "website" varchar(200) NOT NULL
);
'''

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name ='e-mail')
    
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title

'''    
python manage.py check

# Generate Migrations from Models:
python manage.py makemigrations books 

# Print SQL Statements:
python manage.py sqlmigrate books 0001

# Commit Migrations to DB:
python manage.py migrate 

# Import necessary for SELECT, INSERT, etc.
from books.models import Publisher

###############################################################
# INSERT Example, call save on Publisher Object:
p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
    city='Berkeley', state_province='CA', country='U.S.A.',
    website='http://www.apress.com/')
p1.save()

# Or call Publisher.objects.create():
p1 = Publisher.objects.create(name='Apress',
        address='2855 Telegraph Avenue',
        city='Berkeley', state_province='CA', country='U.S.A.',
        website='http://www.apress.com/')

###############################################################
# SELECT, returns a list
    Model.Manager.QuerySet(field='value')
        
Publisher.objects.all()
Publisher.objects.filter(country="U.S.A.", state_province="CA")

# Advanced Lookup types 
    icontains (case-insensitive LIKE)
    startswith
    endswith
    range (SQL BETWEEN queries)
# WHERE name LIKE '%press%';
Publisher.objects.filter(name__contains="press")

# SELECT, returns single object
try:
    p = Model.objects.get(field='value')
except Model.DoesNotExist:
    print ("Apress isn't in the database yet.")
else:
    print ("Apress is in the database.")

###############################################################
# ORDER BY field Ascending
Model.objects.order_by("field")
# ORDER BY field Descending
Model.objects.order_by("-field")

###############################################################
# Chaining: WHERE field = 'value' ORDER BY field ASC;
Model.objects.filter(field="value").order_by("field")

# Slicing OFFSET 0 LIMIT n;
Model.objects.order_by('field')[0:n]

###############################################################
# Updating multiple objects, SET field2 = 'value2' WHERE field1 = value1;
Model.objects.filter(field1=value1).update(field2='value2')

# Deleting, call delete()
Model.objects.filter(field='value').delete()

'''