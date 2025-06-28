from django.db import models


class SiteMeta(models.Model):
    """
    Stores basic metadata for the website, such as the page title and copyright info.
    This data is used in the <title> tag and the footer.
    """
    title = models.CharField(max_length=200, default="My Portfolio")
    copyright_name = models.CharField(max_length=200, default="Max Mustermann")
    copyright_year = models.CharField(max_length=4, default="2025")

    def __str__(self):
        return "Website Meta Information"


class Section(models.Model):
    """
    Defines a content section of the landing page, such as intro, skills, projects, or contact.
    Each section is identified by a unique slug and can optionally include an image.
    """
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='section_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    """
    Represents a technical skill, such as a programming language or tool.
    The skill's icon is typically derived from the name.
    """
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=0)  # Represented as a percentage (0–100)

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class Tag(models.Model):
    """
    Used to categorize projects (e.g. 'Django', 'React', 'API').
    Tags are shown below project cards if available.
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Represents a portfolio project.
    Includes description, tech stack, tags, optional image, and external links.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    repo_missing = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    """
    Stores contact methods for the contact section.
    Fields are optional and only rendered if present.
    """
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Contact Information"


class Imprint(models.Model):
    """
    Stores legal imprint content, shown in a modal when requested.
    Multilingual content is handled via modeltranslation.
    """
    content = models.TextField()

    def __str__(self):
        return "Impressum"
