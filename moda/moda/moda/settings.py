# -*- coding: utf-8 -*-

"""

Тут надо написать свой собственный комментарий. Что за проект, зачем он нужен и т.д.
Если Вам неудобно писать на русском - пишите на английском. Но комментарии быть
должны и их должно быть много, чтобы любому человеку было понятно, о чем идет речь.

"""

# Лишние комментарии, не имеющие никакого смысла для проекта или из шаблонов,
# можно и поудалять - зачем они?
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,platform,pymysql
import locale
from django.utils.translation import ugettext_lazy as _
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '79eg5p)7e-ss3)8rifb-gd&2gb_+4!owc3#aq$_tsnws28cna3'

# Это на момент отладки - нужно и важно. Эта опция дает на экран не просто
# "Ошибка такая-то", она расписывает подробно, где и из-за чего произошла
# ошибка. Потом, на Production версии, эту опцию можно выключить.

DEBUG = True

# Вот это вот - зачем? Вы только что запретили вход в Ваше приложение
# со всех остальных хостов, кроме локального. А зачем же Вы тогда
# пишете приложение, если запрещаете народу в него заходить?

#ALLOWED_HOSTS = ['127.0.0.1:8000']

# Директорий, в котором располагается сам проект. Нужен для
# формирования полных абсолютных путей к файлам. Можно и без него, но так
# будет удобнее.

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__)) + "/../"

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.utils.translation',
    'moda',

    #'django_ajax',
    #'django.contrib.sites',



)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
)

# Нужно понимать прямо по одной строке, что Вы делаете и зачем.
# activation_days Вам либо вообще не понадобится, либо понадобится - очень
# и очень не скоро!

# ACCOUNT_ACTIVATION_DAYS=7
# LOGIN_URL = 'django.contrib.auth.views.login'
# ROOT_URLCONF = 'moda.urls'

# Уже есть такое по смыслу, PROJECT_DIR, см. выше.
#BASE_DIR=os.path.abspath(os.path.dirname((__file__)))

# Не надо, думаю, хватит одной переменной STATIC_URL
#STATICFILES_DIRS=(os.path.join(BASE_DIR,"static"),
#                  )

# Здесь будут лежать "статические файлы". То есть такие файлы,
# содержание которых не меняется во времени. Картинки, скрипты и т.д.

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join( PROJECT_DIR, "static" ),
)
########################################################################################################
LOGIN_URL = '/ajax_login/'
LOGIN_REDIRECT_URL = '/'

########################################################################################################################

WSGI_APPLICATION = 'moda.wsgi.application'
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True
AUTHENTICATION_BACKENDS=('django.contrib.auth.backends.ModelBackend',)
MEDIA_ROOT=os.path.join(PROJECT_DIR, "static/media")
MEDIA_URL='/media/'
AUTH_PROFILE_MODULE="userprofile.UserProfile"


########################################################################################################################
# Как сделать трансляцию:
# 1. Нужно поставить себе пакет gettext. Это - GNU пакет, то есть его надо поставить - в cygwin. Снова идем
# в cygwin64, запускаем setup-x86_64. Если при этом заругается, что версия setup не совпадает с имеющимися файлкми (
# его собственной "базой данных" - нужно сходить на cygwin и стащить оттуда setup поновее. Запустили, в окне выбора
# пакетов набираем gettext, и в секции text выбираем крыжиком
#
#         gettext : GNU internationalization library and core utilites.
#
# Еще я себе поставил из секции devel, скорее всего, он понадобится:
#
#         gettext-devel : GNU internationalization development utilites
#
# 2. Я Вам много говорил о "ресурсах". И даже нашел что-то в Вашем проекте, но непонятно, откуда Вы это
# взяли. Вот Вы что-то писали-писали - ок, дошли до перевода. Исходными данными являются - Ваши тексты
# программ и шаблонов. Чтобы создать ресурс, набираем на клавиатуре, стоя в дереве проекта (для русского):
#
#         django-admin makemessages -l ru
#
# 3. Идем в получившийся ресурс. Он лежит в каталоге locale/имя_языка/LC_MESSAGES/django.po.
# Делаем ему перевод. То есть msgid оставляем как есть, а вот вместо msgstr вбиваем то, что хотели получить
# на не-английском языке. Важно! У файла должна быть кодировка - UTF-8, иначе будут ошибки.
#
# 4. Полученный ресурс нужно оттранслировать, сделать из него файлик django.mo. Делается это при помощи команды
#
#         django-amdin compilemessages
#
# опять же стоя в каталоге самого проекта (именно там, где и лежит каталог locale)
#
# Все. На экране оно появится - само, уже переведенное.
#

# Что нужно для трансляции (перевода на другие языки)
USE_I18N = True
USE_L10N = True
LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, "locale" ),
)


TIME_ZONE = 'Asia/Ulaanbaatar'
USE_TZ = True

# Где лежат файлы шаблонов.
TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[
            os.path.join(PROJECT_DIR, "templates")
        ],
        'APP_DIRS':True,
        'OPTIONS':{
            'context_processors':[
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]



LANGUAGES=(
    ('en',_('English')),

)
LANGUAGE_CODE='en'
# Нельзя указывать в проекте абсолютные пути. Когда Вы поставите
# приложение на сервер, там вообще не будет диска c:,
# на серверных платформах нет "дисков".

# DJANGO_SETTINGS_MODULE="c:/work/moda/moda/setiings.py"

ROOT_URLCONF = "moda.urls"

########################################################################################################################
#                                                                                                                      #
#                                              Подключение базы данных.                                                #
#                  Не исключаем, что баз в итоге может быть не одна, поэтому я сделал по default.                      #
#          Это - общее определение. И здесь ничего менять не нужно. Если нужно поставить своего собственного           #
#                               пользователя, пароль, имя базы и т.д. - см. файлик config.py.                          #
#                                                                                                                      #
########################################################################################################################

#DATABASES = {
#    'default' : {
#        'ENGINE' : 'django.db.backends.mysql',
#        'NAME'   : 'khaliunaa',
#        'HOST'   : '127.0.0.1',
#        'PORT'   : 3306,
#        'USER'   : 'root',
#        'PASSWORD' : 'uragshaa123',
#        'STORAGE_ENGINE': 'INNODB'
#    },

#}

DATABASES = {
    'default' : {
        'ENGINE' : 'mysql.connector.django',
 #       'ENGINE' : 'django.db.backends.mysql',
        'NAME'   : 'moda',
        'HOST'   : 'localhost',
        'PORT'   : 3306,
        'USER'   : 'haliuna',
        'PASSWORD' : '123456',
        'STORAGE_ENGINE': 'INNODB'
    },

}

DEFAULT_CHARSET = 'UTF-8'

# Импорт перекрытия установок для конкретных компьютеров.
# должен быть в файле - самым последним оператором. Сначала
# полностью все объявили, потом перекрыли - только
# нужное и только для того компьютера, на котором прямо сейчас
# запустилость приложение.
#################################Email##################################################
############################################################################################
if DEBUG:
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_HOST_USER='fashionmongoliasite@gmail.com'
    EMAIL_HOST_PASSWORD='uragshaa'
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    DEFAULT_FROM_EMAIL=EMAIL_HOST_USER

##################Search settings###########################33
############################################################

from moda.config import *
