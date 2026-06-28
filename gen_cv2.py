#!/usr/bin/env python3
"""
Generate professional ATS-friendly CV
White background, dark text, one page, clean layout
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

FONT_DIR = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont('Cal', os.path.join(FONT_DIR, 'calibri.ttf')))
pdfmetrics.registerFont(TTFont('Cal-B', os.path.join(FONT_DIR, 'calibrib.ttf')))
pdfmetrics.registerFont(TTFont('Cal-I', os.path.join(FONT_DIR, 'calibrii.ttf')))

DARK = HexColor('#1e293b')
ACCENT = HexColor('#2563eb')
GRAY = HexColor('#64748b')
MID = HexColor('#475569')

M = 2.0 * cm  # margin
W, H = A4
CW = W - 2 * M  # content width

def wrap(c, text, font, size, max_w):
    words = text.split()
    lines = []
    cur = ''
    for w in words:
        test = cur + ' ' + w if cur else w
        if c.stringWidth(test, font, size) <= max_w:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_cv(c):
    y = H - M
    
    # ===== HEADER =====
    c.setFont('Cal-B', 22)
    c.setFillColor(DARK)
    c.drawString(M, y, 'ARTUR FILIPE')
    y -= 26
    
    c.setFont('Cal', 12)
    c.setFillColor(ACCENT)
    c.drawString(M, y, 'IT & Cybersecurity Professional')
    y -= 18
    
    # Contact line
    c.setFont('Cal', 8.5)
    c.setFillColor(GRAY)
    contacts = '\u2022  \u00c9vora, Portugal    \u2022  artur.a.filipe@protonmail.com    \u2022  +351 968 856 700    \u2022  arturfilipe.work'
    c.drawString(M, y, contacts)
    y -= 10
    c.drawString(M, y, '\u2022  github.com/artur-filipe-byte    \u2022  linkedin.com/in/artur-filipe-it')
    y -= 16
    
    # Separator
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(M, y, W - M, y)
    y -= 16
    
    # ===== PROFILE =====
    c.setFont('Cal-B', 10)
    c.setFillColor(DARK)
    c.drawString(M, y, 'PROFESSIONAL PROFILE')
    y -= 14
    
    c.setFont('Cal', 9)
    c.setFillColor(MID)
    text = ('Professional transitioning to IT and cybersecurity with CompTIA A+ and Security+ certifications. '
            'I build hands-on projects in my homelab (servers, networks, firewalls, SIEM) and document everything '
            'as proof of technical competence. 13 years of customer-facing experience developed strong incident '
            'management, clear communication, and fast problem-solving skills applied daily in IT projects.')
    for line in wrap(c, text, 'Cal', 9, CW):
        c.drawString(M, y, line)
        y -= 11
    y -= 10
    
    # ===== CERTIFICATIONS =====
    c.setStrokeColor(HexColor('#e2e8f0'))
    c.setLineWidth(0.5)
    c.line(M, y, W-M, y)
    y -= 12
    
    c.setFont('Cal-B', 10)
    c.setFillColor(DARK)
    c.drawString(M, y, 'CERTIFICATIONS')
    y -= 14
    
    certs = [
        ('CompTIA A+ (770)', 'CompTIA - Hardware, OS, networking and support foundation', 'Feb 2026'),
        ('CompTIA Security+', 'CompTIA - Network security, risk management and cryptography', 'Mar 2026'),
        ('Introduction to Cybersecurity', 'Claranet / Professional Training', 'Jun 2026'),
        ('Cyber Security 101', 'TryHackMe', 'Jan 2026'),
        ('Pre-Security Learning Path', 'TryHackMe', 'Jan 2026'),
    ]
    for title, sub, date in certs:
        c.setFont('Cal-B', 9)
        c.setFillColor(DARK)
        c.drawString(M, y, title)
        c.setFont('Cal', 8)
        c.setFillColor(GRAY)
        dw = c.stringWidth(date, 'Cal', 8)
        c.drawString(W - M - dw, y, date)
        y -= 11
        c.setFont('Cal-I', 8)
        c.setFillColor(GRAY)
        c.drawString(M, y, sub)
        y -= 13
    y -= 4
    
    # ===== EXPERIENCE =====
    c.setStrokeColor(HexColor('#e2e8f0'))
    c.setLineWidth(0.5)
    c.line(M, y, W-M, y)
    y -= 12
    
    c.setFont('Cal-B', 10)
    c.setFillColor(DARK)
    c.drawString(M, y, 'PROFESSIONAL EXPERIENCE')
    y -= 14
    
    exps = [
        ('Transition to IT', 'Study and Hands-on Projects', '2026 - Present', [
            'Homelab with pfSense, Suricata IDS/IPS, Elastic SIEM, Pi-hole and Docker',
            'Python automation: backup scripts, Telegram bots, API integrations',
            'Rigorous documentation of all projects on GitHub (homelab-docs)',
            'Personal portfolio: arturfilipe.work (Cloudflare + HTTPS)',
        ]),
        ('Casa do Vale Hotel - Front Desk', 'First Receptionist | \u00c9vora', '2019 - 2026', [
            'Full guest cycle management: check-in/out, invoicing and online reservations (Booking, Expedia)',
            'Shift coordination, staff training and compliance with data protection policies (GDPR)',
            'Managed access control, physical security procedures and incident documentation',
            'In-person and phone service in Portuguese and English',
        ]),
        ('Hotel Dom Fernando - Front Desk', 'Receptionist | \u00c9vora', '2013 - 2019', [
            'Promoted to First Receptionist after 9 years of service',
            'Customer service, reservations, invoicing and real-time incident resolution',
            'Developed intercultural communication and interdepartmental coordination skills',
        ]),
        ('Call Center Operator', 'Reditus - Travel Assistance | \u00c9vora', '2013 - 2014', [
            'Phone support in Portuguese and English for travel insurance',
            'Assistance to clients in emergency and high-stress situations',
        ]),
    ]
    
    for title, sub, date, bullets in exps:
        c.setFont('Cal-B', 9)
        c.setFillColor(DARK)
        c.drawString(M, y, title)
        c.setFont('Cal', 8)
        c.setFillColor(GRAY)
        dw = c.stringWidth(date, 'Cal', 8)
        c.drawString(W - M - dw, y, date)
        y -= 11
        if sub:
            c.setFont('Cal-I', 8)
            c.setFillColor(GRAY)
            c.drawString(M, y, sub)
            y -= 11
        for b in bullets:
            c.setFont('Cal', 8.5)
            c.setFillColor(MID)
            bw = CW - 10
            lines = wrap(c, '\u2022  ' + b, 'Cal', 8.5, bw)
            for line in lines:
                c.drawString(M + 5, y, line)
                y -= 10
        y -= 4
    
    # Check if we need more space - if y < 3cm, start page 2
    if y < 3 * cm:
        c.showPage()
        y = H - M
    
    # ===== SKILLS =====
    c.setStrokeColor(HexColor('#e2e8f0'))
    c.setLineWidth(0.5)
    c.line(M, y, W-M, y)
    y -= 12
    
    c.setFont('Cal-B', 10)
    c.setFillColor(DARK)
    c.drawString(M, y, 'TECHNICAL SKILLS')
    y -= 14
    
    skills = [
        ('Security:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intel'),
        ('Networking:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, Wireshark, Nmap'),
        ('Systems:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
        ('Tools:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare'),
        ('Services:', 'Nextcloud, Pi-hole, Jellyfin, Portainer'),
    ]
    for label, value in skills:
        c.setFont('Cal-B', 9)
        c.setFillColor(DARK)
        c.drawString(M, y, label)
        c.setFont('Cal', 8.5)
        c.setFillColor(MID)
        c.drawString(M + 42, y, value)
        y -= 13
    y -= 4
    
    # ===== LANGUAGES =====
    c.setStrokeColor(HexColor('#e2e8f0'))
    c.setLineWidth(0.5)
    c.line(M, y, W-M, y)
    y -= 12
    
    c.setFont('Cal-B', 10)
    c.setFillColor(DARK)
    c.drawString(M, y, 'LANGUAGES')
    y -= 14
    
    c.setFont('Cal-B', 9)
    c.setFillColor(DARK)
    c.drawString(M, y, 'Portuguese:')
    c.setFont('Cal', 8.5)
    c.setFillColor(MID)
    c.drawString(M + 42, y, 'Native')
    y -= 13
    c.setFont('Cal-B', 9)
    c.setFillColor(DARK)
    c.drawString(M, y, 'English:')
    c.setFont('Cal', 8.5)
    c.setFillColor(MID)
    c.drawString(M + 42, y, 'Advanced (C1) - Reading, writing and conversation')
    y -= 16
    
    # ===== EDUCATION =====
    c.setStrokeColor(HexColor('#e2e8f0'))
    c.setLineWidth(0.5)
    c.line(M, y, W-M, y)
    y -= 12
    
    c.setFont('Cal-B', 10)
    c.setFillColor(DARK)
    c.drawString(M, y, 'EDUCATION')
    y -= 14
    
    edu = [
        ('Cybersecurity Course', 'ISCTE - University Institute of Lisbon', 'Nov 2025 - Jul 2026'),
        ("Bachelor's in International Relations", 'University of \u00c9vora', '2012 - 2015'),
        ('Professional Tourism Course', 'Severim de Faria High School, \u00c9vora', '2009 - 2011'),
    ]
    for title, sub, date in edu:
        c.setFont('Cal-B', 9)
        c.setFillColor(DARK)
        c.drawString(M, y, title)
        c.setFont('Cal', 8)
        c.setFillColor(GRAY)
        dw = c.stringWidth(date, 'Cal', 8)
        c.drawString(W - M - dw, y, date)
        y -= 11
        c.setFont('Cal-I', 8)
        c.setFillColor(GRAY)
        c.drawString(M, y, sub)
        y -= 13
    
    # Footer
    c.setFont('Cal', 7)
    c.setFillColor(GRAY)
    c.drawCentredString(W/2, 1.5*cm, 'CV updated June 2026 | arturfilipe.work | github.com/artur-filipe-byte')

def generate():
    out = r'C:\Users\artur\arturfilipe.pt'
    c = canvas.Canvas(os.path.join(out, 'cv-artur-filipe.pdf'), pagesize=A4)
    c.setTitle('Artur Filipe - CV')
    draw_cv(c)
    c.save()
    print(f'CV saved: {os.path.join(out, "cv-artur-filipe.pdf")}')

if __name__ == '__main__':
    generate()
