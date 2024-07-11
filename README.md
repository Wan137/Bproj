git clone https://github.com/Wan137/Bproj.git
python -m venv env
For windows: env\Scripts\activate
For mac: source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
