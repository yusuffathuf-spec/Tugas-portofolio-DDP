from django.shortcuts import render

def home(request):
    context = {
        'page_title': 'Home',
        'name': 'Muhamad Yusuf Fathurrohman',
        'profession': 'Mahasiswa Teknik Informatika',
        'description': 'Saya adalah mahasiswa STT Terpadu Nurul Fikri yang berfokus pada pengembangan web menggunakan teknologi modern.',
        'skills': ['Python', 'Django', 'JavaScript', 'Bootstrap', 'HTML/CSS'],
        'email': 'Yusuffathuf@gmail.com',
        'phone': '+62 857-4872-3858',
        'location': 'Depok, Indonesia'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'page_title': 'About Me',
        'education': [
            {
                'degree': 'S1 Teknik Informatika',
                'institution': 'STT Terpadu Nurul Fikri',
                'year': '2025 - Sekarang',
                'description': 'Fokus pada pengembangan aplikasi web dan sistem informasi.'
            },
            {
                'degree': 'MA IPA',
                'institution': 'MA Arrahmaniyah Depok',
                'year': '2022 - 2025',
                'description': 'Mempelajari dasar sains, logika, dan aktif dalam pengembangan diri melalui organisasi.'
            }
        ],
        'organizations': [
            {
                'name': 'Dewan Ambalan MA Arrahmaniyah',
                'position': 'Humas',
                'period': '2023 - 2025',
                'description': 'Menjadi jembatan komunikasi, mengelola publikasi media sosial, dokumentasi kegiatan, serta membina citra positif Ambalan.'
            },
            {
                'name': 'OSIS MA Arrahmaniyah',
                'position': 'Sekbid Olahraga dan Kesenian',
                'period': '2023 - 2025',
                'description': 'Mengelola kegiatan minat bakat, pembinaan jasmani, serta pengembangan kreativitas seni anggota melalui aktivitas sportif.'
            }
        ]
    }
    return render(request, 'about.html', context)

def gallery(request):
    context = {
        'page_title': 'Gallery',
        'images': [
            {
                'title': 'Travelling',
                'description': 'Berbagi Moment saat Travelling',
                'image': 'images/fatur.jpeg' 
            },
            {
                'title': 'Foto BTS',
                'description': 'Foto buku tahunan sekolah',
                'image': 'images/fatur1.jpeg'
            },
            {
                'title': 'Pelantikan Laksan',
                'description': 'Melaksanakan pelantikan Pramuka tingkat Laksana',
                'image': 'images/fatur2.jpeg'
            }
        ]
    }
    return render(request, 'gallery.html', context)