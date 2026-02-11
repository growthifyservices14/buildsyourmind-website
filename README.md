# Builds Your Mind - Full Stack Website

Complete website with **Two Modes** as per the Builds Your Mind specification:

## Mode 1: Education Kits & Workshops (B2B + B2C)

- Online store for STEM, Robotics, IoT, Science kits
- Products for Play Schools, Schools, and Colleges
- B2C direct purchase + B2B bulk order system
- Workshop booking system for schools/colleges
- OEM/ODM manufacturing inquiry
- Distributor & Retailer partner programs

## Mode 2: Home Tuition (Service Platform)

- Parent online application for home tuition
- Teacher registration and verification
- Subject-wise and location-based matching
- Teacher profiles display

## Website Structure

1. **Home** - Overview of both modes with CTAs
2. **Education Kits & Workshops** - Products, Workshops, OEM, ODM
3. **Home Tuition** - Parent application & Teacher registration
4. **For Schools / Partners** - School inquiry, Distributor, Retailer
5. **About Builds Your Mind** - Company story, values, eco-commitment
6. **Contact / Apply Now** - General enquiry form

---

## Tech Stack

- **Frontend**: React 18 + Vite + Tailwind CSS + Framer Motion
- **Backend**: Django 4.2 + Django REST Framework
- **Database**: SQLite (dev) / MySQL (production)

---

## Quick Start

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

Admin: http://localhost:8000/admin/ (admin / admin123)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173/

---

## API Endpoints

### Core

- `GET /api/settings/` - Site settings
- `GET /api/testimonials/` - Testimonials
- `POST /api/newsletter/` - Subscribe

### Products

- `GET /api/products/categories/` - Categories
- `GET /api/products/` - Product list (filterable)
- `GET /api/products/{slug}/` - Product detail

### Workshops

- `GET /api/workshops/list/` - All workshops
- `POST /api/workshops/bookings/` - Book workshop

### Home Tuition

- `GET /api/tuition/subjects/` - Subjects
- `GET /api/tuition/teachers/` - Active teachers
- `POST /api/tuition/apply/` - Parent application
- `POST /api/tuition/register-teacher/` - Teacher registration

### Enquiries

- `POST /api/enquiries/enquiry/` - General enquiry
- `POST /api/enquiries/school-inquiry/` - School inquiry

---

## Production Deployment

### Backend

1. Set environment variables:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS`
   - `CORS_ALLOWED_ORIGINS`
   - Database credentials (PostgreSQL)
2. Run: `gunicorn config.wsgi:application`

### Frontend

1. Set `VITE_API_URL` to production API URL
2. Build: `npm run build`
3. Serve the `dist/` folder via Nginx

---

## Color Scheme

- Primary Blue: `#1E3A8A`
- Blue Light: `#2E4A9A`
- Orange: `#F97316`
- Orange Dark: `#EA580C`
- Cream/Background: `#F8FAFC`
- Gray: `#1F2933`
