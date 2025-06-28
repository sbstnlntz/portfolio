from modeltranslation.translator import register, TranslationOptions
from .models import Section, Project, Skill, Imprint

@register(Section)
class SectionTranslationOptions(TranslationOptions):
    """
    Defines translatable fields for the Section model.
    """
    fields = ('title', 'content')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    """
    Defines translatable fields for the Project model.
    """
    fields = ('title', 'description')


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    """
    Defines translatable fields for the Skill model.
    """
    fields = ('name',)


@register(Imprint)
class ImprintTranslationOptions(TranslationOptions):
    """
    Defines translatable fields for the Imprint model.
    """
    fields = ('content',)
