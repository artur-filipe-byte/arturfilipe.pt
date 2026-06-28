1|#!/usr/bin/env python3
2|"""Generate CV PDF for Artur Filipe - IT & Cybersecurity focus, aligned with LinkedIn."""
3|
4|from fpdf import FPDF
5|import os
6|
7|class CVPDF(FPDF):
8|    def header(self):
9|        pass
10|
11|    def footer(self):
12|        self.set_y(-15)
13|        self.set_font('Helvetica', 'I', 7)
14|        self.set_text_color(148, 148, 148)
15|        self.cell(0, 10, f'CV atualizado em Junho 2026  |  arturfilipe.work  |  github.com/artur-filipe-byte', 0, 0, 'C')
16|
17|    def section_title(self, title):
18|        self.set_font('Helvetica', 'B', 11)
19|        self.set_text_color(56, 189, 248)
20|        self.cell(0, 7, title.upper(), 0, 1)
21|        self.set_draw_color(56, 189, 248)
22|        self.set_line_width(0.3)
23|        self.line(self.get_x(), self.get_y(), self.get_x() + 190, self.get_y())
24|        self.ln(3)
25|
26|    def bullet(self, text):
27|        self.set_font('Helvetica', '', 9)
28|        self.set_text_color(220, 220, 220)
29|        self.set_x(20)
30|        self.multi_cell(170, 4.5, '- ' + text)
31|
32|    def body_text(self, text, bold=False):
33|        style = 'B' if bold else ''
34|        self.set_font('Helvetica', style, 9)
35|        self.set_text_color(220, 220, 220)
36|        self.multi_cell(0, 4.5, text)
37|
38|    def entry_header(self, title, subtitle, period):
39|        self.set_font('Helvetica', 'B', 10)
40|        self.set_text_color(255, 255, 255)
41|        self.cell(120, 5, title, 0, 0)
42|        self.set_font('Helvetica', '', 8)
43|        self.set_text_color(56, 189, 248)
44|        self.cell(0, 5, period, 0, 1, 'R')
45|        if subtitle:
46|            self.set_font('Helvetica', 'I', 8)
47|            self.set_text_color(148, 148, 148)
48|            self.cell(0, 4, subtitle, 0, 1)
49|        self.ln(1)
50|
51|    def skill_tag(self, label, value):
52|        self.set_font('Helvetica', 'B', 9)
53|        self.set_text_color(180, 180, 180)
54|        self.cell(40, 4.5, label)
55|        self.set_font('Helvetica', '', 9)
56|        self.set_text_color(220, 220, 220)
57|        self.cell(0, 4.5, value, 0, 1)
58|
59|
60|def create_cv_pt():
61|    pdf = CVPDF('P', 'mm', 'A4')
62|    pdf.set_auto_page_break(auto=True, margin=20)
63|    pdf.add_page()
64|
65|    # Background color
66|    pdf.set_fill_color(15, 17, 23)
67|    pdf.rect(0, 0, 210, 297, 'F')
68|
69|    # ========== HEADER ==========
70|    pdf.set_font('Helvetica', 'B', 26)
71|    pdf.set_text_color(255, 255, 255)
72|    pdf.ln(6)
73|    pdf.cell(0, 10, 'ARTUR FILIPE', 0, 1, 'C')
74|    pdf.set_font('Helvetica', '', 13)
75|    pdf.set_text_color(56, 189, 248)
76|    pdf.cell(0, 7, 'Profissional IT & Ciberseguranca', 0, 1, 'C')
77|    pdf.ln(3)
78|
79|    # Contact bar
80|    pdf.set_fill_color(22, 27, 39)
81|    pdf.set_draw_color(56, 189, 248)
82|    pdf.set_line_width(0.2)
83|    pdf.rect(15, pdf.get_y(), 180, 14, 'DF')
84|    pdf.set_font('Helvetica', '', 8)
85|    pdf.set_text_color(200, 200, 200)
86|    pdf.set_y(pdf.get_y() + 3)
87|    pdf.cell(60, 4, 'Evora, Portugal', 0, 0, 'C')
88|    pdf.cell(60, 4, 'artur.a.filipe@protonmail.com', 0, 0, 'C')
89|    pdf.cell(60, 4, 'arturfilipe.work', 0, 1, 'C')
90|    pdf.ln(6)
91|
92|    # ========== PROFILE ==========
93|    pdf.section_title('Perfil Profissional')
94|    pdf.body_text(
95|        'Profissional em transicao para IT e ciberseguranca com certificacoes CompTIA A+ e Security+. '
96|        'Construo projetos praticos no meu homelab - servidores, redes, firewall, SIEM - e documento '
97|        'tudo como prova de competencia tecnica. 13 anos de experiencia em atendimento ao cliente '
98|        'deram-me capacidades fortes de gestao de incidentes, comunicacao clara e resolucao rapida '
99|        'de problemas, que aplico diariamente nos meus projetos IT.'
100|    )
101|    pdf.ln(4)
102|
103|    # ========== CERTIFICATIONS ==========
104|    pdf.section_title('Certificacoes')
105|    pdf.entry_header('CompTIA A+ (770)', 'CompTIA - Hardware, SO, redes e suporte tecnico', 'Fev 2026')
106|    pdf.entry_header('CompTIA Security+', 'CompTIA - Seguranca de redes, gestao de risco e criptografia', 'Mar 2026')
107|    pdf.entry_header('Introducao a Ciberseguranca', 'Claranet / Formacao Profissional', 'Jun 2026')
108|    pdf.entry_header('Cyber Security 101', 'TryHackMe', 'Jan 2026')
109|    pdf.entry_header('Pre-Security Learning Path', 'TryHackMe', 'Jan 2026')
110|    pdf.ln(2)
111|
112|    # ========== EXPERIENCE ==========
113|    pdf.section_title('Experiencia Profissional')
114|
115|    # IT transition
116|    pdf.entry_header('Transicao para IT', 'Estudo e Projetos Praticos', '2026 - Presente')
117|    pdf.bullet('Homelab com pfSense, Suricata IDS/IPS, SIEM (Elastic Stack), Pi-hole e Docker')
118|    pdf.bullet('Automacao com Python: scripts de backup, bots Telegram, integracoes API')
119|    pdf.bullet('Documentacao rigorosa de cada projeto no GitHub (homelab-docs)')
120|    pdf.bullet('Portfolio pessoal: arturfilipe.work (GitHub Pages + Cloudflare + HTTPS)')
121|    pdf.ln(2)
122|
123|    # Hotel Casa do Vale
124|    pdf.entry_header('Casa do Vale Hotel - Rececao', 'Rececionista de Primeira - Evora', '2019 - 2026')
125|    pdf.bullet('Gestao completa do ciclo de acolhimento: check-in, check-out, faturacao e reservas online (Booking, Expedia)')
126|    pdf.bullet('Coordenacao de turnos, formacao de novos colaboradores e conformidade com protecao de dados')
127|    pdf.bullet('Atendimento presencial e telefonico em portugues e ingles')
128|    pdf.ln(2)
129|
130|    # Hotel Dom Fernando
131|    pdf.entry_header('Hotel Dom Fernando - Rececao', 'Rececionista - Evora', '2013 - 2019')
132|    pdf.bullet('Promovido a Rececionista de 1.a. Atendimento ao cliente, reservas, faturacao e resolucao de incidentes')
133|    pdf.bullet('Comunicacao intercultural, coordenacao interdepartamental e resolucao de problemas sob pressao')
134|    pdf.ln(2)
135|
136|    # Call center
137|    pdf.entry_header('Operador de Call Center / Assistencia em Viagem', 'Reditus - Evora', '2013 - 2014')
138|    pdf.bullet('Atendimento telefonico em portugues e ingles para seguros de viagem')
139|    pdf.ln(2)
140|
141|    # ========== TECHNICAL SKILLS ==========
142|    pdf.section_title('Competencias Tecnicas')
143|    pdf.skill_tag('Seguranca:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intel')
144|    pdf.skill_tag('Redes:', 'TCP/IP, DNS, DHCP, VLANs, firewall rules, pfSense, Wireshark, Nmap')
145|    pdf.skill_tag('Sistemas:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox')
146|    pdf.skill_tag('Ferramentas:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare')
147|    pdf.skill_tag('Servicos:', 'Nextcloud, Pi-hole, Jellyfin, Portainer')
148|    pdf.ln(2)
149|
150|    # ========== LANGUAGES ==========
151|    pdf.section_title('Idiomas')
152|    pdf.skill_tag('Portugues:', 'Nativo')
153|    pdf.skill_tag('Ingles:', 'Avancado (C1)')
154|    pdf.ln(2)
155|
156|    # ========== EDUCATION ==========
157|    pdf.section_title('Formacao')
158|    pdf.entry_header('Curso de Ciberseguranca', 'ISCTE - Instituto Universitario de Lisboa', 'Nov 2025 - Jul 2026')
159|    pdf.entry_header('Licenciatura em Relacoes Internacionais', 'Universidade de Evora', '2012 - 2015')
160|    pdf.entry_header('Curso Profissional de Turismo', 'Escola Secundaria Severim de Faria, Evora', '2009 - 2011')
161|
162|    return pdf
163|
164|
165|def create_cv_en():
166|    pdf = CVPDF('P', 'mm', 'A4')
167|    pdf.set_auto_page_break(auto=True, margin=20)
168|    pdf.add_page()
169|
170|    # Background color
171|    pdf.set_fill_color(15, 17, 23)
172|    pdf.rect(0, 0, 210, 297, 'F')
173|
174|    # ========== HEADER ==========
175|    pdf.set_font('Helvetica', 'B', 26)
176|    pdf.set_text_color(255, 255, 255)
177|    pdf.ln(6)
178|    pdf.cell(0, 10, 'ARTUR FILIPE', 0, 1, 'C')
179|    pdf.set_font('Helvetica', '', 13)
180|    pdf.set_text_color(56, 189, 248)
181|    pdf.cell(0, 7, 'IT & Cybersecurity Professional', 0, 1, 'C')
182|    pdf.ln(3)
183|
184|    # Contact bar
185|    pdf.set_fill_color(22, 27, 39)
186|    pdf.set_draw_color(56, 189, 248)
187|    pdf.set_line_width(0.2)
188|    pdf.rect(15, pdf.get_y(), 180, 14, 'DF')
189|    pdf.set_font('Helvetica', '', 8)
190|    pdf.set_text_color(200, 200, 200)
191|    pdf.set_y(pdf.get_y() + 3)
192|    pdf.cell(60, 4, 'Evora, Portugal', 0, 0, 'C')
193|    pdf.cell(60, 4, 'artur.a.filipe@protonmail.com', 0, 0, 'C')
194|    pdf.cell(60, 4, 'arturfilipe.work', 0, 1, 'C')
195|    pdf.ln(6)
196|
197|    # ========== PROFILE ==========
198|    pdf.section_title('Professional Profile')
199|    pdf.body_text(
200|        'Professional transitioning to IT and cybersecurity with CompTIA A+ and Security+ certifications. '
201|        'I build hands-on projects in my homelab - servers, networks, firewalls, SIEM - and document '
202|        'everything as proof of technical competence. 13 years of customer-facing experience gave me '
203|        'strong incident management, clear communication, and fast problem-solving skills that I apply '
204|        'daily in my IT projects.'
205|    )
206|    pdf.ln(4)
207|
208|    # ========== CERTIFICATIONS ==========
209|    pdf.section_title('Certifications')
210|    pdf.entry_header('CompTIA A+ (770)', 'CompTIA - Hardware, OS, networking and support foundation', 'Feb 2026')
211|    pdf.entry_header('CompTIA Security+', 'CompTIA - Network security, risk management and cryptography', 'Mar 2026')
212|    pdf.entry_header('Introduction to Cybersecurity', 'Claranet / Professional Training', 'Jun 2026')
213|    pdf.entry_header('Cyber Security 101', 'TryHackMe', 'Jan 2026')
214|    pdf.entry_header('Pre-Security Learning Path', 'TryHackMe', 'Jan 2026')
215|    pdf.ln(2)
216|
217|    # ========== EXPERIENCE ==========
218|    pdf.section_title('Professional Experience')
219|
220|    # IT transition
221|    pdf.entry_header('Transition to IT', 'Study and Hands-on Projects', '2026 - Present')
222|    pdf.bullet('Homelab with pfSense, Suricata IDS/IPS, Elastic SIEM, Pi-hole and Docker')
223|    pdf.bullet('Python automation: backup scripts, Telegram bots, API integrations')
224|    pdf.bullet('Rigorous documentation of all projects on GitHub (homelab-docs)')
225|    pdf.bullet('Personal portfolio: arturfilipe.work (GitHub Pages + Cloudflare + HTTPS)')
226|    pdf.ln(2)
227|
228|    # Hotel Casa do Vale
229|    pdf.entry_header('Casa do Vale Hotel - Front Desk', 'First Receptionist - Evora', '2019 - 2026')
230|    pdf.bullet('Full guest cycle management: check-in, check-out, invoicing and online reservations (Booking, Expedia)')
231|    pdf.bullet('Shift coordination, new staff training and compliance with data protection policies')
232|    pdf.bullet('In-person and phone service in Portuguese and English')
233|    pdf.ln(2)
234|
235|    # Hotel Dom Fernando
236|    pdf.entry_header('Hotel Dom Fernando - Front Desk', 'Receptionist - Evora', '2013 - 2019')
237|    pdf.bullet('Promoted to First Receptionist. Customer service, reservations, invoicing, real-time incident resolution')
238|    pdf.bullet('Developed intercultural communication, interdepartmental coordination and problem-solving skills')
239|    pdf.ln(2)
240|
241|    # Call center
242|    pdf.entry_header('Call Center Operator / Travel Assistance', 'Reditus - Evora', '2013 - 2014')
243|    pdf.bullet('Phone support in Portuguese and English for travel insurance')
244|    pdf.ln(2)
245|
246|    # ========== TECHNICAL SKILLS ==========
247|    pdf.section_title('Technical Skills')
248|    pdf.skill_tag('Security:', 'Network security, IDS/IPS (Suricata), SIEM (Elastic Stack), threat intel')
249|    pdf.skill_tag('Networking:', 'TCP/IP, DNS, DHCP, VLANs, firewall rules, pfSense, Wireshark, Nmap')
250|    pdf.skill_tag('Systems:', 'Linux (Ubuntu/Debian), Windows Server, Proxmox, VirtualBox')
251|    pdf.skill_tag('Tools:', 'Docker, Docker Compose, Python, Bash, Git, Cloudflare')
252|    pdf.skill_tag('Services:', 'Nextcloud, Pi-hole, Jellyfin, Portainer')
253|    pdf.ln(2)
254|
255|    # ========== LANGUAGES ==========
256|    pdf.section_title('Languages')
257|    pdf.skill_tag('Portuguese:', 'Native')
258|    pdf.skill_tag('English:', 'Advanced (C1)')
259|    pdf.ln(2)
260|
261|    # ========== EDUCATION ==========
262|    pdf.section_title('Education')
263|    pdf.entry_header('Cybersecurity Course', 'ISCTE - University Institute of Lisbon', 'Nov 2025 - Jul 2026')
264|    pdf.entry_header('Bachelor in International Relations', 'University of Evora', '2012 - 2015')
265|    pdf.entry_header('Professional Tourism Course', 'Severim de Faria High School, Evora', '2009 - 2011')
266|
267|    return pdf
268|
269|
270|if __name__ == '__main__':
271|    output_dir = r'C:\Users\artur\arturfilipe.pt'
272|
273|    # Portuguese CV
274|    pdf_pt = create_cv_pt()
275|    pt_path = os.path.join(output_dir, 'cv-artur-filipe.pdf')
276|    pdf_pt.output(pt_path)
277|    print(f'Portuguese CV saved to: {pt_path}')
278|
279|    print('Done!')
280|