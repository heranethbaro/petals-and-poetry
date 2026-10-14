# Petals and Poetry

A simple five-page Django website for a flower shop that sells bouquets,
offers flower arrangement workshops, and runs a small library.

## Pages
- Home
- About
- Services & Products
- Gallery
- Contact

## Features
- Template inheritance with `base.html`
- Navbar and footer as separate `{% include %}` files
- Navigation built with `{% url %}` tags
- CSS and images served with `{% static %}`
- Responsive, light and dark mode design

## How to run
```bash
git clone <your-repo-url>
cd ISAE101FinalProject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
Then open http://127.0.0.1:8000/

## Author/s
Heraneth F. Baro
Princess Dianah Lucena
Kristhel V. Obille