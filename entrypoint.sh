#!/bin/bash

# ... seus comandos existentes (como python manage.py migrate) ...

echo "--> Gerenciando o superusuário..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@email.com', 'opet2026')
    print("Superusuário criado com sucesso.")
else:
    u = User.objects.get(username='admin')
    u.set_password('opet2026')
    u.save()
    print("Senha do superusuário atualizada com sucesso.")
EOF

# ... comando para rodar o gunicorn ...
