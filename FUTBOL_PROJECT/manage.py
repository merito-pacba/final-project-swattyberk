import os
import sys

def main():
    # Buradaki 'scout_project.settings' kısmının klasör adınla aynı olduğundan emin ol
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scout_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django bulunamadı. pip install django yaptığından emin ol."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()