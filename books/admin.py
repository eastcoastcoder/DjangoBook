from django.contrib import admin
from .models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email') #Add Sortable Cols
    search_fields = ('first_name', 'last_name') #Add Search Bar

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',) #Add Filer Sidebar
    date_hierarchy = 'publication_date' #Add Date Tabs
    ordering = ('-publication_date',) #Or define ordering in models (Meta is primary)
    #fields = ('title', 'authors', 'publisher') #Editing Entry, Exclude Avaliable Fields
    filter_horizontal = ('authors',) #Editing Entry, Many-To-Many
    #raw_id_fields = ('publisher',) #Display RawID Instead of Dropdown

# Format: admin.site.register(ModelClass, ModelAdminClass)
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)