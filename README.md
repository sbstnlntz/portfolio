# Portfolio Website (Django)

This is a personal portfolio website built with Django. It features a scroll-snapping single-page layout with sections for introduction, skills, projects, and contact — all editable through the Django admin interface.

## Features

- Scroll-snapping layout with full-screen sections
- Admin-managed content: site metadata, sections, skills, projects, and contact links
- Project slider with seamless infinite loop
- Skill icons with animated transitions and progress indicators
- Responsive design for desktop and mobile
- Timeline navigation and fullscreen mobile menu

## Technologies Used

- Django (Python)
- HTML, CSS, JavaScript
- SQLite (default; configurable to PostgreSQL/MySQL)

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/sbstnlntz/portfolio.git
   cd your-portfolio
   ```

2. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Apply migrations and create a superuser**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Open `http://localhost:8000` to view the site, and `http://localhost:8000/admin/` to manage the content.

## Admin Content Management

- **Site Metadata**: Website title, copyright
- **Sections**: Intro, Skills, Projects, Contact (content + optional image)
- **Skills**: Name and proficiency (0–100%)
- **Projects**: Title, description, tech stack, tags, link, image, sort order
- **Contact Info**: Email, phone, WhatsApp, GitHub, LinkedIn

## Running Tests

Basic unit tests for models:

```bash
python manage.py test
```

## License

This project is open-source under the MIT License.
