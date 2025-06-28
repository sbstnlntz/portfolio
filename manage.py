#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

Typical commands:
    - runserver         Starts the development server
    - migrate           Applies database migrations
    - createsuperuser   Creates a new admin user
    - collectstatic     Collects static files for deployment
    - shell             Opens the Django interactive shell
"""

import os
import sys


def main():
    """
    Sets the default Django settings module and runs management commands.

    This ensures that when you run `python manage.py <command>`,
    Django knows which settings to use and can handle your command.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raised if Django isn't installed or the virtual environment is inactive
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?"
        ) from exc

    # Run the command (e.g., `runserver`, `migrate`, etc.)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
