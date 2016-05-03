import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tangoWithDjango.settings")

import django
django.setup()

from rango.models import Category, Page


def delete_data():
    cate = Category.objects.all()
    page = Page.objects.all()
    cate.delete()
    page.delete()


if __name__ =='__main__':
    delete_data()