import os

def create_django_project(project_name):
    # Create main project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create manage.py
    with open("manage.py", "w") as manage_file:
        manage_file.write("#!/usr/bin/env python\n")
        manage_file.write("import os\n")
        manage_file.write("import sys\n\n")
        manage_file.write("if __name__ == '__main__':\n")
        manage_file.write("    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings.development')\n".format(project_name))
        manage_file.write("    try:\n")
        manage_file.write("        from django.core.management import execute_from_command_line\n")
        manage_file.write("    except ImportError as exc:\n")
        manage_file.write("        raise ImportError(\n")
        manage_file.write("            \"Couldn't import Django. Are you sure it's installed and \"\n")
        manage_file.write("            \"available on your PYTHONPATH environment variable? Did you \"\n")
        manage_file.write("            \"forget to activate a virtual environment?\"\n")
        manage_file.write("        ) from exc\n\n")
        manage_file.write("    execute_from_command_line(sys.argv)\n")

    # Create main project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create main project package
    os.makedirs(project_name)

    # Create settings directory
    os.makedirs(os.path.join(project_name, "settings"))
    os.chdir(os.path.join(project_name, "settings"))

    # Create __init__.py
    open("__init__.py", "w").close()

    # Create base.py
    with open("base.py", "w") as base_file:
        base_file.write("# Base settings\n\n")

    # Create development.py
    with open("development.py", "w") as development_file:
        development_file.write("# Development settings\n\n")

    # Create production.py
    with open("production.py", "w") as production_file:
        production_file.write("# Production settings\n\n")

    # Create testing.py
    with open("testing.py", "w") as testing_file:
        testing_file.write("# Testing settings\n\n")

    # Go back to main project directory
    os.chdir(os.path.join("..", ".."))

    print(f"Django project structure for '{project_name}' has been created.")

if __name__ == "__main__":
    project_name = input("Enter your Django project name: ")
    create_django_project(project_name)
