# i18n Project

This project involves implementing internationalization (i18n) features in a Flask application. You will learn how to display different languages, infer the correct locale based on various parameters, and localize timestamps.

## Learning Objectives

- Parametrize Flask templates to display different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- A README.md file at the root of the project folder is mandatory.
- Use the pycodestyle style (version 2.5).
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- All `.py` files should be executable.
- All modules should have documentation.
- All classes should have documentation.
- All functions and methods should have documentation.
- Documentation should be real sentences explaining the purpose of the module, class, or method.
- All functions and coroutines must be type-annotated.

## Tasks

### 0. Basic Flask App

Setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that outputs "Welcome to Holberton" as the page title and "Hello world" as the header.

- **Files:** 
  - `0-app.py`
  - `templates/0-index.html`

### 1. Basic Babel Setup

Install the Babel Flask extension and instantiate the Babel object in your app. Configure available languages and set the default locale and timezone.

- **Files:** 
  - `1-app.py`
  - `templates/1-index.html`

### 2. Get Locale from Request

Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with supported languages.

- **Files:** 
  - `2-app.py`
  - `templates/2-index.html`

### 3. Parametrize Templates

Use the `_` or `gettext` function to parametrize your templates with message IDs. Initialize and compile translations for English and French.

- **Files:** 
  - `3-app.py`
  - `babel.cfg`
  - `templates/3-index.html`
  - `translations/en/LC_MESSAGES/messages.po`
  - `translations/fr/LC_MESSAGES/messages.po`
  - `translations/en/LC_MESSAGES/messages.mo`
  - `translations/fr/LC_MESSAGES/messages.mo`

### 4. Force Locale with URL Parameter

Implement a way to force a particular locale by passing the `locale` parameter in the URL.

- **Files:** 
  - `4-app.py`
  - `templates/4-index.html`

### 5. Mock Logging In

Create a mock user login system and display a welcome message in the HTML template if a user is logged in.

- **Files:** 
  - `5-app.py`
  - `templates/5-index.html`

### 6. Use User Locale

Update the `get_locale` function to use the user's preferred locale if supported. The order of priority should be URL parameters, user settings, request header, and default locale.

- **Files:** 
  - `6-app.py`
  - `templates/6-index.html`

### 7. Infer Appropriate Time Zone

Define a `get_timezone` function and use the `babel.timezoneselector` decorator to infer the correct timezone based on URL parameters, user settings, or default to UTC.

- **Files:** 
  - `7-app.py`
  - `templates/7-index.html`

## Resources

Read or watch the following resources to help you complete this project:

- [Flask-Babel](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](https://pythonhosted.org/pytz/)

## Submission

- All code is documented.
- All functions and methods are type-annotated.
- Test application thoroughly.

## Repository

- **GitHub repository:** `alx-backend`
- **Directory:** `0x02-i18n`

## Author

- **@waltertaya**
