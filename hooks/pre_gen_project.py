import sys

# Retrieve user inputs
author_names = "{{ cookiecutter.author_names }}".split(',')
author_emails = "{{ cookiecutter.author_emails }}".split(',')

# Check that both lists have the same length
if len(author_names) != len(author_emails):
    print("Error: The number of author names must match the number of author emails.")
    sys.exit(1)
