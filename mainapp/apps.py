import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_name.settings")
django.setup()

# from django.apps import AppConfig
from mainapp import models

class MainappConfig():
# class MainappConfig(AppConfig):
#     name = 'mainapp'
    all_categs_dict = {}

    def ready(self):
        print('get_keys runs')
        # from mainapp import models
        all_categs = models.Category.objects.all()
        for el in all_categs:
            # print(el.id, el.name)
            self.all_categs_dict[el.name] = int(el.id)