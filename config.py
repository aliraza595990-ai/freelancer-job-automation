# ============================================
# ALIRAZA FREELANCER JOB AUTOMATION SYSTEM
# Configuration File
# ============================================

# Personal Info
FREELANCER_NAME = "Aliraza"
FREELANCER_EMAIL = "aliraza595990@gmail.com"
FREELANCER_WHATSAPP = "+92 329 6883804"
FREELANCER_EXPERIENCE = "3 years"

# Skills
SKILLS = [
    "Logo Design",
    "Facebook Post Design",
    "Instagram Post Design",
    "YouTube Thumbnail Design",
    "Website Development",
    "Content Writing",
    "eBook Writing",
    "Facebook Account Management",
    "Instagram Account Management",
    "Social Media Management",
    "Graphic Design",
    "WordPress Development"
]

# Gmail SMTP Settings
GMAIL_USER = "aliraza595990@gmail.com"
GMAIL_APP_PASSWORD = "YOUR_GMAIL_APP_PASSWORD_HERE"  # Generate from Google Account Settings

# Job Search Keywords
JOB_KEYWORDS = [
    "graphic designer remote",
    "social media manager remote",
    "logo designer freelance",
    "content writer remote",
    "ebook writer freelance",
    "web developer remote",
    "youtube thumbnail designer",
    "instagram manager remote",
    "facebook ads manager"
]

# Job Sites to Search
JOB_SITES = {
    "remoteok": "https://remoteok.com/api",
    "remotive": "https://remotive.com/api/remote-jobs",
    "arbeitnow": "https://arbeitnow.com/api/job-board-api"
}

# Search Settings
MAX_JOBS_PER_SEARCH = 20
APPLY_DELAY_SECONDS = 30  # Wait between applications
DAILY_APPLICATION_LIMIT = 15

# Files
JOBS_CSV_FILE = "jobs_found.csv"
APPLIED_JOBS_FILE = "applied_jobs.csv"
LOG_FILE = "automation.log"
