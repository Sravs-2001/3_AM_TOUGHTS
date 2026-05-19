import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from mainapp.models import Concept

concepts = [
    {
        "title": "Models & ORM",
        "description": "Models are the single source of truth about your data. The ORM lets you interact with your database using Python instead of writing raw SQL.",
        "icon": "🗄️"
    },
    {
        "title": "Views (Logic)",
        "description": "Views are the brain of your application. They receive the web request from the user, fetch data from Models, perform logic, and decide which Template should be shown to the user.",
        "icon": "🧠"
    },
    {
        "title": "Templates (UI)",
        "description": "Templates handle what the user actually sees. It's HTML mixed with special Django tags that allow you to inject dynamic data directly into the page layout.",
        "icon": "🎨"
    },
    {
        "title": "URLs (Routing)",
        "description": "The URL dispatcher acts like a traffic cop. When a user visits a specific web address, the URL configuration directs the request to the correct View function.",
        "icon": "🛣️"
    },
    {
        "title": "The Admin Panel",
        "description": "One of Django's most legendary features. It automatically reads your Models and generates a beautiful, production-ready administrative interface.",
        "icon": "👑"
    },
    {
        "title": "Forms & Validation",
        "description": "Django provides a rich framework to securely generate HTML forms, validate user input, and easily save that data into the database.",
        "icon": "📝"
    },
    {
        "title": "Authentication",
        "description": "A built-in system to handle user login, logout, passwords, and permissions out-of-the-box, ensuring your app is secure.",
        "icon": "🔐"
    },
    {
        "title": "Middleware",
        "description": "Low-level plugins that run on every request before it hits the View. We used a custom Middleware to bypass the Admin login!",
        "icon": "⚙️"
    },
    {
        "title": "Static Files",
        "description": "How Django handles serving external assets like CSS stylesheets, JavaScript files, and Images to the user's browser.",
        "icon": "🖼️"
    }
]

Concept.objects.all().delete()
for c in concepts:
    Concept.objects.create(**c)

print("Database seeded with ALL topics!")
