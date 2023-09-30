import json
from django.core.management.base import BaseCommand
from quoteapp.models import MyModel

class Command(BaseCommand):
    help = 'Імпортувати дані з JSON файлів'

    def handle(self, *args, **kwargs):
        json_files = ['author_data.json', 'contact_data.json', 'quote_data.json']

        for json_file in json_files:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)

            for item in data:
                my_model = MyModel()
                for key, value in item.items():
                    setattr(my_model, key, value)
                my_model.save()
                self.stdout.write(self.style.SUCCESS(f'Успішно імпортовано {my_model} з {json_file}'))
