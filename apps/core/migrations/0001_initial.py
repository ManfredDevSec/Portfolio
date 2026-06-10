from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('framework','Framework'),('database','Database'),('infra','Infrastructure'),('service','Third-party Service'),('language','Language'),('other','Other')], default='other', max_length=50)),
                ('label', models.CharField(help_text='Short descriptor e.g. "Primary framework"', max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['order', 'name'], 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('year_range', models.CharField(help_text='e.g. "2024–now" or "2022–2024"', max_length=30)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['order'], 'verbose_name': 'Experience', 'verbose_name_plural': 'Experience'},
        ),
        migrations.CreateModel(
            name='ContactLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('value', models.CharField(help_text='Display text e.g. "github.com/darktrace"', max_length=200)),
                ('url', models.CharField(help_text='Full URL or "mailto:" address', max_length=300)),
                ('icon', models.CharField(choices=[('email','Email'),('github','GitHub'),('linkedin','LinkedIn'),('twitter','Twitter / X'),('location','Location'),('website','Website'),('other','Other')], default='other', max_length=20)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['order'], 'verbose_name': 'Contact Link', 'verbose_name_plural': 'Contact Links'},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('tagline', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('active','In Development'),('launched','Launched'),('archived','Archived')], default='active', max_length=20)),
                ('tags', models.ManyToManyField(blank=True, related_name='projects', to='core.skill')),
                ('tech_tags', models.CharField(blank=True, help_text='Comma-separated tags not in Skills list', max_length=500)),
                ('github_url', models.URLField(blank=True)),
                ('live_url', models.URLField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['order', '-created_at'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
