#!/usr/bin/env python3
from fpdf import FPDF
import os

class CV(FPDF):
    def header(self): pass
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica','I',7)
        self.set_text_color(148,148,148)
        self.cell(0,10,'CV Jun 2026 | arturfilipe.work',0,0,'C')
    def sec(self,t):
        self.set_font('Helvetica','B',11)
        self.set_text_color(56,189,248)
        self.cell(0,7,t.upper(),0,1)
        self.set_draw_color(56,189,248)
        self.set_line_width(0.3)
        self.line(self.get_x(),self.get_y(),self.get_x()+190,self.get_y())
        self.ln(3)
    def hdr(self,t,s,p):
        self.set_font('Helvetica','B',10)
        self.set_text_color(255,255,255)
        self.cell(120,5,t,0,0)
        self.set_font('Helvetica','',8)
        self.set_text_color(56,189,248)
        self.cell(0,5,p,0,1,'R')
        if s:
            self.set_font('Helvetica','I',8)
            self.set_text_color(148,148,148)
            self.cell(0,4,s,0,1)
        self.ln(1)
    def b(self,t):
        self.set_font('Helvetica','',9)
        self.set_text_color(220,220,220)
        self.set_x(18)
        self.multi_cell(172,4.5,'- '+t)
    def txt(self,t):
        self.set_font('Helvetica','',9)
        self.set_text_color(220,220,220)
        self.set_x(15)
        self.multi_cell(180,4.5,t)
    def skill(self,l,v):
        self.set_font('Helvetica','B',9)
        self.set_text_color(180,180,180)
        self.cell(40,4.5,l)
        self.set_font('Helvetica','',9)
        self.set_text_color(220,220,220)
        self.cell(0,4.5,v,0,1)

d = r'C:\Users\artur\arturfilipe.pt'

for lang, name, headline, profile, certs, exp, skills, edu in [
    ('pt','cv-artur-filipe.pdf','Profissional IT & Ciberseguranca',
     'Profissional em transicao para IT e ciberseguranca com certificacoes CompTIA A+ e Security+. Construo projetos praticos no meu homelab - servidores, redes, firewall, SIEM - e documento tudo como prova de competencia tecnica. 13 anos de experiencia em atendimento ao cliente deram-me capacidades fortes de gestao de incidentes, comunicacao clara e resolucao rapida de problemas.',
     [('CompTIA A+ (770)','CompTIA - Hardware, SO, redes','Fev 2026'),
      ('CompTIA Security+','CompTIA - Seguranca de redes, risco','Mar 2026'),
      ('Intro. a Ciberseguranca','Claranet','Jun 2026'),
      ('Cyber Security 101','TryHackMe','Jan 2026'),
      ('Pre-Security','TryHackMe','Jan 2026')],
     [('Transicao para IT','Estudo e Projetos Praticos','2026 - Presente',
       ['Homelab com pfSense, Suricata IDS/IPS, SIEM (Elastic Stack), Pi-hole e Docker',
        'Automacao com Python: scripts de backup, bots Telegram, integracoes API',
        'Documentacao rigorosa de cada projeto no GitHub (homelab-docs)',
        'Portfolio: arturfilipe.work (Cloudflare + HTTPS)']),
      ('Casa do Vale Hotel - Rececao','Rececionista de Primeira - Evora','2019 - 2026',
       ['Gestao completa do ciclo de acolhimento: check-in, checkout, faturacao, reservas online',
        'Coordenacao de turnos, formacao e conformidade com protecao de dados',
        'Atendimento presencial e telefonico em PT e EN']),
      ('Hotel Dom Fernando - Rececao','Rececionista - Evora','2013 - 2019',
       ['Promovido a Rececionista de 1a. Atendimento, reservas, faturacao, incidencias',
        'Comunicacao intercultural, coordenacao interdepartamental, resolucao de problemas']),
      ('Operador Call Center','Reditus - Evora','2013 - 2014',
       ['Atendimento telefonico PT/EN para seguros de viagem'])],
     [('Seguranca:','Network security, IDS/IPS (Suricata), SIEM (Elastic Stack)'),
      ('Redes:','TCP/IP, DNS, DHCP, VLANs, pfSense, Wireshark, Nmap'),
      ('Sistemas:','Linux (Ubuntu/Debian), Windows Server, Proxmox'),
      ('Ferramentas:','Docker, Python, Bash, Git, Cloudflare'),
      ('Servicos:','Nextcloud, Pi-hole, Jellyfin, Portainer')],
     [('Curso de Ciberseguranca','ISCTE - Univ. Lisboa','Nov 2025 - Jul 2026'),
      ('Lic. Relacoes Internacionais','Univ. Evora','2012 - 2015'),
      ('Curso Prof. Turismo','Esc. Severim Faria, Evora','2009 - 2011')]),
]:
    pdf = CV('P','mm','A4')
    pdf.set_auto_page_break(auto=True,margin=20)
    pdf.add_page()
    pdf.set_fill_color(15,17,23)
    pdf.rect(0,0,210,297,'F')
    
    pdf.set_font('Helvetica','B',26)
    pdf.set_text_color(255,255,255)
    pdf.ln(6)
    pdf.cell(0,10,'ARTUR FILIPE',0,1,'C')
    pdf.set_font('Helvetica','',13)
    pdf.set_text_color(56,189,248)
    pdf.cell(0,7,headline,0,1,'C')
    pdf.ln(3)
    
    pdf.set_fill_color(22,27,39)
    pdf.set_draw_color(56,189,248)
    pdf.set_line_width(0.2)
    pdf.rect(15,pdf.get_y(),180,14,'DF')
    pdf.set_font('Helvetica','',8)
    pdf.set_text_color(200,200,200)
    pdf.set_y(pdf.get_y()+3)
    pdf.cell(60,4,'Evora, Portugal',0,0,'C')
    pdf.cell(60,4,'artur.a.filipe@protonmail.com',0,0,'C')
    pdf.cell(60,4,'arturfilipe.work',0,1,'C')
    pdf.ln(6)
    
    pdf.sec('Perfil Profissional' if lang=='pt' else 'Professional Profile')
    pdf.txt(profile)
    pdf.ln(4)
    
    pdf.sec('Certificacoes' if lang=='pt' else 'Certifications')
    for t,s,p in certs: pdf.hdr(t,s,p)
    pdf.ln(2)
    
    pdf.sec('Experiencia Profissional' if lang=='pt' else 'Professional Experience')
    for t,s,p,bs in exp:
        pdf.hdr(t,s,p)
        for b in bs: pdf.b(b)
        pdf.ln(2)
    
    pdf.sec('Competencias Tecnicas' if lang=='pt' else 'Technical Skills')
    for l,v in skills: pdf.skill(l,v)
    pdf.ln(2)
    
    pdf.sec('Idiomas' if lang=='pt' else 'Languages')
    if lang=='pt':
        pdf.skill('Portugues:','Nativo')
        pdf.skill('Ingles:','Avancado (C1)')
    else:
        pdf.skill('Portuguese:','Native')
        pdf.skill('English:','Advanced (C1)')
    pdf.ln(2)
    
    pdf.sec('Formacao' if lang=='pt' else 'Education')
    for t,s,p in edu: pdf.hdr(t,s,p)
    
    pdf.output(os.path.join(d, name))
    print(f'{name} -> OK [{os.path.join(d,name)}]')
