# ============================================
# JOB FINDER MODULE
# Searches multiple job sites for remote jobs
# ============================================

import requests
import json
import csv
import os
import logging
from datetime import datetime
from config import *

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def search_remoteok_jobs(keyword):
    """Search RemoteOK API for jobs"""
    jobs = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(JOB_SITES['remoteok'], headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for job in data[1:]:  # Skip first item (legal notice)
                title = job.get('position', '').lower()
                if any(kw in title for kw in keyword.lower().split()):
                    jobs.append({
                        'title': job.get('position', ''),
                        'company': job.get('company', ''),
                        'location': 'Remote',
                        'salary': job.get('salary', 'Not specified'),
                        'apply_url': job.get('url', ''),
                        'email': job.get('apply_email', ''),
                        'description': job.get('description', '')[:500],
                        'source': 'RemoteOK',
                        'date_found': datetime.now().strftime('%Y-%m-%d')
                    })
        logging.info(f"RemoteOK: Found {len(jobs)} jobs for '{keyword}'")
    except Exception as e:
        logging.error(f"RemoteOK error: {e}")
    return jobs

def search_remotive_jobs(keyword):
    """Search Remotive API for jobs"""
    jobs = []
    try:
        params = {'search': keyword, 'limit': MAX_JOBS_PER_SEARCH}
        response = requests.get(JOB_SITES['remotive'], params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for job in data.get('jobs', []):
                jobs.append({
                    'title': job.get('title', ''),
                    'company': job.get('company_name', ''),
                    'location': 'Remote',
                    'salary': job.get('salary', 'Not specified'),
                    'apply_url': job.get('url', ''),
                    'email': '',
                    'description': job.get('description', '')[:500],
                    'source': 'Remotive',
                    'date_found': datetime.now().strftime('%Y-%m-%d')
                })
        logging.info(f"Remotive: Found {len(jobs)} jobs for '{keyword}'")
    except Exception as e:
        logging.error(f"Remotive error: {e}")
    return jobs

def search_arbeitnow_jobs(keyword):
    """Search Arbeitnow API for jobs"""
    jobs = []
    try:
        response = requests.get(JOB_SITES['arbeitnow'], timeout=10)
        if response.status_code == 200:
            data = response.json()
            for job in data.get('data', []):
                title = job.get('title', '').lower()
                if any(kw in title for kw in keyword.lower().split()):
                    jobs.append({
                        'title': job.get('title', ''),
                        'company': job.get('company_name', ''),
                        'location': 'Remote',
                        'salary': 'Not specified',
                        'apply_url': job.get('url', ''),
                        'email': '',
                        'description': job.get('description', '')[:500],
                        'source': 'Arbeitnow',
                        'date_found': datetime.now().strftime('%Y-%m-%d')
                    })
        logging.info(f"Arbeitnow: Found {len(jobs)} jobs for '{keyword}'")
    except Exception as e:
        logging.error(f"Arbeitnow error: {e}")
    return jobs

def find_all_jobs():
    """Search all job sites with all keywords"""
    all_jobs = []
    print("\n🔍 Searching for jobs...")
    
    for keyword in JOB_KEYWORDS:
        print(f"  Searching: {keyword}")
        all_jobs.extend(search_remoteok_jobs(keyword))
        all_jobs.extend(search_remotive_jobs(keyword))
        all_jobs.extend(search_arbeitnow_jobs(keyword))
    
    # Remove duplicates by URL
    seen_urls = set()
    unique_jobs = []
    for job in all_jobs:
        if job['apply_url'] not in seen_urls:
            seen_urls.add(job['apply_url'])
            unique_jobs.append(job)
    
    print(f"\n✅ Total unique jobs found: {len(unique_jobs)}")
    save_jobs_to_csv(unique_jobs)
    return unique_jobs

def save_jobs_to_csv(jobs):
    """Save found jobs to CSV file"""
    with open(JOBS_CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        if jobs:
            writer = csv.DictWriter(f, fieldnames=jobs[0].keys())
            writer.writeheader()
            writer.writerows(jobs)
    print(f"💾 Jobs saved to {JOBS_CSV_FILE}")

def get_jobs_with_email():
    """Return only jobs that have email addresses"""
    all_jobs = find_all_jobs()
    return [job for job in all_jobs if job.get('email')]

if __name__ == '__main__':
    jobs = find_all_jobs()
    print(f"Found {len(jobs)} jobs!")
