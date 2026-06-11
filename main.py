# ============================================
# ALIRAZA FREELANCER JOB AUTOMATION SYSTEM
# Main Controller - Run this file to start!
# ============================================
# Author: Aliraza | aliraza595990@gmail.com
# Version: 1.0
# ============================================

import os
import csv
import time
import logging
import schedule
from datetime import datetime
from job_finder import find_all_jobs, get_jobs_with_email
from email_sender import send_bulk_applications
from cover_letter import generate_cover_letter
from config import *

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def print_banner():
    print("""
╔══════════════════════════════════════════════════════╗
║     🤖 ALIRAZA FREELANCER JOB AUTOMATION SYSTEM     ║
║         Automatic Job Finder & Auto Apply            ║
╠══════════════════════════════════════════════════════╣
║  👤 Name:     Aliraza                               ║
║  📧 Email:    aliraza595990@gmail.com               ║
║  📱 WhatsApp: +92 329 6883804                       ║
║  ⚡ Skills:   Design | Web Dev | Writing            ║
╚══════════════════════════════════════════════════════╝
    """)

def initialize_csv_files():
    """Create CSV files with headers if they don't exist"""
    if not os.path.exists(APPLIED_JOBS_FILE):
        with open(APPLIED_JOBS_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Job Title', 'Company', 'Email', 'Status'])
        print(f"✅ Created {APPLIED_JOBS_FILE}")

def run_daily_job_search():
    """Main daily automation task"""
    print(f"\n🚀 Starting daily job search - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    logging.info("Daily job search started")
    
    # Step 1: Find all jobs
    print("\n📋 STEP 1: Finding Jobs...")
    all_jobs = find_all_jobs()
    
    # Step 2: Filter jobs with email
    jobs_with_email = [job for job in all_jobs if job.get('email')]
    print(f"\n📧 Jobs with direct email: {len(jobs_with_email)}")
    
    # Step 3: Send applications
    if jobs_with_email:
        print("\n📤 STEP 2: Sending Applications...")
        sent, failed = send_bulk_applications(jobs_with_email)
        logging.info(f"Daily run complete: {sent} sent, {failed} failed")
    else:
        print("\n⚠️ No jobs with email found today. Check jobs_found.csv for manual apply.")
    
    print(f"\n✅ Daily run complete! Check {APPLIED_JOBS_FILE} for results.")
    print(f"📋 All found jobs saved to: {JOBS_CSV_FILE}")

def show_stats():
    """Show application statistics"""
    if os.path.exists(APPLIED_JOBS_FILE):
        with open(APPLIED_JOBS_FILE, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            total = len(rows) - 1  # Minus header
        print(f"\n📊 Total applications sent: {total}")
    else:
        print("\n📊 No applications sent yet.")

def main():
    print_banner()
    initialize_csv_files()
    
    print("\n🎯 What would you like to do?")
    print("1. Run job search NOW")
    print("2. Schedule daily automatic search (9 AM)")
    print("3. View application stats")
    print("4. Generate sample cover letter")
    print("5. Exit")
    
    choice = input("\nEnter choice (1-5): ").strip()
    
    if choice == '1':
        run_daily_job_search()
    
    elif choice == '2':
        print("\n⏰ Scheduling daily job search at 9:00 AM...")
        schedule.every().day.at("09:00").do(run_daily_job_search)
        print("✅ Scheduler started! Press Ctrl+C to stop.")
        while True:
            schedule.run_pending()
            time.sleep(60)
    
    elif choice == '3':
        show_stats()
    
    elif choice == '4':
        job = input("Job title: ")
        company = input("Company name: ")
        letter = generate_cover_letter(job, company)
        print("\n" + "="*50)
        print(letter)
    
    elif choice == '5':
        print("\n👋 Goodbye! Good luck with your job search!")
    
    else:
        print("Invalid choice. Running job search now...")
        run_daily_job_search()

if __name__ == '__main__':
    main()
