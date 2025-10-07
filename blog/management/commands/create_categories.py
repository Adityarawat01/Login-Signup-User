from django.core.management.base import BaseCommand
from blog.models import Category

class Command(BaseCommand):
    help = 'Create default blog categories'

    def handle(self, *args, **options):
        categories = [
            'Mental Health',
            'Heart Disease',
            'Covid19',
            'Immunization'
        ]
        
        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category already exists: {category_name}'))
