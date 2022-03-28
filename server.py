# run.py
import os
from waitress import serve
from config.wsgi import application  # Import your app

# Run from the same directory as this script
this_files_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_files_dir)

# `url_prefix` is optional, but useful if you are serving app on a sub-dir
# behind a reverse-proxy.
serve(application, host='PRIVATE_IP', port=8000)