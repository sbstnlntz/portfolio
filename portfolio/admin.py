# Ensure translation options are loaded
import portfolio.translation

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    SiteMeta,
    Section,
    Project,
    Skill,
    ContactInfo,
    Tag,
    Imprint,
)

# ============================================================
# Basic model registrations (no translation needed)
# ============================================================
admin.site.register(SiteMeta)
admin.site.register(ContactInfo)
admin.site.register(Tag)

# ============================================================
# Translated Admin Interfaces
# These use django-modeltranslation's TranslationAdmin
# ============================================================

@admin.register(Section)
class SectionAdmin(TranslationAdmin):
    list_display = ("slug", "title")  # Show slug and translated title

@admin.register(Skill)
class SkillAdmin(TranslationAdmin):
    list_display = ("name", "level")  # Show name and skill level

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ("title", "order")  # Show title and display order
    filter_horizontal = ("tags",)      # Better UX for selecting tags

@admin.register(Imprint)
class ImprintAdmin(TranslationAdmin):
    fields = ("content_de", "content_en")  # Explicit fields to show in admin form
