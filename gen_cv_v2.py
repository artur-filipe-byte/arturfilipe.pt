#!/usr/bin/env python3
# Generate CV B (ATS Help Desk) and CV C (Hospitality-IT), PT + EN.
# Portable: built-in Helvetica fonts, writes next to this script.
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
import os

FB, FR, FI = 'Helvetica-Bold', 'Helvetica', 'Helvetica-Oblique'

AZUL, CINZA, CINZA_CLARO, PRETO, LINHA = (
    HexColor('#1a5276'), HexColor('#5d6d7e'), HexColor('#aab7b8'),
    HexColor('#2c3e50'), HexColor('#d5dbdb'))

M = 2.2 * cm
W, H = A4
CW = W - 2 * M

def wrap(c, texto, tam, largura):
    linhas, cur = [], ''
    for w in texto.split():
        teste = (cur + ' ' + w) if cur else w
        if c.stringWidth(teste, FR, tam) <= largura:
            cur = teste
        else:
            linhas.append(cur); cur = w
    if cur:
        linhas.append(cur)
    return linhas

def draw_header(c, y):
    c.setFont(FB, 22); c.setFillColor(PRETO); c.drawCentredString(W/2, y, 'ARTUR FILIPE'); y -= 26
    c.setFont(FR, 8); c.setFillColor(CINZA)
    c.drawCentredString(W/2, y, 'Evora, Portugal  |  artur.a.filipe@protonmail.com  |  +351 968 856 700'); y -= 12
    c.setFont(FR, 8); c.setFillColor(CINZA)
    c.drawCentredString(W/2, y, 'arturfilipe.work  |  linkedin.com/in/artur-filipe-it  |  github.com/artur-filipe-byte'); y -= 16
    c.setStrokeColor(LINHA); c.setLineWidth(1); c.line(M, y, W-M, y); y -= 16
    return y

def draw_section(c, y, title):
    c.setFont(FB, 10); c.setFillColor(AZUL); c.drawString(M, y, title); y -= 4
    c.setStrokeColor(LINHA); c.setLineWidth(0.5); c.line(M, y, W-M, y); y -= 12
    return y

def draw_entry(c, y, titulo, subtitulo, data):
    c.setFont(FB, 9); c.setFillColor(PRETO); c.drawString(M, y, titulo)
    c.setFont(FR, 8); c.setFillColor(CINZA); larg = c.stringWidth(data, FR, 8)
    c.drawString(W-M-larg, y, data); y -= 11
    if subtitulo:
        c.setFont(FI, 8); c.setFillColor(CINZA); c.drawString(M, y, subtitulo); y -= 12
    return y

def draw_bullets(c, y, bullets):
    for b in bullets:
        c.setFont(FR, 8.5); c.setFillColor(PRETO)
        for linha in wrap(c, '  ' + b, 8.5, CW-8):
            c.drawString(M+6, y, linha); y -= 10
    return y

def draw_skills(c, y, data):
    for label, valor in data:
        c.setFont(FB, 9); c.setFillColor(PRETO); larg = c.stringWidth(label, FB, 9)
        c.drawString(M, y, label)
        c.setFont(FR, 8.5); c.setFillColor(PRETO); c.drawString(M+larg+5, y, valor); y -= 13
    return y

CERTS_PT = [
    ('CompTIA A+ (770)', 'CompTIA - Hardware, SO, redes e suporte t\u00e9cnico', 'Fev 2026'),
    ('CompTIA Security+', 'CompTIA - Seguran\u00e7a de redes, gest\u00e3o de risco, criptografia', 'Mar 2026'),
    ('PECB ISO/IEC 27001 Foundation', 'Governan\u00e7a, risco e conformidade (GRC) em seguran\u00e7a da informa\u00e7\u00e3o', '2026'),
    ('Introdu\u00e7\u00e3o \u00e0 Ciberseguran\u00e7a', 'Claranet / Forma\u00e7\u00e3o Profissional', 'Jun 2026'),
    ('Cyber Security 101', 'TryHackMe', 'Jan 2026'),
]
CERTS_EN = [
    ('CompTIA A+ (770)', 'CompTIA - Hardware, OS, networking and technical support', 'Feb 2026'),
    ('CompTIA Security+', 'CompTIA - Network security, risk management, crypto', 'Mar 2026'),
    ('PECB ISO/IEC 27001 Foundation', 'Information security governance, risk & compliance (GRC)', '2026'),
    ('Introduction to Cybersecurity', 'Claranet / Professional Training', 'Jun 2026'),
    ('Cyber Security 101', 'TryHackMe', 'Jan 2026'),
]

def make_b(lang):
    fn = 'cv-artur-filipe-en.pdf' if lang == 'en' else 'cv-artur-filipe-pt.pdf'
    c = canvas.Canvas(os.path.join(OUT, fn), pagesize=A4); c.setTitle('Artur Filipe - CV')
    y = H - M
    if lang == 'en':
        y = draw_header(c, y)
        y = draw_section(c, y, 'PROFESSIONAL PROFILE')
        c.setFont(FR, 9); c.setFillColor(PRETO)
        for l in wrap(c, 'After 13 years at a hotel reception desk, dealing with pressure, people and real-time problem solving, I made a focused transition into IT and cybersecurity. It was during that journey that I started studying out of curiosity and realised this is what I want to do. I now hold CompTIA A+, Security+ and PECB ISO/IEC 27001 Foundation and I am looking for IT Support, Service Desk or Help Desk roles in Portugal or remote.', 9, CW):
            c.drawString(M, y, l); y -= 11
        y -= 8
        y = draw_section(c, y, 'CERTIFICATIONS')
        for t, s, d in CERTS_EN: y = draw_entry(c, y, t, s, d)
        y -= 4
        y = draw_section(c, y, 'PROFESSIONAL EXPERIENCE')
        for t, s, p, bs in [
            ('Transition to IT', 'Study and Hands-on Projects', '2026 - Present',
             ['Linux homelab: Pi-hole, Docker, Nextcloud, networking and automation',
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
            y = draw_entry(c, y, t, s, p); y = draw_bullets(c, y, bs); y -= 4
        y = draw_section(c, y, 'TECHNICAL SKILLS')
        y = draw_skills(c, y, [
            ('Security:', 'Network security, threat intel, ISO 27001 / GRC'),
            ('Networking:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, firewall rules, Wireshark, Nmap'),
            ('Systems:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
            ('Tools:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare, Nextcloud, Pi-hole'),
        ]); y -= 4
        y = draw_section(c, y, 'EDUCATION')
        for t, s, d in [
            ('Cybersecurity Course', 'ISCTE - University Institute of Lisbon', 'Nov 2025 - Jul 2026'),
            ("Bachelor's in International Relations", 'University of Evora', '2012 - 2015'),
            ('Professional Tourism Course', 'Severim de Faria High School, Evora', '2009 - 2011'),
        ]: y = draw_entry(c, y, t, s, d)
        y = draw_section(c, y, 'LANGUAGES')
        c.setFont(FR, 9); c.setFillColor(PRETO); c.drawString(M, y, 'Portuguese: Native  |  English: Advanced (C1)')
        c.setFont(FR, 7); c.setFillColor(CINZA_CLARO); c.drawCentredString(W/2, 1.5*cm, 'CV updated Oct 2026  |  arturfilipe.work')
    else:
        y = draw_header(c, y)
        y = draw_section(c, y, 'PERFIL PROFISSIONAL')
        c.setFont(FR, 9); c.setFillColor(PRETO)
        for l in wrap(c, 'Depois de 13 anos na receção de um hotel, a lidar com pressão, pessoas e problemas para resolver em tempo real, fiz uma transição focada para IT e cibersegurança. Foi durante esse percurso que comecei a estudar por curiosidade e descobri que era isto que queria fazer. Hoje tenho as certificações CompTIA A+, Security+ e PECB ISO/IEC 27001 Foundation e procuro funções de IT Support, Service Desk ou Help Desk em Portugal ou remoto.', 9, CW):
            c.drawString(M, y, l); y -= 11
        y -= 8
        y = draw_section(c, y, 'CERTIFICA\u00c7\u00d5ES')
        for t, s, d in CERTS_PT: y = draw_entry(c, y, t, s, d)
        y -= 4
        y = draw_section(c, y, 'EXPERI\u00caNCIA PROFISSIONAL')
        for t, s, p, bs in [
            ('Transi\u00e7\u00e3o para IT', 'Estudo e Projetos Pr\u00e1ticos', '2026 - Presente',
             ['Homelab Linux: Pi-hole, Docker, Nextcloud, redes e automa\u00e7\u00e3o',
              'Automa\u00e7\u00e3o Python: scripts backup, bots Telegram, integra\u00e7\u00f5es API',
              'Documenta\u00e7\u00e3o rigorosa no GitHub; portfolio em arturfilipe.work']),
            ('Casa do Vale Hotel - Rece\u00e7\u00e3o', 'Rececionista de 1\u00aa | \u00c9vora, Portugal', '2019 - 2026',
             ['Ciclo completo do h\u00f3spede: check-in/out, fatura\u00e7\u00e3o, reservas online (Booking, Expedia)',
              'Coordena\u00e7\u00e3o turnos, forma\u00e7\u00e3o, conformidade RGPD, controlo acesso, documenta\u00e7\u00e3o incidentes',
              'Atendimento em portugu\u00eas e ingl\u00eas (presencial e telef\u00f3nico)']),
            ('Hotel Dom Fernando - Rece\u00e7\u00e3o', 'Rececionista | \u00c9vora, Portugal', '2013 - 2019',
             ['Promovido a Rececionista de 1\u00aa. Atendimento cliente, reservas, fatura\u00e7\u00e3o, incid\u00eancias',
              'Comunica\u00e7\u00e3o intercultural e coordena\u00e7\u00e3o interdepartamental']),
            ('Operador Call Center', 'Reditus - Assist\u00eancia Viagem | \u00c9vora, Portugal', '2013 - 2014',
             ['Apoio telef\u00f3nico PT/EN para seguros de viagem e emerg\u00eancias']),
        ]:
            y = draw_entry(c, y, t, s, p); y = draw_bullets(c, y, bs); y -= 4
        y = draw_section(c, y, 'COMPET\u00caNCIAS T\u00c9CNICAS')
        y = draw_skills(c, y, [
            ('Seguran\u00e7a:', 'Network security, threat intel, ISO 27001 / GRC'),
            ('Redes:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, firewall rules, Wireshark, Nmap'),
            ('Sistemas:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
            ('Ferramentas:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare, Nextcloud, Pi-hole'),
        ]); y -= 4
        y = draw_section(c, y, 'FORMA\u00c7\u00c3O')
        for t, s, d in [
            ('Curso de Ciberseguran\u00e7a', 'ISCTE - Instituto Universit\u00e1rio de Lisboa', 'Nov 2025 - Jul 2026'),
            ('Licenciatura Rela\u00e7\u00f5es Internacionais', 'Universidade de \u00c9vora', '2012 - 2015'),
            ('Curso Profissional Turismo', 'Escola Secund\u00e1ria Severim Faria, \u00c9vora', '2009 - 2011'),
        ]: y = draw_entry(c, y, t, s, d)
        y = draw_section(c, y, 'IDIOMAS')
        c.setFont(FR, 9); c.setFillColor(PRETO); c.drawString(M, y, 'Portugu\u00eas: Nativo  |  Ingl\u00eas: Avan\u00e7ado (C1)')
        c.setFont(FR, 7); c.setFillColor(CINZA_CLARO); c.drawCentredString(W/2, 1.5*cm, 'CV atualizado Out 2026  |  arturfilipe.work')
    c.save(); print(fn, '-> OK')

def make_c(lang):
    fn = 'cv-artur-filipe-hospitality-en.pdf' if lang == 'en' else 'cv-artur-filipe-hospitality-pt.pdf'
    c = canvas.Canvas(os.path.join(OUT, fn), pagesize=A4); c.setTitle('Artur Filipe - Hospitality IT CV')
    y = H - M
    if lang == 'en':
        y = draw_header(c, y)
        y = draw_section(c, y, 'PROFESSIONAL PROFILE')
        c.setFont(FR, 9); c.setFillColor(PRETO)
        for l in wrap(c, 'IT professional with 13 years inside hotel operations and deep PMS (Property Management System) expertise, now CompTIA A+ and Security+ and PECB ISO/IEC 27001 Foundation certified. Uniquely positioned to support the technology of hotels and hospitality businesses - PMS, channel managers (Booking/Expedia), payments, networks, security and backups - speaking both the front-desk language and the server language. Seeking IT Support / Systems / Hospitality-Tech roles in Portugal or remote.', 9, CW):
            c.drawString(M, y, l); y -= 11
        y -= 8
        y = draw_section(c, y, 'CERTIFICATIONS')
        for t, s, d in CERTS_EN: y = draw_entry(c, y, t, s, d)
        y -= 4
        y = draw_section(c, y, 'RELEVANT EXPERIENCE')
        for t, s, p, bs in [
            ('Casa do Vale Hotel - Front Desk', 'First Receptionist | Evora, Portugal', '2019 - 2026',
             ['Daily operation of hotel PMS / management software across the full guest lifecycle (Booking, Expedia)',
              'Maintained GDPR compliance, access control and incident documentation',
              'Trained staff and coordinated shifts under peak-occupancy pressure',
              'First point of contact for guest and system issues - translating tech to non-technical colleagues']),
            ('Hotel Dom Fernando - Front Desk', 'Receptionist | Evora, Portugal', '2013 - 2019',
             ['Promoted to First Receptionist; intercultural and interdepartmental coordination',
              'Resolved operational and guest-tech issues in real time']),
            ('Transition to IT', 'Study and Hands-on Projects', '2026 - Present',
             ['Linux homelab: Pi-hole, Docker, Nextcloud, networking and automation',
              'Python automation; security fundamentals (A+, Security+, ISO 27001)']),
        ]:
            y = draw_entry(c, y, t, s, p); y = draw_bullets(c, y, bs); y -= 4
        y = draw_section(c, y, 'HOSPITALITY TECH SKILLS')
        y = draw_skills(c, y, [
            ('Hospitality systems:', 'PMS / hotel management software, channel managers, booking integrations, payment terminals'),
            ('Security:', 'Network security, ISO 27001 / GRC, threat intel'),
            ('Networking:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, firewall rules, Wireshark, Nmap'),
            ('Systems:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
            ('Tools:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare, Nextcloud, Pi-hole'),
        ]); y -= 4
        y = draw_section(c, y, 'EDUCATION')
        for t, s, d in [
            ('Cybersecurity Course', 'ISCTE - University Institute of Lisbon', 'Nov 2025 - Jul 2026'),
            ('Professional Tourism Course', 'Severim de Faria High School, Evora', '2009 - 2011'),
        ]: y = draw_entry(c, y, t, s, d)
        y = draw_section(c, y, 'LANGUAGES')
        c.setFont(FR, 9); c.setFillColor(PRETO); c.drawString(M, y, 'Portuguese: Native  |  English: Advanced (C1)')
        c.setFont(FR, 7); c.setFillColor(CINZA_CLARO); c.drawCentredString(W/2, 1.5*cm, 'CV updated Oct 2026  |  arturfilipe.work')
    else:
        y = draw_header(c, y)
        y = draw_section(c, y, 'PERFIL PROFISSIONAL')
        c.setFont(FR, 9); c.setFillColor(PRETO)
        for l in wrap(c, 'Profissional de IT com 13 anos dentro da opera\u00e7\u00e3o de hot\u00e9is e dom\u00ednio profundo de PMS (Property Management System), agora com certifica\u00e7\u00f5es CompTIA A+ e Security+ e PECB ISO/IEC 27001 Foundation. Posicionado de forma \u00fanica para suportar a tecnologia de hot\u00e9is e neg\u00f3cios de hospitalidade - PMS, channel managers (Booking/Expedia), pagamentos, redes, seguran\u00e7a e backups - falando tanto a linguagem da rece\u00e7\u00e3o como a do servidor. Procuro fun\u00e7\u00f5es de IT Support / Sistemas / Hospitality-Tech em Portugal ou remoto.', 9, CW):
            c.drawString(M, y, l); y -= 11
        y -= 8
        y = draw_section(c, y, 'CERTIFICA\u00c7\u00d5ES')
        for t, s, d in CERTS_PT: y = draw_entry(c, y, t, s, d)
        y -= 4
        y = draw_section(c, y, 'EXPERI\u00caNCIA RELEVANTE')
        for t, s, p, bs in [
            ('Casa do Vale Hotel - Rece\u00e7\u00e3o', 'Rececionista de 1\u00aa | \u00c9vora, Portugal', '2019 - 2026',
             ['Opera\u00e7\u00e3o di\u00e1ria de PMS / software de gest\u00e3o de hotel no ciclo completo do h\u00f3spede (Booking, Expedia)',
              'Assegurou conformidade RGPD, controlo de acesso e documenta\u00e7\u00e3o de incidentes',
              'Formou colegas e coordenou turnos sob press\u00e3o de ocupa\u00e7\u00e3o m\u00e1xima',
              'Primeiro ponto de contacto para problemas de h\u00f3spedes e sistemas - traduzindo tech para colegas n\u00e3o t\u00e9cnicos']),
            ('Hotel Dom Fernando - Rece\u00e7\u00e3o', 'Rececionista | \u00c9vora, Portugal', '2013 - 2019',
             ['Promovido a Rececionista de 1\u00aa; coordena\u00e7\u00e3o intercultural e interdepartamental',
              'Resolveu problemas operacionais e tecnol\u00f3gicos em tempo real']),
            ('Transi\u00e7\u00e3o para IT', 'Estudo e Projetos Pr\u00e1ticos', '2026 - Presente',
             ['Homelab Linux: Pi-hole, Docker, Nextcloud, redes e automa\u00e7\u00e3o',
              'Automa\u00e7\u00e3o Python; fundamentos de seguran\u00e7a (A+, Security+, ISO 27001)']),
        ]:
            y = draw_entry(c, y, t, s, p); y = draw_bullets(c, y, bs); y -= 4
        y = draw_section(c, y, 'COMPET\u00caNCIAS DE HOSPITALIDADE-TECH')
        y = draw_skills(c, y, [
            ('Sistemas hospitalidade:', 'PMS / software gest\u00e3o hotel, channel managers, integra\u00e7\u00f5es reservas, terminais pagamento'),
            ('Seguran\u00e7a:', 'Network security, ISO 27001 / GRC, threat intel'),
            ('Redes:', 'TCP/IP, DNS, DHCP, VLANs, pfSense, firewall rules, Wireshark, Nmap'),
            ('Sistemas:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox'),
            ('Ferramentas:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare, Nextcloud, Pi-hole'),
        ]); y -= 4
        y = draw_section(c, y, 'FORMA\u00c7\u00c3O')
        for t, s, d in [
            ('Curso de Ciberseguran\u00e7a', 'ISCTE - Instituto Universit\u00e1rio de Lisboa', 'Nov 2025 - Jul 2026'),
            ('Curso Profissional Turismo', 'Escola Secund\u00e1ria Severim Faria, \u00c9vora', '2009 - 2011'),
        ]: y = draw_entry(c, y, t, s, d)
        y = draw_section(c, y, 'IDIOMAS')
        c.setFont(FR, 9); c.setFillColor(PRETO); c.drawString(M, y, 'Portugu\u00eas: Nativo  |  Ingl\u00eas: Avan\u00e7ado (C1)')
        c.setFont(FR, 7); c.setFillColor(CINZA_CLARO); c.drawCentredString(W/2, 1.5*cm, 'CV atualizado Out 2026  |  arturfilipe.work')
    c.save(); print(fn, '-> OK')

OUT = os.path.dirname(os.path.abspath(__file__))
make_b('en'); make_b('pt'); make_c('en'); make_c('pt')
print('Done!')
