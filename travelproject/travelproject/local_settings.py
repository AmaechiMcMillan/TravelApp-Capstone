SECRET_KEY = 'django-insecure-@&_$1wtu6n)+mli60p@d574*%8@_x$kdhqn10-qkrcnkbe9+r('

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'travel_database',
        'USER': 'root',
        'PASSWORD': 'Indy#AIM012520',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

