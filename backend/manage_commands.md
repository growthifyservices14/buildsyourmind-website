# Builds Your Mind - Backend Commands

## Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver

## Admin Panel
URL: http://localhost:8000/admin/
Default: admin / admin123

## API Endpoints
- GET  /api/settings/              - Site settings
- GET  /api/testimonials/          - Testimonials
- GET  /api/gallery/               - Gallery images
- POST /api/newsletter/            - Subscribe newsletter

- GET  /api/products/categories/   - Product categories
- GET  /api/products/              - Products list
- GET  /api/products/{slug}/       - Product detail

- GET  /api/workshops/list/        - Workshops
- POST /api/workshops/bookings/    - Book workshop

- GET  /api/tuition/subjects/      - Subjects
- GET  /api/tuition/teachers/      - Teachers
- POST /api/tuition/apply/         - Parent tuition application
- POST /api/tuition/register-teacher/ - Teacher registration

- POST /api/enquiries/enquiry/     - General enquiry
- POST /api/enquiries/school-inquiry/ - School inquiry
