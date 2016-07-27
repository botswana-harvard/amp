import os

from unipath import Path

try:
    # expect at ~/source/amp/etc/default.cnf
    # etc folder is not in the git repo
    PATH = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1).child('etc')
    if not os.path.exists(PATH):
        raise TypeError('Path to database credentials at \'{}\' does not exist'.format(PATH))
    with open(os.path.join(PATH, 'secret_key.txt')) as f:
        PRODUCTION_SECRET_KEY = f.read().strip()
    PRODUCTION_POSTGRES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'OPTIONS': {
                'read_default_file': os.path.join(PATH, 'default.cnf'),
            },
            'HOST': '',
            'PORT': '',
            'ATOMIC_REQUESTS': True,
        },
#         'lab_api': {
#             'ENGINE': 'django.db.backends.mysql',
#             'OPTIONS': {
#                 'read_default_file': os.path.join(PATH, 'lab_api.cnf'),
#             },
#             'HOST': '',
#             'PORT': '',
#             'ATOMIC_REQUESTS': True,
#         },
    }
except TypeError:
    PRODUCTION_POSTGRES = None
    PRODUCTION_SECRET_KEY = None
    print('Path to production database credentials does not exist')

TEST_HOSTS_POSTGRES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'amp',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    },
    'lab_api': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'amp_lab',
        'USER': 'django',
        'PASSWORD': 'ampcc3721b',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    },
}
