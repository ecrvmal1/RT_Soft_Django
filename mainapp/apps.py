from django.apps import AppConfig


class MainappConfig(AppConfig):
    name = 'mainapp'
    all_categs_dict = {}

    def ready(self):
        print('get_keys runs')
        from mainapp import models
        all_categs = models.Category.objects.all()
        for el in all_categs:
            # print(el.id, el.name)
            self.all_categs_dict[el.name] = int(el.id)