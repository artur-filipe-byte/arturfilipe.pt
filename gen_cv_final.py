#!/usr/bin/env python3
"""
CV profissional - formato standard, limpo, ATS-friendly
Fontes: Calibri (títulos) e Calibri (corpo)
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Fontes
FD = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont('CB', os.path.join(FD, 'calibrib.ttf')))
pdfmetrics.registerFont(TTFont('CR', os.path.join(FD, 'calibri.ttf')))
pdfmetrics.registerFont(TTFont('CI', os.path.join(FD, 'calibrii.ttf')))

# Cores
AZUL = HexColor('#1a5276')
CINZA = HexColor('#5d6d7e')
CINZA_CLARO = HexColor('#aab7b8')
PRETO = HexColor('#2c3e50')
LINHA = HexColor('#d5dbdb')

M = 2.2 * cm  # margem
W, H = A4
CW = W - 2 * M  # largura util

def wrap(texto, tam, largura):
    """Quebra texto em linhas"""
    words = texto.split()
    linhas, cur = [], ''
    for w in words:
        teste = cur + ' ' + w if cur else w
        if c.stringWidth(teste, 'CR', tam) <= largura:
            cur = teste
        else:
            linhas.append(cur)
            cur = w
    if cur: linhas.append(cur)
    return linhas

# Iniciar PDF
c = canvas.Canvas(os.path.join(r'C:\Users\artur\arturfilipe.pt', 'cv-artur-filipe.pdf'), pagesize=A4)
c.setTitle('Artur Filipe - CV')

y = H - M

# ===== NOME =====
c.setFont('CB', 22)
c.setFillColor(PRETO)
c.drawCentredString(W/2, y, 'ARTUR FILIPE')
y -= 26

# ===== SUBTITULO =====
c.setFont('CR', 11)
c.setFillColor(AZUL)
c.drawCentredString(W/2, y, 'IT & Cybersecurity Professional')
y -= 18

# ===== CONTACTOS (pequeno, uma linha) =====
c.setFont('CR', 8)
c.setFillColor(CINZA)
contactos = '\u00c9vora, Portugal  |  artur.a.filipe@protonmail.com  |  +351 968 856 700'
c.drawCentredString(W/2, y, contactos)
y -= 12

c.setFont('CR', 8)
c.setFillColor(CINZA)
links = 'arturfilipe.work  |  linkedin.com/in/artur-filipe-it  |  github.com/artur-filipe-byte'
c.drawCentredString(W/2, y, links)
y -= 16

# ===== LINHA SEPARADORA =====
c.setStrokeColor(LINHA)
c.setLineWidth(1)
c.line(M, y, W-M, y)
y -= 16

# ===== SECCAO: PROFILE =====
c.setFont('CB', 10)
c.setFillColor(AZUL)
c.drawString(M, y, 'PROFESSIONAL PROFILE')
y -= 4
c.setStrokeColor(LINHA)
c.setLineWidth(0.5)
c.line(M, y, W-M, y)
y -= 12

c.setFont('CR', 9)
c.setFillColor(PRETO)
texto = ('Professional transitioning to IT and cybersecurity with CompTIA A+ and Security+ certifications. '
         'I build hands-on projects in my homelab (pfSense, Suricata, Elastic SIEM, Docker, Pi-hole) and document '
         'everything on GitHub. 13 years of customer-facing experience developing strong incident management, '
         'communication and problem-solving skills applied daily in IT projects.')
for linha in wrap(texto, 9, CW):
    c.drawString(M, y, linha)
    y -= 11
y -= 8

# ===== SECCAO: CERTIFICATIONS =====
c.setFont('CB', 10)
c.setFillColor(AZUL)
c.drawString(M, y, 'CERTIFICATIONS')
y -= 4
c.setStrokeColor(LINHA)
c.setLineWidth(0.5)
c.line(M, y, W-M, y)
y -= 12

certs = [
    ('CompTIA A+ (770)', 'CompTIA - Hardware, OS, networking and support', 'Feb 2026'),
    ('CompTIA Security+', 'CompTIA - Network security, risk management, crypto', 'Mar 2026'),
    ('Introduction to Cybersecurity', 'Claranet / Professional Training', 'Jun 2026'),
    ('Cyber Security 101', 'TryHackMe', 'Jan 2026'),
]
for titulo, subtitulo, data in certs:
    c.setFont('CB', 9)
    c.setFillColor(PRETO)
    c.drawString(M, y, titulo)
    # Data alinhada direita
    c.setFont('CR', 8)
    c.setFillColor(CINZA)
    larg_data = c.stringWidth(data, 'CR', 8)
    c.drawString(W - M - larg_data, y, data)
    y -= 11
    c.setFont('CI', 8)
    c.setFillColor(CINZA)
    c.drawString(M, y, subtitulo)
    y -= 12
y -= 4

# ===== SECCAO: EXPERIENCE =====
c.setFont('CB', 10)
c.setFillColor(AZUL)
c.drawString(M, y, 'PROFESSIONAL EXPERIENCE')
y -= 4
c.setStrokeColor(LINHA)
c.setLineWidth(0.5)
c.line(M, y, W-M, y)
y -= 12

exps = [
    ('Transition to IT', 'Study and Hands-on Projects', '2026 - Present', [
        'Homelab with pfSense, Suricata IDS/IPS, Elastic SIEM, Pi-hole, Docker and Cloudflare',
        'Python automation: backup scripts, Telegram bots, API integrations',
        'Rigorous documentation on GitHub (homelab-docs); portfolio at arturfilipe.work',
    ]),
    ('Casa do Vale Hotel - Front Desk', 'First Receptionist | \u00c9vora, Portugal', '2019 - 2026', [
        'Full guest cycle: check-in/out, invoicing, online reservations (Booking, Expedia)',
        'Shift coordination, staff training, GDPR compliance, access control, incident documentation',
        'Trilingual service: Portuguese and English (in-person and phone)',
    ]),
    ('Hotel Dom Fernando - Front Desk', 'Receptionist | \u00c9vora, Portugal', '2013 - 2019', [
        'Promoted to First Receptionist. Customer service, reservations, invoicing, incident resolution',
        'Intercultural communication and interdepartmental coordination in international environment',
    ]),
    ('Call Center Operator', 'Reditus - Travel Assistance | \u00c9vora, Portugal', '2013 - 2014', [
        'Phone support in Portuguese and English for travel insurance and emergency assistance',
    ]),
]

for titulo, subtitulo, periodo, bullets in exps:
    c.setFont('CB', 9)
    c.setFillColor(PRETO)
    c.drawString(M, y, titulo)
    c.setFont('CR', 8)
    c.setFillColor(CINZA)
    larg_per = c.stringWidth(periodo, 'CR', 8)
    c.drawString(W - M - larg_per, y, periodo)
    y -= 11
    if subtitulo:
        c.setFont('CI', 8)
        c.setFillColor(CINZA)
        c.drawString(M, y, subtitulo)
        y -= 11
    for b in bullets:
        c.setFont('CR', 8.5)
        c.setFillColor(PRETO)
        for linha in wrap('\u2022  ' + b, 8.5, CW - 8):
            c.drawString(M + 6, y, linha)
            y -= 10
    y -= 4

# ===== SECCAO: TECHNICAL SKILLS =====
c.setFont('CB', 10)
c.setFillColor(AZUL)
c.drawString(M, y, 'TECHNICAL SKILLS')
y -= 4
c.setStrokeColor(LINHA)
c.setLineWidth(0.5)
c.line(M, y, W-M, y)
y -= 12

skills_data = [
    ('Security:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intelligence'),
    ('Networking:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, firewall rules, Wireshark, Nmap'),
    ('Systems:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
    ('Tools:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare, Nextcloud, Pi-hole'),
]
for label, valor in skills_data:
    c.setFont('CB', 9)
    c.setFillColor(PRETO)
    larg_label = c.stringWidth(label, 'CB', 9)
    c.drawString(M, y, label)
    c.setFont('CR', 8.5)
    c.setFillColor(PRETO)
    c.drawString(M + larg_label + 5, y, valor)
    y -= 13
y -= 4

# ===== SECCAO: EDUCATION =====
c.setFont('CB', 10)
c.setFillColor(AZUL)
c.drawString(M, y, 'EDUCATION')
y -= 4
c.setStrokeColor(LINHA)
c.setLineWidth(0.5)
c.line(M, y, W-M, y)
y -= 12

educacao = [
    ('Cybersecurity Course', 'ISCTE - University Institute of Lisbon', 'Nov 2025 - Jul 2026'),
    ("Bachelor's in International Relations", 'University of \u00c9vora, Portugal', '2012 - 2015'),
    ('Professional Tourism Course', 'Severim de Faria High School, \u00c9vora', '2009 - 2011'),
]
for titulo, subtitulo, periodo in educacao:
    c.setFont('CB', 9)
    c.setFillColor(PRETO)
    c.drawString(M, y, titulo)
    c.setFont('CR', 8)
    c.setFillColor(CINZA)
    larg_per = c.stringWidth(periodo, 'CR', 8)
    c.drawString(W - M - larg_per, y, periodo)
    y -= 11
    c.setFont('CI', 8)
    c.setFillColor(CINZA)
    c.drawString(M, y, subtitulo)
    y -= 12

# ===== LANGUAGES (inline no fim) =====
y -= 4
c.setFont('CB', 10)
c.setFillColor(AZUL)
c.drawString(M, y, 'LANGUAGES')
y -= 4
c.setStrokeColor(LINHA)
c.setLineWidth(0.5)
c.line(M, y, W-M, y)
y -= 12

c.setFont('CR', 9)
c.setFillColor(PRETO)
c.drawString(M, y, 'Portuguese: Native  |  English: Advanced (C1)')

# ===== FOOTER =====
c.setFont('CR', 7)
c.setFillColor(CINZA_CLARO)
c.drawCentredString(W/2, 1.5*cm, 'CV updated June 2026  |  arturfilipe.work')

c.save()
cam = r'C:\Users\artur\arturfilipe.pt\cv-artur-filipe.pdf'
print(f'CV guardado: {cam}')
