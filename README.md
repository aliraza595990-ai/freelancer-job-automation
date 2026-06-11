# 🤖 Aliraza Freelancer Job Automation System

> Automatically finds remote jobs and sends professional applications via email!

## 👤 About
- **Name:** Aliraza
- **Email:** aliraza595990@gmail.com  
- **WhatsApp:** +92 329 6883804
- **Skills:** Logo Design | Social Media Design | YouTube Thumbnails | Web Development | Content Writing | eBook Writing | Social Media Management

---

## 🚀 How to Run

### Step 1: Install Python
Download Python from https://python.org (version 3.8+)

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup Gmail App Password
1. Go to your Gmail account
2. Settings → Security → 2-Step Verification (enable it)
3. Settings → Security → App Passwords
4. Create new app password
5. Copy the 16-character password
6. Open `config.py` and replace `YOUR_GMAIL_APP_PASSWORD_HERE` with your password

### Step 4: Run the System
```bash
python main.py
```

---

## 📋 Features

| Feature | Description |
|---------|-------------|
| 🔍 Job Search | Searches RemoteOK, Remotive, Arbeitnow APIs |
| 📝 Cover Letters | Auto-generates personalized cover letters |
| 📧 Auto Apply | Sends emails to companies automatically |
| 📊 CSV Export | Saves all jobs and applications to CSV |
| ⏰ Scheduler | Runs automatically every day at 9 AM |
| 📋 Logging | Keeps detailed logs of all activities |

---

## 📁 File Structure

```
freelancer-job-automation/
│
├── main.py           # 🎯 Main controller - RUN THIS!
├── job_finder.py     # 🔍 Job search module
├── cover_letter.py   # 📝 Cover letter generator  
├── email_sender.py   # 📧 Email sending module
├── config.py         # ⚙️ Configuration settings
├── requirements.txt  # 📦 Python dependencies
├── README.md         # 📖 This file
│
├── jobs_found.csv    # (auto-created) All found jobs
├── applied_jobs.csv  # (auto-created) Applied jobs log
└── automation.log    # (auto-created) System logs
```

---

## ⚙️ Customization

Edit `config.py` to change:
- Job search keywords
- Daily application limit
- Delay between applications
- Your personal information

---

## 💡 Tips

1. **Run daily** for best results
2. **Check jobs_found.csv** to manually apply to jobs without email
3. **Check applied_jobs.csv** to track your applications
4. Set Gmail App Password correctly for emails to work

---

## 📞 Support

- 📧 Email: aliraza595990@gmail.com
- 📱 WhatsApp: +92 329 6883804

---

*Built with ❤️ for Aliraza's freelancing success!*
