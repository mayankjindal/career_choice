import os, sys

path = "/home/mayankjindal/career_choice"
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "career_choice.settings")

application = StaticFilesHandler(get_wsgi_application())
