from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Font ayarlari
        self.set_font('Arial', 'B', 16)
        # Isim
        self.cell(0, 10, 'ŞEHMUS KEREM TURĞAY', 0, 1, 'C')
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Android Engineer (Kotlin & Jetpack Compose)', 0, 1, 'C')
        
        # Iletisim Bilgileri
        self.set_font('Arial', '', 10)
        self.cell(0, 5, 'Turkey / Osmaniye | +90 507 804 0154 | kerem.turga.yy@gmail.com', 0, 1, 'C')
        self.cell(0, 5, 'LinkedIn | GitHub | Google Play Store Profile', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255) # Hafif mavi arka plan
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, body)
        self.ln()

    def job_entry(self, title, company, date, description, bullets):
        self.set_font('Arial', 'B', 11)
        self.cell(0, 6, f'{title}', 0, 1)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 6, f'{company} | {date}', 0, 1)
        
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, description)
        self.ln(2)
        
        for bullet in bullets:
            self.cell(5) # Girinti
            self.cell(2, 5, '-', 0, 0)
            self.multi_cell(0, 5, bullet)
        self.ln(5)

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# --- OZET ---
pdf.chapter_title('PROFESSIONAL SUMMARY')
summary = (
    "Innovative Android Engineer with a strong background in Kotlin and Jetpack Compose. "
    "Experienced in developing published applications with full-stack capabilities, including WebSocket integration for real-time communication "
    "and Location Services. Passionate about building scalable mobile architectures (MVVM/Clean Architecture) and crafting intuitive user experiences. "
    "Eager to contribute to BiTaksi's mission of transforming urban mobility with modern, reliable, and high-performance mobile solutions."
)
pdf.chapter_body(summary)

# --- TEKNIK BECERILER ---
pdf.chapter_title('TECHNICAL SKILLS')
skills = (
    "• Mobile Development: Kotlin (Advanced), Jetpack Compose, Coroutines, Flow, Dagger-Hilt, RoomDB\n"
    "• Architecture & Patterns: MVVM, Clean Architecture, OOP, RESTful APIs, WebSocket (Socket.io)\n"
    "• Tools & DevOps: Git/GitHub, Android Studio, Figma, Firebase (Analytics/Crashlytics), CI/CD Awareness\n"
    "• Backend Awareness: Node.js, Express.js, MySQL (Strong understanding of API & DB interactions)"
)
pdf.chapter_body(skills)

# --- IS DENEYIMI ---
pdf.chapter_title('PROFESSIONAL EXPERIENCE')

# Tubitak
pdf.job_entry(
    "Full Stack Developer",
    "Tubitak 1001 Project (Remote/Hybrid)",
    "October 2024 – Present",
    "Developed a real-time communication platform enabling seamless interaction between users, utilizing WebSocket technology critical for time-sensitive data flow.",
    [
        "Real-Time Architecture: Built a robust chat and data system using WebSockets and RESTful APIs, handling high-concurrency data streams.",
        "Modern UI/UX: Designed and implemented the Android UI entirely with Jetpack Compose, ensuring a responsive and fluid user experience.",
        "Dependency Injection: Utilized Dagger Hilt for dependency injection, creating a testable and modular codebase.",
        "Full-Stack Integration: Developed the backend with Express.js and optimized MySQL stored procedures to handle complex data queries efficiently."
    ]
)

# Aklımdaki Hediye
pdf.job_entry(
    "Android Developer",
    "Self Project - 'Aklımdaki Hediye' (Remote)",
    "March 2025 – May 2025",
    "Designed, developed, and published an AI-powered recommendation app on the Google Play Store.",
    [
        "Google Play Publishing: Successfully managed the full lifecycle of the app, from development to Play Store release and maintenance.",
        "AI Integration: Integrated AI APIs to provide personalized gift suggestions based on user input.",
        "Monetization: Implemented AdMob services to generate revenue streams.",
        "Tech Stack: Kotlin, Jetpack Compose, Retrofit."
    ]
)

# Earthquake Assistant
pdf.job_entry(
    "Android Developer",
    "Self Project - 'Earthquake Assistant' (Remote)",
    "June 2025 – Present",
    "Developing a safety-focused application relying on offline capabilities and location services.",
    [
        "Location Services: Implementing core location-based features to guide users during emergencies, highly relevant to urban mobility navigation.",
        "Offline First: Designing RoomDB architecture to ensure app functionality even without internet connectivity.",
        "Alert Systems: Creating critical alert mechanisms focusing on low-latency notifications."
    ]
)

# --- EGITIM ---
pdf.chapter_title('EDUCATION')
pdf.job_entry(
    "Management Information Systems (BSc)",
    "Osmaniye Korkut Ata University",
    "2022 – Present",
    "Focus: Mobile Technologies, Software Development, System Analysis and Design.",
    ["Relevant Coursework: Object-Oriented Programming, Database Management Systems."]
)

# --- DILLER ---
pdf.chapter_title('LANGUAGES')
pdf.chapter_body("Turkish (Native) | English (Professional Working Proficiency)")

# PDF'i kaydet
pdf.output('Sehmus_Kerem_Turgay_BiTaksi_CV.pdf')
print("PDF başarıyla oluşturuldu: Sehmus_Kerem_Turgay_BiTaksi_CV.pdf")