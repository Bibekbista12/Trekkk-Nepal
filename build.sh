#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata trekimages.json
echo "
from users.models import CustomUser
if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser('admin', 'admin@treknepal.com', 'Admin@123', role='agency')
    print('Admin created')
else:
    u = CustomUser.objects.get(username='admin')
    u.set_password('Admin@123')
    u.role = 'agency'
    u.is_staff = True
    u.is_superuser = True
    u.save()
    print('Admin updated')
" | python manage.py shell