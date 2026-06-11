# ============================================
# EMAIL SENDER MODULE
# Sends job applications via Gmail SMTP
# ============================================

import smtplib
import csv
import time
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config import *
from cover_letter import generate_cover_letter

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_application_email(to_email, job_title, company_name, job_description=""):
    """Send a job application email"""
    try:
        # Generate cover letter
        cover_letter = generate_cover_letter(job_title, company_name, job_description)
        
        # Create email
        msg = MIMEMultipart('alternative')
        msg['From'] = GMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = f"Application for {job_title} - Aliraza | 3 Years Experience"
        
        # Plain text version
        msg.attach(MIMEText(cover_letter, 'plain'))
        
        # HTML version
        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <div style="background: #1a73e8; color: white; padding: 20px; border-radius: 8px 8px 0 0;">
                <h2>Job Application - {job_title}</h2>
                <p>From: Aliraza | Freelance Professional</p>
            </div>
            <div style="padding: 20px; background: #f9f9f9;">
                <pre style="white-space: pre-wrap; font-family: Arial; font-size: 14px;">{cover_letter}</pre>
            </div>
            <div style="background: #1a73e8; color: white; padding: 10px 20px; border-radius: 0 0 8px 8px; text-align: center;">
                <p>📧 {FREELANCER_EMAIL} | 📱 {FREELANCER_WHATSAPP}</p>
            </div>
        </body>
        </html>
        """
        msg.attach(MIMEText(html_body, 'html'))
        
        # Send via Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        
        logging.info(f"✅ Email sent to {to_email} for {job_title} at {company_name}")
        print(f"✅ Applied to: {job_title} at {company_name} ({to_email})")
        
        # Save to applied jobs
        save_applied_job(job_title, company_name, to_email)
        return True
        
    except Exception as e:
        logging.error(f"❌ Failed to send to {to_email}: {e}")
        print(f"❌ Failed: {job_title} at {company_name} - {e}")
        return False

def save_applied_job(job_title, company, email):
    """Save applied job to CSV"""
    with open(APPLIED_JOBS_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M'), job_title, company, email, 'Applied'])

def send_bulk_applications(jobs):
    """Send applications to multiple jobs with email"""
    sent = 0
    failed = 0
    
    print(f"\n📧 Sending {len(jobs)} job applications...")
    print("=" * 50)
    
    for i, job in enumerate(jobs[:DAILY_APPLICATION_LIMIT]):
        if job.get('email'):
            success = send_application_email(
                to_email=job['email'],
                job_title=job['title'],
                company_name=job['company'],
                job_description=job.get('description', '')
            )
            if success:
                sent += 1
            else:
                failed += 1
            
            # Wait between emails to avoid spam detection
            if i < len(jobs) - 1:
                print(f"   ⏳ Waiting {APPLY_DELAY_SECONDS} seconds...")
                time.sleep(APPLY_DELAY_SECONDS)
    
    print("\n" + "=" * 50)
    print(f"📊 Results: ✅ Sent: {sent} | ❌ Failed: {failed}")
    return sent, failed

if __name__ == '__main__':
    # Test single email
    send_application_email(
        to_email="test@example.com",
        job_title="Graphic Designer",
        company_name="Test Company"
    )
