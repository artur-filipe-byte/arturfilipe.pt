#!/usr/bin/env python3
"""
Professional one-page CV - ATS-friendly, Calibri font
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
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
BLUE = HexColor('#2563eb')
GRAY = HexColor('#64748b')
MID = HexColor('#475569')
LINE = HexColor('#e2e8f0')

M = 1.8 * cm
W, H = A4
CW = W - 2 * M

def wrap(c, text, f, sz, mw):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        t = cur + ' ' + w if cur else w
        if c.stringWidth(t, f, sz) <= mw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def sec_line(c, y):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(M, y, W-M, y)
    return y - 10

c = canvas.Canvas(os.path.join(r'C:\Users\artur\arturfilipe.pt', 'cv-artur-filipe.pdf'), pagesize=A4)
c.setTitle('Artur Filipe - CV')
y = H - M

# HEADER
c.setFont('Cal-B', 20)
c.setFillColor(DARK)
c.drawString(M, y, 'ARTUR FILIPE')
y -= 22

c.setFont('Cal', 11)
c.setFillColor(BLUE)
c.drawString(M, y, 'IT & Cybersecurity Professional')
y -= 16

c.setFont('Cal', 7.5)
c.setFillColor(GRAY)
c.drawString(M, y, 'artur.a.filipe@protonmail.com  |  +351 968 856 700  |  \u00c9vora, Portugal  |  arturfilipe.work  |  linkedin.com/in/artur-filipe-it')
y -= 14

# PROFILE
y = sec_line(c, y)
c.setFont('Cal-B', 9)
c.setFillColor(DARK)
c.drawString(M, y, 'Professional Profile')
y -= 11

c.setFont('Cal', 8)
c.setFillColor(MID)
for line in wrap(c, 'Professional transitioning to IT and cybersecurity with CompTIA A+ and Security+ certifications. I build hands-on projects in my homelab (pfSense, Suricata, Elastic SIEM, Docker, Pi-hole) and document everything on GitHub. 13 years of customer-facing experience developed strong incident management and communication skills applied daily in IT projects.', 'Cal', 8, CW):
    c.drawString(M, y, line)
    y -= 9
y -= 5

# CERTIFICATIONS
y = sec_line(c, y)
c.setFont('Cal-B', 9)
c.setFillColor(DARK)
c.drawString(M, y, 'Certifications')
y -= 11

for t, s, d in [
    ('CompTIA A+ (770)', 'CompTIA - Hardware, OS, networking and support', 'Feb 2026'),
    ('CompTIA Security+', 'CompTIA - Network security, risk management, crypto', 'Mar 2026'),
    ('Introduction to Cybersecurity', 'Claranet / Professional Training', 'Jun 2026'),
    ('Cyber Security 101', 'TryHackMe', 'Jan 2026'),
]:
    c.setFont('Cal-B', 8)
    c.setFillColor(DARK)
    c.drawString(M, y, t)
    c.setFont('Cal', 7)
    c.setFillColor(GRAY)
    c.drawString(W-M-c.stringWidth(d,'Cal',7), y, d)
    y -= 9
    c.setFont('Cal-I', 7.5)
    c.setFillColor(GRAY)
    c.drawString(M, y, s)
    y -= 11
y -= 3

# EXPERIENCE
y = sec_line(c, y)
c.setFont('Cal-B', 9)
c.setFillColor(DARK)
c.drawString(M, y, 'Professional Experience')
y -= 11

for t, s, d, bs in [
    ('Transition to IT', 'Study and Hands-on Projects', '2026 - Present',
     ['Homelab with pfSense, Suricata IDS/IPS, Elastic SIEM, Pi-hole, Docker',
      'Python automation: backup scripts, Telegram bots, API integrations',
      'Documentation of all projects on GitHub (homelab-docs); portfolio at arturfilipe.work']),
    ('Casa do Vale Hotel', 'First Receptionist | \u00c9vora', '2019 - 2026',
     ['Full guest cycle management: check-in/out, invoicing and online reservations (Booking, Expedia)',
      'Shift coordination, staff training, GDPR compliance, access control and incident documentation',
      'In-person and phone service in Portuguese and English']),
    ('Hotel Dom Fernando', 'Receptionist | \u00c9vora', '2013 - 2019',
     ['Promoted to First Receptionist after 9 years of service',
      'Customer service, reservations, invoicing and real-time incident resolution',
      'Intercultural communication and interdepartmental coordination']),
    ('Call Center Operator', 'Reditus - Travel Assistance | \u00c9vora', '2013 - 2014',
     ['Phone support in Portuguese and English for travel insurance']),
]:
    c.setFont('Cal-B', 8.5)
    c.setFillColor(DARK)
    c.drawString(M, y, t)
    c.setFont('Cal', 7)
    c.setFillColor(GRAY)
    c.drawString(W-M-c.stringWidth(d,'Cal',7), y, d)
    y -= 9
    if s:
        c.setFont('Cal-I', 7.5)
        c.setFillColor(GRAY)
        c.drawString(M, y, s)
        y -= 9
    for b in bs:
        c.setFont('Cal', 7.5)
        c.setFillColor(MID)
        for line in wrap(c, '\u2022  ' + b, 'Cal', 7.5, CW-8):
            c.drawString(M+6, y, line)
            y -= 9
    y -= 3

# SKILLS
y = sec_line(c, y)
c.setFont('Cal-B', 9)
c.setFillColor(DARK)
c.drawString(M, y, 'Technical Skills')
y -= 11

for l, v in [
    ('Security:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intel'),
    ('Networking:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, Wireshark, Nmap'),
    ('Systems:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
    ('Tools:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare'),
]:
    c.setFont('Cal-B', 8)
    c.setFillColor(DARK)
    c.drawString(M, y, l)
    c.setFont('Cal', 7.5)
    c.setFillColor(MID)
    c.drawString(M+38, y, v)
    y -= 11

# LANGUAGES + EDUCATION side by side to save space
y -= 2
c.setFont('Cal-B', 9)
c.setFillColor(DARK)
c.drawString(M, y, 'Languages')
y -= 11
c.setFont('Cal-B', 8)
c.setFillColor(DARK)
c.drawString(M, y, 'Portuguese:')
c.setFont('Cal', 7.5)
c.setFillColor(MID)
c.drawString(M+42, y, 'Native')
y -= 10
c.setFont('Cal-B', 8)
c.setFillColor(DARK)
c.drawString(M, y, 'English:')
c.setFont('Cal', 7.5)
c.setFillColor(MID)
c.drawString(M+42, y, 'Advanced (C1)')
y -= 14

# EDUCATION
c.setFont('Cal-B', 9)
c.setFillColor(DARK)
c.drawString(M, y, 'Education')
y -= 11

for t, s, d in [
    ('Cybersecurity Course', 'ISCTE - University Institute of Lisbon', 'Nov 2025 - Jul 2026'),
    ("Bachelor's in International Relations", 'University of \u00c9vora', '2012 - 2015'),
]:
    c.setFont('Cal-B', 8)
    c.setFillColor(DARK)
    c.drawString(M, y, t)
    c.setFont('Cal', 7)
    c.setFillColor(GRAY)
    c.drawString(W-M-c.stringWidth(d,'Cal',7), y, d)
    y -= 9
    c.setFont('Cal-I', 7.5)
    c.setFillColor(GRAY)
    c.drawString(M, y, s)
    y -= 11

# FOOTER
c.setFont('Cal', 6.5)
c.setFillColor(GRAY)
c.drawCentredString(W/2, 1.3*cm, 'CV updated June 2026 | arturfilipe.work | github.com/artur-filipe-byte')

c.save()
out_path = r'C:\Users\artur\arturfilipe.pt\cv-artur-filipe.pdf'
print(f'CV saved to: {out_path}')
