1. Fix CSRF problem when send POST request
 - Disable checking CSRF token in views.py
    adding `@csrf_exempt` decorator before the class definition
    this method is not recommended for security, so it is used for only testing in the dev stage
