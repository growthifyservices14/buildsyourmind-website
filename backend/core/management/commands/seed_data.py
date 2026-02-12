from django.core.management.base import BaseCommand
from products.models import Category, Product
from workshops.models import Workshop
from tuition.models import Subject
from core.models import SiteSettings, Testimonial


class Command(BaseCommand):
    help = 'Seed initial data with all PDF requirements'

    def handle(self, *args, **options):
        # Site Settings - PDF Official Tagline
        SiteSettings.objects.get_or_create(
            pk=1,
            defaults={
                'site_name': 'Builds Your Mind',
                'tagline': 'Smart, Eco-Friendly Learning Kits & Classroom Solutions',
                'email': 'buildsyourmind@gmail.com',
                'phone': '+91 91097 11321',
                'whatsapp': '+91 91097 11321',
                'address': 'Harmono Pvt. Ltd., Indore, Madhya Pradesh, India',
            }
        )

        # Categories - All 8 Categories
        cats = {
            'stem': Category.objects.get_or_create(slug='stem', defaults={'name': 'STEM Learning Kits', 'order': 1, 'description': 'Science, Technology, Engineering & Math learning kits'})[0],
            'robotics': Category.objects.get_or_create(slug='robotics', defaults={'name': 'Robotics Kits', 'order': 2, 'description': 'Build and program robots'})[0],
            'iot': Category.objects.get_or_create(slug='iot', defaults={'name': 'IoT Kits', 'order': 3, 'description': 'Internet of Things learning kits'})[0],
            'science': Category.objects.get_or_create(slug='science', defaults={'name': 'Science Kits', 'order': 4, 'description': 'Physics, Chemistry, Biology experiment kits'})[0],
            'electronics': Category.objects.get_or_create(slug='electronics', defaults={'name': 'Electronics Kits', 'order': 5, 'description': 'Electronics and Arduino learning kits'})[0],
            'creative': Category.objects.get_or_create(slug='creative', defaults={'name': 'Mind Development & Creative', 'order': 6, 'description': 'Creative and cognitive development kits'})[0],
            # NEW CATEGORIES FOR PDF REQUIREMENTS
            'smart_classroom': Category.objects.get_or_create(slug='smart-classroom-solutions', defaults={'name': 'Smart Classroom Solutions', 'order': 7, 'description': 'Smart speakers, projectors and classroom technology'})[0],
            'wooden_toys': Category.objects.get_or_create(slug='wooden-toys', defaults={'name': 'Eco-Friendly Wooden Toys', 'order': 8, 'description': 'Sustainable wooden toys for early learning'})[0],
        }

        # Products - Existing + New Products
        products_data = [
            # EXISTING PRODUCTS
            {'name': 'Basic Electronics Kit', 'slug': 'basic-electronics-kit', 'category': cats['electronics'],
             'short_description': 'Learn basic electronics with hands-on experiments',
             'description': 'Comprehensive kit for learning electronics fundamentals. Perfect for schools and home learning.',
             'age_group': '8-12', 'target_audience': 'school', 'price': 1499, 'bulk_price': 1199, 'is_featured': True,
             'features': ['All components included', 'Step-by-step manual', 'Safe components', 'QR video tutorials']},
            
            {'name': 'Solar System Model Kit', 'slug': 'solar-system-model-kit', 'category': cats['stem'],
             'short_description': 'Build your own solar system model',
             'description': 'Learn astronomy by building a detailed solar system model. Made in India with eco-friendly materials.',
             'age_group': '5-8', 'target_audience': 'home', 'price': 999, 'bulk_price': 799, 'is_featured': True,
             'features': ['Glow-in-dark planets', 'Educational booklet', 'Easy assembly', 'Made in India']},
            
            {'name': 'Robotics Starter Kit', 'slug': 'robotics-starter-kit', 'category': cats['robotics'],
             'short_description': 'Introduction to robotics and programming',
             'description': 'Build and program your first robot. Complete kit for beginners with all components and detailed guide.',
             'age_group': '12-16', 'target_audience': 'school', 'price': 2999, 'bulk_price': 2499, 'is_featured': True,
             'features': ['Arduino compatible', 'Sensors included', 'Project booklet', 'Online support', 'Made in India']},
            
            {'name': 'IoT Weather Station Kit', 'slug': 'iot-weather-station-kit', 'category': cats['iot'],
             'short_description': 'Build a connected weather monitoring station',
             'description': 'Learn IoT by building a real weather station with WiFi connectivity and mobile app.',
             'age_group': '16+', 'target_audience': 'college', 'price': 3499, 'bulk_price': 2999, 'is_featured': True,
             'features': ['WiFi enabled', 'Real-time data', 'Mobile app compatible', 'Cloud integration']},
            
            {'name': 'Chemistry Experiment Kit', 'slug': 'chemistry-experiment-kit', 'category': cats['science'],
             'short_description': 'Safe chemistry experiments for home learning',
             'description': 'Learn chemistry with safe, hands-on experiments. Perfect for students and science enthusiasts.',
             'age_group': '12-16', 'target_audience': 'school', 'price': 1999, 'bulk_price': 1599,
             'features': ['50+ experiments', 'Safety equipment', 'Lab manual', 'Non-toxic materials']},
            
            {'name': 'Creative Art & Craft Kit', 'slug': 'creative-art-craft-kit', 'category': cats['creative'],
             'short_description': 'Eco-friendly art supplies for young minds',
             'description': 'Develop creativity with eco-friendly materials. Perfect for early childhood development.',
             'age_group': '3-5', 'target_audience': 'play_school', 'price': 699, 'bulk_price': 549,
             'features': ['Non-toxic materials', 'Activity guide', 'Parent tips', '100% eco-friendly']},
            
            {'name': 'Arduino Learning Kit', 'slug': 'arduino-learning-kit', 'category': cats['electronics'],
             'short_description': 'Complete Arduino programming kit',
             'description': 'Master Arduino programming from beginner to advanced. Comprehensive kit with 30+ components.',
             'age_group': '16+', 'target_audience': 'college', 'price': 3499, 'bulk_price': 2999, 'is_featured': True,
             'features': ['Arduino board', '30+ components', 'Project book', 'Online course access']},
            
            {'name': 'Physics Lab Kit', 'slug': 'physics-lab-kit', 'category': cats['science'],
             'short_description': 'Hands-on physics experiments',
             'description': 'Explore physics concepts through practical experiments. Complete lab setup for schools.',
             'age_group': '12-16', 'target_audience': 'school', 'price': 1799, 'bulk_price': 1449,
             'features': ['20+ experiments', 'Lab equipment', 'Theory guide', 'School tested']},

            # NEW PRODUCTS - SMART CLASSROOM SOLUTIONS (PDF REQUIREMENT)
            {'name': 'Smart Speaker with Built-in HD Projector', 'slug': 'smart-speaker-projector', 'category': cats['smart_classroom'],
             'short_description': 'All-in-one smart speaker and HD projector for modern classrooms',
             'description': 'Transform your classroom with our smart speaker and projector combo. Features HD projection, premium audio, wireless connectivity, and interactive learning modes. Perfect for smart classroom solutions. Made in India by Harmono Pvt. Ltd.',
             'age_group': '8-12', 'target_audience': 'school', 'price': 25000, 'bulk_price': 22000, 'is_featured': True, 'is_eco_friendly': False,
             'features': ['Built-in HD Projector (1080p)', 'Premium Stereo Speakers', 'WiFi & Bluetooth', 'Interactive Mode', 'Plug & Play', 'Multi-device Compatible', 'Made in India']},
            
            {'name': '65" Smart Interactive Teaching Panel', 'slug': 'smart-teaching-panel-65', 'category': cats['smart_classroom'],
             'short_description': '65-inch touchscreen smart panel for interactive teaching',
             'description': '65-inch interactive touchscreen panel with built-in speakers, Android OS, and pre-loaded educational apps. The ultimate smart classroom solution for modern education.',
             'age_group': '8-12', 'target_audience': 'school', 'price': 45000, 'bulk_price': 42000, 'is_featured': True, 'is_eco_friendly': False,
             'features': ['65" Touchscreen Display', 'Built-in Speakers', 'Android OS', 'Educational Apps Pre-loaded', 'Screen Mirroring', 'Multi-touch Support', 'Made in India']},
            
            {'name': 'Wireless Interactive Projector for Schools', 'slug': 'wireless-interactive-projector', 'category': cats['smart_classroom'],
             'short_description': 'Portable wireless projector with interactive features',
             'description': 'Wireless screen mirroring projector with interactive touch technology. Portable design perfect for schools and training centers.',
             'age_group': '8-12', 'target_audience': 'school', 'price': 18000, 'bulk_price': 16000, 'is_eco_friendly': False,
             'features': ['Wireless Mirroring', 'Interactive Touch', 'Portable Design', 'Long Lamp Life', 'HD Quality', 'Easy Setup']},

            # NEW PRODUCTS - WOODEN TOYS FOR PLAY SCHOOLS (PDF REQUIREMENT)
            {'name': 'Eco-Friendly Wooden Building Blocks Set', 'slug': 'wooden-building-blocks', 'category': cats['wooden_toys'],
             'short_description': 'Child-safe wooden building blocks for creative play',
             'description': 'Premium quality wooden building blocks made from sustainable wood with non-toxic paint. Perfect for play schools and early childhood development. Promotes creativity, motor skills, and problem-solving. Made in India.',
             'age_group': '3-5', 'target_audience': 'play_school', 'price': 899, 'bulk_price': 699, 'is_featured': True,
             'features': ['Sustainable Wood', 'Non-toxic Paint', 'Child Safe', 'Smooth Edges', '50+ Pieces', 'Made in India', 'BIS Certified']},
            
            {'name': 'Wooden Educational Puzzle Set', 'slug': 'wooden-puzzle-set', 'category': cats['wooden_toys'],
             'short_description': 'Eco-friendly wooden puzzles for cognitive development',
             'description': 'Set of 5 wooden puzzles including animals, numbers, alphabets, and shapes. Develops cognitive skills, hand-eye coordination, and problem-solving abilities.',
             'age_group': '3-5', 'target_audience': 'play_school', 'price': 699, 'bulk_price': 549, 'is_featured': True,
             'features': ['5 Puzzle Set', 'Eco-friendly Wood', 'Non-toxic Colors', 'Educational Design', 'Durable Quality', 'Made in India']},
            
            {'name': 'Wooden Shape Sorter Toy', 'slug': 'wooden-shape-sorter', 'category': cats['wooden_toys'],
             'short_description': 'Classic wooden shape sorting toy for toddlers',
             'description': 'Traditional shape sorter made from sustainable wood. Helps children learn shapes, colors, and develop motor skills. Perfect for play schools.',
             'age_group': '3-5', 'target_audience': 'play_school', 'price': 499, 'bulk_price': 399,
             'features': ['10 Different Shapes', 'Bright Colors', 'Smooth Finish', 'Child Safe', 'Made in India']},
            
            {'name': 'Wooden Counting & Math Learning Kit', 'slug': 'wooden-counting-kit', 'category': cats['wooden_toys'],
             'short_description': 'Wooden counting rods and number learning kit',
             'description': 'Complete math learning kit with wooden counting rods, numbers, and operation symbols. Makes early math learning fun and engaging.',
             'age_group': '3-5', 'target_audience': 'play_school', 'price': 799, 'bulk_price': 649,
             'features': ['Counting Rods', 'Wooden Numbers', 'Math Symbols', 'Storage Box', 'Activity Guide', 'Made in India']},
            
            {'name': 'Wooden Animal Kingdom Set', 'slug': 'wooden-animal-set', 'category': cats['wooden_toys'],
             'short_description': 'Hand-painted wooden animal toys for imaginative play',
             'description': 'Collection of 12 hand-painted wooden animals. Promotes imaginative play, animal recognition, and storytelling skills.',
             'age_group': '3-5', 'target_audience': 'play_school', 'price': 999, 'bulk_price': 849,
             'features': ['12 Animals', 'Hand-painted', 'Eco-friendly Wood', 'Safe for Kids', 'Imaginative Play', 'Made in India']},
            
            {'name': 'Wooden Stacking & Balancing Toy', 'slug': 'wooden-stacking-toy', 'category': cats['wooden_toys'],
             'short_description': 'Colorful wooden stacking rings for motor skill development',
             'description': 'Classic stacking rings toy made from sustainable wood. Develops motor skills, hand-eye coordination, and color recognition.',
             'age_group': '3-5', 'target_audience': 'play_school', 'price': 599, 'bulk_price': 479,
             'features': ['Colorful Rings', 'Safe Wood', 'Smooth Finish', 'Skill Development', 'Durable', 'Made in India']},
        ]

        for p in products_data:
            Product.objects.get_or_create(slug=p['slug'], defaults=p)

        # Workshops - Existing + New Coaching Programs (PDF REQUIREMENT)
        workshops_data = [
            # EXISTING WORKSHOPS
            {'title': 'STEM Discovery Workshop', 'workshop_type': 'stem', 'target_audience': 'school',
             'description': 'Interactive STEM workshop for school students. Hands-on activities covering science, technology, engineering and math concepts.',
             'duration': '3 Hours', 'max_students': 40, 'is_active': True},
            
            {'title': 'Robotics Hands-On Workshop', 'workshop_type': 'robotics', 'target_audience': 'school',
             'description': 'Build and program robots in this hands-on session. Perfect for introducing robotics to students.',
             'duration': 'Full Day', 'max_students': 30, 'is_active': True},
            
            {'title': 'IoT Workshop for Colleges', 'workshop_type': 'iot', 'target_audience': 'college',
             'description': 'Learn IoT concepts with real projects. Hands-on experience with sensors, connectivity, and cloud integration.',
             'duration': '2 Days', 'max_students': 25, 'is_active': True},
            
            {'title': 'Fun Science Workshop', 'workshop_type': 'science', 'target_audience': 'play_school',
             'description': 'Fun science activities for young learners. Age-appropriate experiments and demonstrations.',
             'duration': '2 Hours', 'max_students': 20, 'is_active': True},

            # NEW COACHING PROGRAMS (PDF REQUIREMENT)
            {'title': 'Mathematics Concept Clarity Program', 'workshop_type': 'coaching', 'target_audience': 'school',
             'description': '8-week intensive coaching program for building strong mathematics fundamentals. Covers all topics with focus on concept clarity and problem-solving skills. Suitable for Classes 6-10.',
             'duration': '8 Weeks', 'max_students': 25, 'is_active': True},
            
            {'title': 'Science Board Exam Preparation Coaching', 'workshop_type': 'coaching', 'target_audience': 'school',
             'description': '12-week comprehensive science coaching for Classes 9-10 board exam preparation. Includes practical sessions, doubt clearing, and mock tests.',
             'duration': '12 Weeks', 'max_students': 30, 'is_active': True},
            
            {'title': 'Robotics & Coding Bootcamp', 'workshop_type': 'robotics', 'target_audience': 'school',
             'description': 'Intensive 6-week bootcamp on robotics and coding. Students learn Arduino programming, robot building, and automation. Certificate provided.',
             'duration': '6 Weeks', 'max_students': 20, 'is_active': True},
            
            {'title': 'Physics Practical Training Program', 'workshop_type': 'science', 'target_audience': 'school',
             'description': 'Hands-on physics practical training for Classes 11-12. Focus on board exam practicals and lab skills development.',
             'duration': '4 Weeks', 'max_students': 25, 'is_active': True},
            
            {'title': 'Creative Thinking & Problem Solving Workshop', 'workshop_type': 'creative', 'target_audience': 'school',
             'description': 'Workshop focused on developing creative thinking, logical reasoning, and problem-solving skills through activities and challenges.',
             'duration': '2 Days', 'max_students': 35, 'is_active': True},
            
            {'title': 'Electronics & Circuit Building Workshop', 'workshop_type': 'electronics', 'target_audience': 'college',
             'description': 'Advanced electronics workshop covering circuit design, PCB making, and microcontroller programming.',
             'duration': '3 Days', 'max_students': 20, 'is_active': True},
        ]

        for w in workshops_data:
            Workshop.objects.get_or_create(title=w['title'], defaults=w)

        # Subjects for Home Tuition
        for subj in ['Mathematics', 'Science', 'English', 'Hindi', 'Physics', 'Chemistry', 'Biology',
                      'Computer Science', 'Social Studies', 'Sanskrit', 'French', 'All Subjects']:
            Subject.objects.get_or_create(name=subj)

        # Testimonials
        testimonials_data = [
            {'name': 'Rajesh Kumar', 'role': 'school', 'role_label': 'School Principal',
             'content': 'Builds Your Mind kits have transformed our science labs. Students are more engaged than ever!', 'rating': 5},
            {'name': 'Priya Sharma', 'role': 'parent', 'role_label': 'Parent',
             'content': 'My kids love the DIY kits. Great quality and eco-friendly - exactly what I was looking for.', 'rating': 5},
            {'name': 'Amit Patel', 'role': 'distributor', 'role_label': 'Distributor',
             'content': 'Excellent partnership program with great margins and support. Highly recommended!', 'rating': 5},
            {'name': 'Sunita Verma', 'role': 'parent', 'role_label': 'Parent',
             'content': 'The home tuition service matched us with an amazing teacher. My daughter is doing so much better now!', 'rating': 5},
            {'name': 'Dr. Meera Joshi', 'role': 'teacher', 'role_label': 'Home Tutor',
             'content': 'Teaching with Builds Your Mind gives me flexibility and a great platform to help students.', 'rating': 5},
            {'name': 'Anita Desai', 'role': 'school', 'role_label': 'Play School Owner',
             'content': 'The wooden toys are perfect for our play school. Eco-friendly, safe, and children love them!', 'rating': 5},
            {'name': 'Vikram Singh', 'role': 'school', 'role_label': 'School IT Head',
             'content': 'Smart classroom solutions from Builds Your Mind have modernized our teaching. Excellent quality!', 'rating': 5},
        ]

        for t in testimonials_data:
            Testimonial.objects.get_or_create(name=t['name'], defaults=t)

        self.stdout.write(self.style.SUCCESS('✅ Seed data created successfully with all PDF requirements!'))