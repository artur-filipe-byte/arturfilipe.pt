#!/usr/bin/env python3
"""Generate CV in EN and PT versions - professional ATS-friendly format"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

FD = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont('CB', os.path.join(FD, 'calibrib.ttf')))
pdfmetrics.registerFont(TTFont('CR', os.path.join(FD, 'calibri.ttf')))
pdfmetrics.registerFont(TTFont('CI', os.path.join(FD, 'calibrii.ttf')))

AZUL = HexColor('#1a5276')
CINZA = HexColor('#5d6d7e')
CINZA_CLARO = HexColor('#aab7b8')
PRETO = HexColor('#2c3e50')
LINHA = HexColor('#d5dbdb')

M = 2.2 * cm
W, H = A4
CW = W - 2 * M

def wrap(c, texto, tam, largura):
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

def draw_header(c, y, subtitle):
    c.setFont('CB', 22)
    c.setFillColor(PRETO)
    c.drawCentredString(W/2, y, 'ARTUR FILIPE')
    y -= 26
    c.setFont('CR', 11)
    c.setFillColor(AZUL)
    c.drawCentredString(W/2, y, subtitle)
    y -= 18
    c.setFont('CR', 8)
    c.setFillColor(CINZA)
    c.drawCentredString(W/2, y, 'Evora, Portugal  |  artur.a.filipe@protonmail.com  |  +351 968 856 700')
    y -= 12
    c.setFont('CR', 8)
    c.setFillColor(CINZA)
    c.drawCentredString(W/2, y, 'arturfilipe.work  |  linkedin.com/in/artur-filipe-it  |  github.com/artur-filipe-byte')
    y -= 16
    c.setStrokeColor(LINHA)
    c.setLineWidth(1)
    c.line(M, y, W-M, y)
    y -= 16
    return y

def draw_section(c, y, title):
    c.setFont('CB', 10)
    c.setFillColor(AZUL)
    c.drawString(M, y, title)
    y -= 4
    c.setStrokeColor(LINHA)
    c.setLineWidth(0.5)
    c.line(M, y, W-M, y)
    y -= 12
    return y

def draw_entry(c, y, titulo, subtitulo, data):
    c.setFont('CB', 9)
    c.setFillColor(PRETO)
    c.drawString(M, y, titulo)
    c.setFont('CR', 8)
    c.setFillColor(CINZA)
    larg = c.stringWidth(data, 'CR', 8)
    c.drawString(W-M-larg, y, data)
    y -= 11
    if subtitulo:
        c.setFont('CI', 8)
        c.setFillColor(CINZA)
        c.drawString(M, y, subtitulo)
        y -= 12
    return y

def draw_bullets(c, y, bullets):
    for b in bullets:
        c.setFont('CR', 8.5)
        c.setFillColor(PRETO)
        for linha in wrap(c, '  '+b, 8.5, CW-8):
            c.drawString(M+6, y, linha)
            y -= 10
    return y

def draw_skills(c, y, data):
    for label, valor in data:
        c.setFont('CB', 9)
        c.setFillColor(PRETO)
        larg = c.stringWidth(label, 'CB', 9)
        c.drawString(M, y, label)
        c.setFont('CR', 8.5)
        c.setFillColor(PRETO)
        c.drawString(M+larg+5, y, valor)
        y -= 13
    return y

def make_cv(filename, lang):
    c = canvas.Canvas(os.path.join(out_dir, filename), pagesize=A4)
    c.setTitle('Artur Filipe - CV')
    y = H - M

    if lang == 'en':
        y = draw_header(c, y, 'IT & Cybersecurity Professional')
        y = draw_section(c, y, 'PROFESSIONAL PROFILE')
        c.setFont('CR', 9)
        c.setFillColor(PRETO)
        for linha in wrap(c, 'Professional transitioning to IT and cybersecurity with CompTIA A+ and Security+ certifications. I build hands-on projects in my homelab (pfSense, Suricata, Elastic SIEM, Docker, Pi-hole) and document everything on GitHub. 13 years of customer-facing experience developing strong incident management, communication and problem-solving skills applied daily in IT projects.', 9, CW):
            c.drawString(M, y, linha); y -= 11
        y -= 8

        y = draw_section(c, y, 'CERTIFICATIONS')
        for t, s, d in [('CompTIA A+ (770)', 'CompTIA - Hardware, OS, networking and support', 'Feb 2026'),
                         ('CompTIA Security+', 'CompTIA - Network security, risk management, crypto', 'Mar 2026'),
                         ('Introduction to Cybersecurity', 'Claranet / Professional Training', 'Jun 2026'),
                         ('Cyber Security 101', 'TryHackMe', 'Jan 2026')]:
            y = draw_entry(c, y, t, s, d)
        y -= 4

        y = draw_section(c, y, 'PROFESSIONAL EXPERIENCE')
        for t, s, p, bs in [
            ('Transition to IT', 'Study and Hands-on Projects', '2026 - Present',
             ['Homelab with pfSense, Suricata IDS/IPS, Elastic SIEM, Pi-hole, Docker and Cloudflare',
              'Python automation: backup scripts, Telegram bots, API integrations',
              'Rigorous documentation on GitHub; portfolio at arturfilipe.work']),
            ('Casa do Vale Hotel - Front Desk', 'First Receptionist | Evora, Portugal', '2019 - 2026',
             ['Full guest cycle: check-in/out, invoicing, online reservations (Booking, Expedia)',
              'Shift coordination, staff training, GDPR compliance, access control, incident documentation',
              'Service in Portuguese and English (in-person and phone)']),
            ('Hotel Dom Fernando - Front Desk', 'Receptionist | Evora, Portugal', '2013 - 2019',
             ['Promoted to First Receptionist. Customer service, reservations, invoicing, incidents',
              'Intercultural communication and interdepartmental coordination']),
            ('Call Center Operator', 'Reditus - Travel Assistance | Evora, Portugal', '2013 - 2014',
             ['Phone support in Portuguese and English for travel insurance and emergencies']),
        ]:
            y = draw_entry(c, y, t, s, p)
            y = draw_bullets(c, y, bs)
            y -= 4

        y = draw_section(c, y, 'TECHNICAL SKILLS')
        y = draw_skills(c, y, [
            ('Security:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intel'),
            ('Networking:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, firewall rules, Wireshark, Nmap'),
            ('Systems:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
            ('Tools:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare, Nextcloud, Pi-hole'),
        ])
        y -= 4

        y = draw_section(c, y, 'EDUCATION')
        for t, s, d in [
            ('Cybersecurity Course', 'ISCTE - University Institute of Lisbon', 'Nov 2025 - Jul 2026'),
            ("Bachelor's in International Relations", 'University of Evora', '2012 - 2015'),
            ('Professional Tourism Course', 'Severim de Faria High School, Evora', '2009 - 2011'),
        ]:
            y = draw_entry(c, y, t, s, d)

        y = draw_section(c, y, 'LANGUAGES') if y > 8*cm else y
        c.setFont('CR', 9)
        c.setFillColor(PRETO)
        c.drawString(M, y, 'Portuguese: Native  |  English: Advanced (C1)')

        c.setFont('CR', 7)
        c.setFillColor(CINZA_CLARO)
        c.drawCentredString(W/2, 1.5*cm, 'CV updated June 2026  |  arturfilipe.work')

    else:  # PT
        y = draw_header(c, y, 'Profissional IT & Ciberseguranca')
        y = draw_section(c, y, 'PERFIL PROFISSIONAL')
        c.setFont('CR', 9)
        c.setFillColor(PRETO)
        for linha in wrap(c, 'Profissional em transicao para IT e ciberseguranca com certificacoes CompTIA A+ e Security+. Construo projetos praticos no meu homelab (pfSense, Suricata, Elastic SIEM, Docker, Pi-hole) e documento tudo no GitHub. 13 anos de experiencia em atendimento ao cliente desenvolveram capacidades fortes de gestao de incidentes, comunicacao e resolucao de problemas aplicadas diariamente em projetos IT.', 9, CW):
            c.drawString(M, y, linha); y -= 11
        y -= 8

        y = draw_section(c, y, 'CERTIFICACOES')
        for t, s, d in [('CompTIA A+ (770)', 'CompTIA - Hardware, SO, redes e suporte tecnico', 'Fev 2026'),
                         ('CompTIA Security+', 'CompTIA - Seguranca de redes, gestao de risco, criptografia', 'Mar 2026'),
                         ('Introducao a Ciberseguranca', 'Claranet / Formacao Profissional', 'Jun 2026'),
                         ('Cyber Security 101', 'TryHackMe', 'Jan 2026')]:
            y = draw_entry(c, y, t, s, d)
        y -= 4

        y = draw_section(c, y, 'EXPERIENCIA PROFISSIONAL')
        for t, s, p, bs in [
            ('Transicao para IT', 'Estudo e Projetos Praticos', '2026 - Presente',
             ['Homelab com pfSense, Suricata IDS/IPS, SIEM Elastic, Pi-hole, Docker e Cloudflare',
              'Automacao Python: scripts backup, bots Telegram, integracoes API',
              'Documentacao rigorosa no GitHub; portfolio em arturfilipe.work']),
            ('Casa do Vale Hotel - Rececao', 'Rececionista de 1a | Evora, Portugal', '2019 - 2026',
             ['Ciclo completo do hospede: check-in/out, faturacao, reservas online (Booking, Expedia)',
              'Coordenacao turnos, formacao, conformidade RGPD, controlo acesso, documentacao incidentes',
              'Atendimento em portugues e ingles (presencial e telefonico)']),
            ('Hotel Dom Fernando - Rececao', 'Rececionista | Evora, Portugal', '2013 - 2019',
             ['Promovido a Rececionista de 1a. Atendimento cliente, reservas, faturacao, incidencias',
              'Comunicacao intercultural e coordenacao interdepartamental']),
            ('Operador Call Center', 'Reditus - Assistencia Viagem | Evora, Portugal', '2013 - 2014',
             ['Apoio telefonico PT/EN para seguros de viagem e emergencias']),
        ]:
            y = draw_entry(c, y, t, s, p)
            y = draw_bullets(c, y, bs)
            y -= 4

        y = draw_section(c, y, 'COMPETENCIAS TECNICAS')
        y = draw_skills(c, y, [
            ('Seguranca:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intel'),
            ('Redes:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, firewall rules, Wireshark, Nmap'),
            ('Sistemas:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
            ('Ferramentas:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare, Nextcloud, Pi-hole'),
        ])
        y -= 4

        y = draw_section(c, y, 'FORMACAO')
        for t, s, d in [
            ('Curso de Ciberseguranca', 'ISCTE - Instituto Universitario de Lisboa', 'Nov 2025 - Jul 2026'),
            ('Licenciatura Relacoes Internacionais', 'Universidade de Evora', '2012 - 2015'),
            ('Curso Profissional Turismo', 'Escola Secundaria Severim Faria, Evora', '2009 - 2011'),
        ]:
            y = draw_entry(c, y, t, s, d)

        y = draw_section(c, y, 'IDIOMAS') if y > 8*cm else y
        c.setFont('CR', 9)
        c.setFillColor(PRETO)
        c.drawString(M, y, 'Portugues: Nativo  |  Ingles: Avancado (C1)')

        c.setFont('CR', 7)
        c.setFillColor(CINZA_CLARO)
        c.drawCentredString(W/2, 1.5*cm, 'CV atualizado Junho 2026  |  arturfilipe.work')

    c.save()
    print(f'{filename} -> OK')

out_dir = r'C:\Users\artur\arturfilipe.pt'
make_cv('cv-artur-filipe-en.pdf', 'en')
make_cv('cv-artur-filipe-pt.pdf', 'pt')
print('Done!')
