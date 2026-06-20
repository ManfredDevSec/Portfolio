from django.core.management.base import BaseCommand
from apps.core.models import Skill


class Command(BaseCommand):
    help = 'Seed the Skills table with DarkTrace\'s tech stack'

    SKILLS = [
        ('Django REST Framework', 'framework', 'Primary framework', 1),
        ('FastAPI', 'framework', 'Async APIs', 2),
        ('PostgreSQL', 'database', 'Production database', 3),
        ('Redis', 'database', 'Caching & task queues', 4),
        ('Celery', 'infra', 'Background task processing', 5),
        ('Render', 'infra', 'Deployment', 6),
        ('AWS Elastic Beanstalk', 'infra', 'Deployment', 7),
        ('Neon', 'database', 'Serverless Postgres', 8),
        ('Paystack', 'service', 'Payment processing', 9),
        ('Expo Push', 'service', 'Mobile notifications', 10),
        ('Wigal SMS', 'service', 'SMS delivery', 11),
        ('Cloudinary', 'service', 'Media storage', 12),
        ('Jazzmin', 'other', 'Admin dashboard theming', 13),
        ('WebSockets', 'other', 'Real-time features', 14),
        ('Python', 'language', 'Primary language', 15),
    ]

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for name, category, label, order in self.SKILLS:
            skill, created = Skill.objects.update_or_create(
                name=name,
                defaults={
                    'category': category,
                    'label': label,
                    'order': order,
                    'is_active': True,
                }
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created: {name}'))
            else:
                updated_count += 1
                self.stdout.write(f'Updated: {name}')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone. {created_count} created, {updated_count} updated.'
        ))
