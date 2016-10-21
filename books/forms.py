from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
    
'''
# Ways to generate form html
from books.forms import ContactForm
f = ContactForm()

# Default: Table
f

# Unordered List
f.as_ul()

# Paragraph
f.as_p()

# Specific Field
f['field']

###############################################################
# Validate, Email can be excluded because required=False
f = ContactForm({'subject': 'Hello', 'email': 'adrian@example.com', 'message': 'Nice site!'})
f.is_bound
f.is_valid()

# Error Check
f.errors
f['field'].errors

# Clean Data, Converts values into appropriate Python types
f.cleaned_data
'''