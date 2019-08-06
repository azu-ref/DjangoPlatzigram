from datetime import date

users = [
    {
        'email': 'hola@mail.com',
        'password': '12345678',
        'first_name': 'Carmen',
        'last_name': 'tamarin',
        'isAdmin': True
    },
    {
        'email': 'hola2@mail.com',
        'password': '12345678',
        'first_name': 'Pedro',
        'last_name': 'Manzanero',
        'birthdate': date(1995, 12, 24)
    },
    {
        'email': 'hola3@mail.com',
        'password': '12345678',
        'first_name': 'Elias',
        'last_name': 'Peralta'
    },
    {
        'email': 'hola4@mail.com',
        'password': '12345678',
        'first_name': 'Taisha',
        'last_name': 'Freseo'
    }
]

from posts.models import User

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk)