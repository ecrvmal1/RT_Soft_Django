import csv
import os
from config.settings import BASE_DIR
from mainapp.models import Category
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "This command is using to import categories to Database"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        # inp_filename = os.path.join(BASE_DIR, 'gen_csv','input_data.csv' )
        inp_filename = options['csv_file']
        categ_list = []
        with open(inp_filename, mode='r', encoding='utf-8') as inp_file:
            f_reader = csv.reader(inp_file, delimiter=';')
            for line in f_reader:
                print(line)
                for el in line[2:]:
                    # print(el)
                    if el not in categ_list:
                        categ_list.append(el)

        for el in categ_list:
            cat = Category()
            cat.name = el
            cat.save()
            print(f'Category {el} saved')

