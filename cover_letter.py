# ============================================
# COVER LETTER GENERATOR
# Creates personalized cover letters
# ============================================

from config import *

def generate_cover_letter(job_title, company_name, job_description=""):
    """Generate a personalized professional cover letter"""
    
    # Detect job type for customization
    job_lower = job_title.lower()
    
    if any(kw in job_lower for kw in ['logo', 'graphic', 'design', 'thumbnail', 'youtube', 'instagram', 'facebook post']):
        skill_highlight = """My design expertise includes:
• Logo Design - Creating memorable brand identities
• Social Media Graphics - Eye-catching Facebook & Instagram posts
• YouTube Thumbnails - High CTR thumbnail designs
• Brand Identity - Complete visual branding packages"""
        tools = "Adobe Photoshop, Illustrator, Canva Pro, Figma"
        
    elif any(kw in job_lower for kw in ['web', 'wordpress', 'developer', 'website']):
        skill_highlight = """My web development expertise includes:
• WordPress Development - Custom themes and plugins
• Frontend Development - HTML, CSS, JavaScript
• Responsive Design - Mobile-first approach
• E-commerce - WooCommerce setup and customization"""
        tools = "WordPress, HTML5, CSS3, JavaScript, PHP, WooCommerce"
        
    elif any(kw in job_lower for kw in ['content', 'writer', 'writing', 'ebook', 'copywriter']):
        skill_highlight = """My writing expertise includes:
• Content Writing - SEO-optimized blog posts and articles
• eBook Writing - Professional long-form content
• Copywriting - Persuasive marketing copy
• Social Media Content - Engaging captions and posts"""
        tools = "Microsoft Word, Google Docs, Grammarly, SEO tools"
        
    elif any(kw in job_lower for kw in ['social media', 'manager', 'facebook', 'instagram', 'account']):
        skill_highlight = """My social media expertise includes:
• Account Management - Facebook & Instagram growth strategies
• Content Creation - Engaging posts and stories
• Community Management - Audience engagement and growth
• Analytics - Performance tracking and reporting"""
        tools = "Facebook Business Manager, Instagram Insights, Hootsuite, Buffer, Canva"
        
    else:
        skill_highlight = """My expertise includes:
• Graphic Design - Logo, social media, and brand design
• Web Development - WordPress and frontend development
• Content Writing - Articles, eBooks, and copywriting
• Social Media Management - Facebook & Instagram"""
        tools = "Adobe Photoshop, WordPress, Canva, Microsoft Office"
    
    cover_letter = f"""Subject: Application for {job_title} Position - Aliraza | 3 Years Experience

Dear Hiring Manager at {company_name},

I am writing to express my strong interest in the {job_title} position at {company_name}. With {FREELANCER_EXPERIENCE} of professional freelancing experience, I am confident I can deliver exceptional results for your team.

{skill_highlight}

Tools & Technologies I use:
{tools}

What sets me apart:
✅ 3+ years of proven experience
✅ 100% client satisfaction rate
✅ Fast turnaround times
✅ Clear communication throughout projects
✅ Unlimited revisions until you're satisfied

I am immediately available to start and can dedicate full-time hours to your project. I am passionate about delivering high-quality work that exceeds expectations.

I would love to discuss how my skills align with your needs. Please feel free to reach out:
📧 Email: {FREELANCER_EMAIL}
📱 WhatsApp: {FREELANCER_WHATSAPP}

Thank you for considering my application. I look forward to hearing from you!

Best regards,
Aliraza
Freelance Professional | {FREELANCER_EXPERIENCE} Experience
📧 {FREELANCER_EMAIL}
📱 {FREELANCER_WHATSAPP}"""
    
    return cover_letter

if __name__ == '__main__':
    # Test cover letter generation
    letter = generate_cover_letter("Logo Designer", "Creative Agency")
    print(letter)
