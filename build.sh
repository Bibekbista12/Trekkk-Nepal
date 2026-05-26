


#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
echo "from users.models import CustomUser; CustomUser.objects.filter(username='admin').exists() or CustomUser.objects.create_superuser('admin', 'admin@treknepal.com', 'Admin@123', role='agency')" | python manage.py shell