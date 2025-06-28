from django.test import TestCase
from .models import Section, Skill, Project, Tag, ContactInfo, SiteMeta, Imprint


# ===============================
# Section Model Tests
# ===============================
class SectionModelTest(TestCase):
    """
    Tests for the Section model.
    """

    def test_str_returns_title(self):
        section = Section.objects.create(slug='about', title='About Me', content='Lorem ipsum')
        self.assertEqual(str(section), 'About Me')

    def test_image_field_can_be_null(self):
        section = Section.objects.create(slug='intro', title='Intro', content='Welcome')
        self.assertIsNone(section.image)


# ===============================
# Skill Model Tests
# ===============================
class SkillModelTest(TestCase):
    """
    Tests for the Skill model.
    """

    def test_str_returns_name_and_level(self):
        skill = Skill.objects.create(name='Python', level=90)
        self.assertEqual(str(skill), 'Python (90%)')

    def test_default_skill_level_is_zero(self):
        skill = Skill.objects.create(name='HTML')
        self.assertEqual(skill.level, 0)


# ===============================
# Tag Model Tests
# ===============================
class TagModelTest(TestCase):
    """
    Tests for the Tag model.
    """

    def test_str_returns_tag_name(self):
        tag = Tag.objects.create(name='Django')
        self.assertEqual(str(tag), 'Django')

    def test_tag_name_is_unique(self):
        Tag.objects.create(name='React')
        with self.assertRaises(Exception):
            Tag.objects.create(name='React')


# ===============================
# Project Model Tests
# ===============================
class ProjectModelTest(TestCase):
    """
    Tests for the Project model.
    """

    def test_str_returns_project_title(self):
        project = Project.objects.create(title='My Project', description='Test', order=1)
        self.assertEqual(str(project), 'My Project')

    def test_projects_are_ordered_by_order_field(self):
        p1 = Project.objects.create(title='First', description='desc', order=2)
        p2 = Project.objects.create(title='Second', description='desc', order=1)
        projects = list(Project.objects.all())
        self.assertEqual(projects[0], p2)
        self.assertEqual(projects[1], p1)

    def test_project_can_have_multiple_tags(self):
        tag1 = Tag.objects.create(name='React')
        tag2 = Tag.objects.create(name='Docker')
        project = Project.objects.create(title='Web App', description='desc', order=1)
        project.tags.set([tag1, tag2])
        self.assertEqual(project.tags.count(), 2)

    def test_project_repo_missing_flag(self):
        project = Project.objects.create(title='Private', description='desc', order=1, repo_missing=True)
        self.assertTrue(project.repo_missing)


# ===============================
# ContactInfo Model Tests
# ===============================
class ContactInfoModelTest(TestCase):
    """
    Tests for the ContactInfo model.
    """

    def test_all_fields_can_be_blank(self):
        contact = ContactInfo.objects.create()
        self.assertIsNone(contact.email)
        self.assertIsNone(contact.phone)
        self.assertIsNone(contact.github)
        self.assertIsNone(contact.whatsapp)
        self.assertIsNone(contact.linkedin)

    def test_str_returns_fixed_label(self):
        contact = ContactInfo.objects.create(email='info@example.com')
        self.assertEqual(str(contact), "Contact Information")


# ===============================
# SiteMeta Model Tests
# ===============================
class SiteMetaModelTest(TestCase):
    """
    Tests for the SiteMeta model.
    """

    def test_str_returns_meta_label(self):
        meta = SiteMeta.objects.create()
        self.assertEqual(str(meta), "Website Meta Information")

    def test_meta_has_default_values(self):
        meta = SiteMeta.objects.create()
        self.assertEqual(meta.title, "My Portfolio")
        self.assertEqual(meta.copyright_name, "Max Mustermann")
        self.assertEqual(meta.copyright_year, "2025")


# ===============================
# Imprint Model Tests
# ===============================
class ImprintModelTest(TestCase):
    """
    Tests for the Imprint model.
    """

    def test_str_returns_impressum_label(self):
        imprint = Imprint.objects.create(content="Some legal content")
        self.assertEqual(str(imprint), "Impressum")
