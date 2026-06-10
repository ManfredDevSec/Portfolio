# DarkTrace — Portfolio

Personal portfolio and project showcase. Built with Django REST Framework on the backend, Django templates on the frontend, and PostgreSQL (Neon) as the database. All content — projects, skills, experience, and contact links — is managed through the admin dashboard.

## Tech Stack

- **Backend:** Django 5.1, Django REST Framework
- **Database:** PostgreSQL via [Neon](https://neon.tech)
- **Admin:** Jazzmin
- **Static files:** WhiteNoise
- **Deployment:** Render

## API

All endpoints are read-only and public.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/portfolio/` | All portfolio data in one call |
| GET | `/api/projects/` | Projects list |
| GET | `/api/projects/<slug>/` | Single project |
| GET | `/api/skills/` | Skills / tech stack |
| GET | `/api/experience/` | Work experience |
| GET | `/api/contact/` | Contact links |

## Project Structure

```
portfolio/
├── apps/
│   └── core/               # Models, serializers, views, admin
├── portfolio/
│   └── settings/
│       ├── base.py
│       ├── development.py
│       └── production.py
├── templates/
│   ├── base.html
│   └── core/
│       ├── index.html
│       └── project_detail.html
├── static/
│   ├── css/main.css
│   └── js/main.js
├── build.sh
└── manage.py
```

## License

MIT