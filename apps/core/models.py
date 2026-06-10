from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('framework', 'Framework'),
        ('database', 'Database'),
        ('infra', 'Infrastructure'),
        ('service', 'Third-party Service'),
        ('language', 'Language'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    label = models.CharField(max_length=100, help_text='Short descriptor e.g. "Primary framework"')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'In Development'),
        ('launched', 'Launched'),
        ('archived', 'Archived'),
    ]

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    tags = models.ManyToManyField(Skill, blank=True, related_name='projects')
    tech_tags = models.CharField(
        max_length=500, blank=True,
        help_text='Comma-separated tags that are not in the Skills list e.g. "Deep Links, ASGI"'
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def get_all_tags(self):
        skill_tags = list(self.tags.values_list('name', flat=True))
        extra = [t.strip() for t in self.tech_tags.split(',') if t.strip()]
        return skill_tags + extra


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    year_range = models.CharField(max_length=30, help_text='e.g. "2024–now" or "2022–2024"')
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f'{self.role} @ {self.company}'


class ContactLink(models.Model):
    ICON_CHOICES = [
        ('email', 'Email'),
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter / X'),
        ('location', 'Location'),
        ('website', 'Website'),
        ('other', 'Other'),
    ]

    label = models.CharField(max_length=50)
    value = models.CharField(max_length=200, help_text='Display text e.g. "github.com/darktrace"')
    url = models.CharField(max_length=300, help_text='Full URL or "mailto:" address')
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='other')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Contact Link'
        verbose_name_plural = 'Contact Links'

    def __str__(self):
        return f'{self.label}: {self.value}'
