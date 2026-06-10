from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Skill, Experience, ContactLink


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'label', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
    ordering = ['order', 'name']


class SkillInline(admin.TabularInline):
    model = Project.tags.through
    extra = 1
    verbose_name = 'Skill Tag'
    verbose_name_plural = 'Skill Tags'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status_badge', 'is_featured', 'order', 'updated_at']
    list_editable = ['is_featured', 'order']
    list_filter = ['status', 'is_featured']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', '-created_at']
    inlines = [SkillInline]
    exclude = ['tags']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'tagline', 'status', 'is_featured', 'order')
        }),
        ('Content', {
            'fields': ('description', 'tech_tags')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url'),
            'classes': ('collapse',),
        }),
    )

    def status_badge(self, obj):
        colors = {
            'active': '#1D9E75',
            'launched': '#378ADD',
            'archived': '#888780',
        }
        color = colors.get(obj.status, '#888')
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 8px;border-radius:4px;font-size:11px">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Status'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'year_range', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['role', 'company']
    ordering = ['order']


@admin.register(ContactLink)
class ContactLinkAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'icon', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']
