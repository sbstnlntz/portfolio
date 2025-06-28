from django.shortcuts import render
from .models import SiteMeta, Section, Skill, Project, ContactInfo, Imprint


def home(request):
    """
    Renders the main landing page of the portfolio site.

    Loads and prepares content for:
    - Meta information for title and footer
    - The four defined content sections in specific order (slug-based)
    - Skills for the skills section (used with rotating icons)
    - Projects for the slider (with head/tail clones for infinite looping)
    - Contact information for dynamic icon rendering
    - Legal imprint text (displayed in modal)

    Context passed to the template:
    - meta: SiteMeta instance (title, copyright)
    - sections: Dict of Section objects mapped by slug
    - slugs: Display order of section slugs
    - skills: All Skill entries
    - projects: All projects with first and last clones
    - contact: ContactInfo instance
    - imprint: Imprint instance
    """

    # ============================================================
    # Fetch global metadata and imprint
    # ============================================================
    meta = SiteMeta.objects.first()
    imprint = Imprint.objects.first()

    # ============================================================
    # Define and fetch required sections by slug
    # ============================================================
    slugs = ['intro', 'skills', 'projects', 'contact']
    section_qs = Section.objects.filter(slug__in=slugs)
    section_map = {section.slug: section for section in section_qs}

    # ============================================================
    # Fetch supporting data
    # ============================================================
    skills = Skill.objects.all()
    contact = ContactInfo.objects.first()

    # ============================================================
    # Fetch projects and add clones for seamless carousel effect
    # ============================================================
    original_projects = list(Project.objects.all())
    if original_projects:
        projects = [original_projects[-1]] + original_projects + [original_projects[0]]
    else:
        projects = []

    # ============================================================
    # Final render call
    # ============================================================
    return render(request, 'portfolio/home.html', {
        'meta': meta,
        'sections': section_map,
        'slugs': slugs,
        'skills': skills,
        'projects': projects,
        'contact': contact,
        'imprint': imprint,
    })
