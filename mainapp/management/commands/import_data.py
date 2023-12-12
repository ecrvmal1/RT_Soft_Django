import csv
import os
from config.settings import BASE_DIR
from mainapp.models import Category, Record
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "This command is using to import record data to Database"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        all_categs = Category.objects.all()
        all_categs_dict = {}
        for el in all_categs:
            print(el.id, el.name)
            all_categs_dict[el.name] = int(el.id)

        # inp_filename = os.path.join(BASE_DIR, 'gen_csv','input_data.csv' )
        inp_filename = options['csv_file']
        with open(inp_filename, mode='r', encoding='utf-8') as inp_file:
            f_reader = csv.reader(inp_file, delimiter=';')
            for line in f_reader:
                print(line)
                categ_set = set()
                r = Record()
                r.file_url = line[0]
                r.num_of_show = line[1]
                r.save()
                for el in line[2:]:
                    # print(el)
                    r.category.add(all_categs_dict[el])
                # r.category.add(categ_set)
                r.category.save()
                # r.save()
                print(f'record {r} saved')
