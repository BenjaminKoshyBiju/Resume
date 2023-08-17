pip install -r requirements.txt
pip install Pillow
python manage.py collectstatic --no-input
python manage.py migrate