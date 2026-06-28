#!/usr/bin/env python3
"""
Generate professional CV PDF for Artur Filipe
Uses Calibri font for proper Portuguese accent support
Clean, ATS-friendly, single-column layout
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Register Calibri font
FONT_DIR = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont('Calibri', os.path.join(FONT_DIR, 'calibri.ttf')))
pdfmetrics.registerFont(TTFont('Calibri-Bold', os.path.join(FONT_DIR, 'calibrib.ttf')))
pdfmetrics.registerFont(TTFont('Calibri-Italic', os.path.join(FONT_DIR, 'calibrii.ttf')))

# Colors
DARK = HexColor('#1a1a2e')
ACCENT = HexColor('#16213e')
BLUE = HexColor('#0f3460')
TEAL = HexColor('#38bdf8')
GRAY = HexColor('#64748b')
LIGHT_GRAY = HexColor('#cbd5e1')
NEAR_WHITE = HexColor('#f1f5f9')

def draw_cv(c, lang='pt'):
    width, height = A4
    margin = 2.0 * cm
    content_width = width - 2 * margin
    y = height - margin
    
    def section_header(text, y_pos):
        """Draw section header with underline"""
        c.setFont('Calibri-Bold', 12)
        c.setFillColor(DARK)
        c.drawString(margin, y_pos, text.upper())
        y_pos -= 4
        c.setStrokeColor(BLUE)
        c.setLineWidth(0.8)
        c.line(margin, y_pos, width - margin, y_pos)
        y_pos -= 12
        return y_pos
    
    def entry(title, subtitle, date, y_pos):
        """Draw an entry with title left, date right"""
        c.setFont('Calibri-Bold', 10)
        c.setFillColor(DARK)
        c.drawString(margin, y_pos, title)
        c.setFont('Calibri', 9)
        c.setFillColor(GRAY)
        # Date right-aligned
        date_width = c.stringWidth(date, 'Calibri', 9)
        c.drawString(width - margin - date_width, y_pos, date)
        y_pos -= 14
        if subtitle:
            c.setFont('Calibri-Italic', 9)
            c.setFillColor(GRAY)
            c.drawString(margin, y_pos, subtitle)
            y_pos -= 12
        return y_pos
    
    def bullet(text, y_pos):
        """Draw a bullet point"""
        c.setFont('Calibri', 9)
        c.setFillColor(HexColor('#334155'))
        bullet_text = f'\u2022  {text}'
        # Word wrap
        max_width = content_width - 10
        words = bullet_text.split()
        lines = []
        current_line = ''
        for word in words:
            test = current_line + ' ' + word if current_line else word
            if c.stringWidth(test, 'Calibri', 9) < max_width:
                current_line = test
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        
        for line in lines:
            c.drawString(margin + 5, y_pos, line)
            y_pos -= 11
        y_pos -= 2
        return y_pos
    
    def skill_row(label, value, y_pos):
        """Draw a skill label: value pair"""
        c.setFont('Calibri-Bold', 9)
        c.setFillColor(DARK)
        c.drawString(margin, y_pos, label)
        c.setFont('Calibri', 9)
        c.setFillColor(HexColor('#334155'))
        c.drawString(margin + 40, y_pos, value)
        return y_pos - 14
    
    # ===== HEADER =====
    # Name
    c.setFont('Calibri-Bold', 24)
    c.setFillColor(DARK)
    c.drawString(margin, y, 'ARTUR FILIPE')
    y -= 28
    
    # Subtitle
    subtitle_text = 'IT & Cybersecurity Professional' if lang == 'en' else 'Profissional IT & Cibersegurança'
    c.setFont('Calibri', 13)
    c.setFillColor(BLUE)
    c.drawString(margin, y, subtitle_text)
    y -= 22
    
    # Contact bar
    contact_bar_y = y
    c.setFillColor(NEAR_WHITE)
    c.setStrokeColor(HexColor('#e2e8f0'))
    c.setLineWidth(0.5)
    c.roundRect(margin - 3, y - 4, content_width + 6, 28, 3, fill=1, stroke=1)
    
    contact_info = [
        ('\U0001F4CD', 'Évora, Portugal'),
        ('\U00002709', 'artur.a.filipe@protonmail.com'),
        ('\U0001F310', 'arturfilipe.work'),
        ('\U0001F4F1', '+351 968 856 700'),
    ]
    
    c.setFont('Calibri', 8)
    c.setFillColor(GRAY)
    x_pos = margin + 8
    for icon, text in contact_info:
        c.drawString(x_pos, contact_bar_y + 6, f'{icon}  {text}')
        x_pos += c.stringWidth(f'  {text}', 'Calibri', 8) + 40
    
    y = contact_bar_y - 10
    
    # ===== PROFILE =====
    y = section_header('Perfil Profissional' if lang == 'pt' else 'Professional Profile', y - 8)
    
    profile_text = (
        'Profissional em transição para IT e cibersegurança com certificações CompTIA A+ e Security+. '
        'Construo projetos práticos no meu homelab (servidores, redes, firewall, SIEM) e documento tudo '
        'como prova de competência técnica. 13 anos de experiência em atendimento ao cliente '
        'desenvolveram capacidades fortes de gestão de incidentes, comunicação clara e resolução rápida '
        'de problemas, aplicadas diariamente nos projetos IT.'
    ) if lang == 'pt' else (
        'Professional transitioning to IT and cybersecurity with CompTIA A+ and Security+ certifications. '
        'I build hands-on projects in my homelab (servers, networks, firewalls, SIEM) and document everything '
        'as proof of technical competence. 13 years of customer-facing experience developed strong incident '
        'management, clear communication, and fast problem-solving skills applied daily in IT projects.'
    )
    
    c.setFont('Calibri', 9)
    c.setFillColor(HexColor('#334155'))
    
    # Word wrap profile text
    max_width = content_width
    words = profile_text.split()
    lines = []
    current_line = ''
    for word in words:
        test = current_line + ' ' + word if current_line else word
        if c.stringWidth(test, 'Calibri', 9) < max_width:
            current_line = test
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    for line in lines:
        c.drawString(margin, y, line)
        y -= 11
    y -= 8
    
    # ===== CERTIFICATIONS =====
    y = section_header('Certificações' if lang == 'pt' else 'Certifications', y - 4)
    
    certifications = [
        ('CompTIA A+ (770)', 'CompTIA - Hardware, SO, redes e suporte técnico', 'Fev 2026'),
        ('CompTIA Security+', 'CompTIA - Segurança de redes, gestão de risco e criptografia', 'Mar 2026'),
        ('Introdução à Cibersegurança', 'Claranet / Formação Profissional', 'Jun 2026'),
        ('Cyber Security 101', 'TryHackMe', 'Jan 2026'),
        ('Pre-Security Learning Path', 'TryHackMe', 'Jan 2026'),
    ] if lang == 'pt' else [
        ('CompTIA A+ (770)', 'CompTIA - Hardware, OS, networking and support', 'Feb 2026'),
        ('CompTIA Security+', 'CompTIA - Network security, risk management, crypto', 'Mar 2026'),
        ('Introduction to Cybersecurity', 'Claranet / Professional Training', 'Jun 2026'),
        ('Cyber Security 101', 'TryHackMe', 'Jan 2026'),
        ('Pre-Security Learning Path', 'TryHackMe', 'Jan 2026'),
    ]
    
    for title, sub, date in certifications:
        y = entry(title, sub, date, y)
    y -= 4
    
    # ===== EXPERIENCE =====
    y = section_header('Experiência Profissional' if lang == 'pt' else 'Professional Experience', y - 4)
    
    if lang == 'pt':
        experiences = [
            ('Transição para IT', 'Estudo e Projetos Práticos', '2026 - Presente', [
                'Homelab com pfSense, Suricata IDS/IPS, SIEM (Elastic Stack), Pi-hole e Docker',
                'Automação com Python: scripts de backup, bots Telegram, integrações API',
                'Documentação rigorosa de cada projeto no GitHub (homelab-docs)',
                'Portfolio pessoal: arturfilipe.work (Cloudflare + HTTPS)',
            ]),
            ('Casa do Vale Hotel - Receção', 'Rececionista de Primeira | Évora', '2019 - 2026', [
                'Gestão completa do ciclo de acolhimento: check-in, check-out, faturação e reservas online',
                'Coordenação de turnos, formação de novos colaboradores e conformidade com RGPD',
                'Garantia de conformidade com procedimentos internos e políticas de proteção de dados',
                'Atendimento presencial e telefónico em português e inglês',
            ]),
            ('Hotel Dom Fernando - Receção', 'Rececionista | Évora', '2013 - 2019', [
                'Promovido a Rececionista de 1.ª após 9 anos de serviço',
                'Atendimento ao cliente, gestão de reservas, faturação e resolução de incidentes',
                'Comunicação intercultural e coordenação interdepartamental',
                'Resolução de problemas sob pressão em ambiente internacional',
            ]),
            ('Operador de Call Center', 'Reditus - Assistência em Viagem | Évora', '2013 - 2014', [
                'Atendimento telefónico em português e inglês para seguros de viagem',
                'Apoio a clientes em situações de emergência e stress elevado',
            ]),
        ]
    else:
        experiences = [
            ('Transition to IT', 'Study and Hands-on Projects', '2026 - Present', [
                'Homelab with pfSense, Suricata IDS/IPS, Elastic SIEM, Pi-hole and Docker',
                'Python automation: backup scripts, Telegram bots, API integrations',
                'Rigorous documentation of all projects on GitHub (homelab-docs)',
                'Personal portfolio: arturfilipe.work (Cloudflare + HTTPS)',
            ]),
            ('Casa do Vale Hotel - Front Desk', 'First Receptionist | Évora', '2019 - 2026', [
                'Full guest cycle management: check-in, check-out, invoicing and online reservations',
                'Shift coordination, staff training and GDPR compliance',
                'Compliance with internal procedures, data handling policies and security protocols',
                'In-person and phone service in Portuguese and English',
            ]),
            ('Hotel Dom Fernando - Front Desk', 'Receptionist | Évora', '2013 - 2019', [
                'Promoted to First Receptionist after 9 years of service',
                'Customer service, reservations, invoicing and real-time incident resolution',
                'Intercultural communication and interdepartmental coordination',
                'Problem-solving under pressure in an international environment',
            ]),
            ('Call Center Operator', 'Reditus - Travel Assistance | Évora', '2013 - 2014', [
                'Phone support in Portuguese and English for travel insurance',
                'Assistance to clients in emergency and high-stress situations',
            ]),
        ]
    
    for title, sub, date, bullets in experiences:
        y = entry(title, sub, date, y)
        for b in bullets:
            y = bullet(b, y)
        y -= 4
    
    # ===== TECHNICAL SKILLS =====
    y = section_header('Competências Técnicas' if lang == 'pt' else 'Technical Skills', y - 4)
    
    skills = [
        ('Segurança:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intelligence'),
        ('Redes:', 'TCP/IP, DNS, DHCP, VLANs, firewall rules, pfSense, Wireshark, Nmap'),
        ('Sistemas:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
        ('Ferramentas:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare'),
        ('Serviços:', 'Nextcloud, Pi-hole, Jellyfin, Portainer, bind9'),
    ] if lang == 'pt' else [
        ('Security:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intelligence'),
        ('Networking:', 'TCP/IP, DNS, DHCP, VLANs, firewall rules, pfSense, Wireshark, Nmap'),
        ('Systems:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
        ('Tools:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare'),
        ('Services:', 'Nextcloud, Pi-hole, Jellyfin, Portainer, bind9'),
    ]
    
    for label, value in skills:
        y = skill_row(label, value, y)
    y -= 4
    
    # ===== LANGUAGES =====
    y = section_header('Idiomas' if lang == 'pt' else 'Languages', y - 4)
    
    if lang == 'pt':
        y = skill_row('Português:', 'Nativo', y)
        y = skill_row('Inglês:', 'Avançado (C1) - Leitura, escrita e conversação', y)
    else:
        y = skill_row('Portuguese:', 'Native', y)
        y = skill_row('English:', 'Advanced (C1) - Reading, writing and conversation', y)
    y -= 4
    
    # ===== EDUCATION =====
    y = section_header('Formação' if lang == 'pt' else 'Education', y - 4)
    
    education = [
        ('Curso de Cibersegurança', 'ISCTE - Instituto Universitário de Lisboa', 'Nov 2025 - Jul 2026'),
        ('Licenciatura em Relações Internacionais', 'Universidade de Évora', '2012 - 2015'),
        ('Curso Profissional de Turismo', 'Escola Secundária Severim de Faria, Évora', '2009 - 2011'),
    ] if lang == 'pt' else [
        ('Cybersecurity Course', 'ISCTE - University Institute of Lisbon', 'Nov 2025 - Jul 2026'),
        ("Bachelor's in International Relations", 'University of Évora', '2012 - 2015'),
        ('Professional Tourism Course', 'Severim de Faria High School, Évora', '2009 - 2011'),
    ]
    
    for title, sub, date in education:
        y = entry(title, sub, date, y)
    
    # ===== FOOTER =====
    c.setFont('Calibri', 7)
    c.setFillColor(GRAY)
    footer_text = f'CV atualizado em Junho 2026  |  arturfilipe.work  |  github.com/artur-filipe-byte'
    c.drawCentredString(width / 2, 1.5 * cm, footer_text)


def generate():
    output_dir = r'C:\Users\artur\arturfilipe.pt'
    
    # Portuguese CV
    c = canvas.Canvas(os.path.join(output_dir, 'cv-artur-filipe.pdf'), pagesize=A4)
    c.setTitle('Artur Filipe - CV')
    c.setAuthor('Artur Filipe')
    c.setSubject('Curriculum Vitae - IT & Cybersecurity')
    draw_cv(c, lang='pt')
    c.showPage()
    c.save()
    print(f'CV PT criado: {os.path.join(output_dir, "cv-artur-filipe.pdf")}')
    
    print('Done!')

if __name__ == '__main__':
    generate()
