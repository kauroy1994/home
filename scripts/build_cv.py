from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,KeepTogether,HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_RIGHT

src=Path('scripts/cv_reference.txt').read_text()
for name,path in [('Lato','/usr/share/fonts/truetype/lato/Lato-Regular.ttf'),('LatoBold','/usr/share/fonts/truetype/lato/Lato-Bold.ttf'),('LatoItalic','/usr/share/fonts/truetype/lato/Lato-Italic.ttf'),('Serif','/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'),('SerifBold','/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,path))
C=HexColor('#9E1B32');D=HexColor('#24262D');M=HexColor('#56616A');P=HexColor('#E9DDE0');BG=HexColor('#F6EDEF');G=HexColor('#9BA1A6')
styles={
 'name':ParagraphStyle('name',fontName='SerifBold',fontSize=32,leading=36,textColor=D),
 'position':ParagraphStyle('position',fontName='LatoBold',fontSize=10.8,leading=15,textColor=C),
 'contact':ParagraphStyle('contact',fontName='Lato',fontSize=8.3,leading=13,textColor=M),
 'heading':ParagraphStyle('heading',fontName='LatoBold',fontSize=11.1,leading=15.5,textColor=C,spaceAfter=8,keepWithNext=True),
 'sub':ParagraphStyle('sub',fontName='LatoBold',fontSize=9.3,leading=13,textColor=D,spaceBefore=9,spaceAfter=5,keepWithNext=True),
 'body':ParagraphStyle('body',fontName='Lato',fontSize=9.1,leading=14,textColor=D,spaceAfter=6),
 'date':ParagraphStyle('date',fontName='LatoBold',fontSize=8.3,leading=13,textColor=C),
 'pub':ParagraphStyle('pub',fontName='Lato',fontSize=8.55,leading=13.1,textColor=D,spaceAfter=0),
 'num':ParagraphStyle('num',fontName='LatoBold',fontSize=8.6,leading=13.1,textColor=C),
 'fine':ParagraphStyle('fine',fontName='Lato',fontSize=8.4,leading=12.7,textColor=M,spaceAfter=6)
}
story=[]
def p(t,kind='body'):return Paragraph(t,styles[kind])
def section(title,n):
 story.append(Spacer(1,9));story.append(p(f'<font color="#9E1B32">{n:02d}</font>   {escape(title.upper())}','heading'))
 story.append(HRFlowable(width='100%',thickness=.65,color=P,spaceAfter=9))
def row(date,text):
 t=Table([[p(escape(date),'date'),p(text)]],colWidths=[93,415],hAlign='LEFT')
 t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),0)]));story.append(t)
def plain(text):story.append(p(text))
def pubentries(entries):
 for i,e in enumerate(entries,1):
  e=re.sub(r'\s*\[(?:source|paper|code|preprint|website)\]','',e,flags=re.I)
  e=e.replace('56– 62.', '56–62.')
  e=e.replace('et al. (including K. Roy)','et al. (including K. Roy)')
  t=Table([[p(f'{i:02d}','num'),p(escape(e),'pub')]],colWidths=[30,478],hAlign='LEFT')
  t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
  story.append(t)
def extract(a,b):
 block=src.split(a,1)[1].split(b,1)[0]
 # handle entries wrapped across lines, strip page headers
 result=[]; cur=[]
 for line in block.splitlines():
  z=line.strip()
  if re.match(r'^\d{2}\.\s',z) and not re.match(r'^62\.\s*\[source\]$',z):
   if cur:result.append(' '.join(cur));cur=[]
   cur=[re.sub(r'^\d{2}\.\s*','',z)]
  elif cur and z and not z.startswith(('October 17','KAUSHIK ROY','PEER-REVIEWED')) and not re.match(r'^\f',z) and not re.match(r'^\s*\d+\s*$',z):
   if 'October 17, 2026' not in z and 'KAUSHIK ROY /' not in z:cur.append(z)
 if cur:result.append(' '.join(cur))
 return [re.sub(r'\s+',' ',e).strip() for e in result if e.strip() and not re.match(r'^\s*\d+\s*$',e)]

# Editorial cover-like header without graphic gimmicks
header=Table([[p('KAUSHIK ROY','name'),p('THE UNIVERSITY OF ALABAMA','position')]],colWidths=[300,208],hAlign='LEFT')
header.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'BOTTOM'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),8)]));story.append(header)
story.append(p('Assistant Professor  /  Department of Computer Science','position'))
story.append(Spacer(1,7))
contacts=Table([[p('3031 Cyber Hall · Tuscaloosa, AL','contact'),p('kroy2@ua.edu  ·  (205) 348-2171','contact')],[p('kauroy1994.github.io/home/','contact'),p('ORCID 0000-0001-6610-7845','contact')]],colWidths=[254,254],hAlign='LEFT')
contacts.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),BG),('LEFTPADDING',(0,0),(-1,-1),13),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story.append(contacts)
story.append(Spacer(1,10));story.append(HRFlowable(width='100%',thickness=2.3,color=C,spaceAfter=10))
section('Academic appointment',1)
row('2025–present','<b>Assistant Professor</b> · Department of Computer Science, The University of Alabama')
section('Education',2)
row('2025','<b>Ph.D., Computer Science and Engineering</b> · University of South Carolina<br/>Dissertation: <i>Process-Grounded Knowledge-Infused Learning and Decision Making</i><br/>Advisor: Amit P. Sheth')
row('2017','<b>M.S., Computer Science</b> · Indiana University Bloomington')
row('2015','<b>B.E., Computer Science</b> · R. V. College of Engineering, Bengaluru')
section('Research interests',3)
plain('Neurosymbolic AI · Knowledge representation · Process-grounded and causal reasoning · Trustworthy agentic systems · Explainable AI · Healthcare AI · Sequential decision-making')
section('Awards and research funding',4)
row('2026','<b>SCoE CORE Equipment Funding</b> · The University of Alabama, College of Engineering · $30,000 collaborative equipment award')
row('2023–2025','<b>NSF EAGER #2335967</b> · Knowledge-Guided Neurosymbolic AI with Guardrails for Safe Virtual Health Assistants · Research contributor')
row('2022–2024','<b>NSF EAGER #2133842</b> · Advancing Neurosymbolic AI with Deep Knowledge-Infused Learning · Research contributor')
section('Publications',5)

def publication_year(entry):
    matches=re.findall(r'\((20\d{2}|19\d{2})\)',entry)
    return int(matches[0]) if matches else 0

def normalize(entry):
    entry=re.sub(r'\s+',' ',entry).strip()
    entry=entry.replace('56– 62.','56–62.')
    return entry

def reverse_chronological(entries):
    return sorted([normalize(e) for e in entries],key=publication_year,reverse=True)

journals=extract('PEER-REVIEWED JOURNAL ARTICLES','PEER-REVIEWED CONFERENCE PAPERS')
conferences=extract('PEER-REVIEWED CONFERENCE PAPERS AND DEMONSTRATIONS','PUBLISHED SYMPOSIUM')
symposia=extract('PUBLISHED SYMPOSIUM AND WORKSHOP PAPERS','BOOK CHAPTERS')
chapters=extract('BOOK CHAPTERS','ACCEPTED WORK')

# Entries are integrated in their publication category; no separate additional-outputs section.
conferences.append('Tripathi, H., Roy, K., Neupane, S., & Rahimi, S. (2026). How Compliant Is Sepsis Treatment? An Expert-Guided Neuro-Symbolic Pipeline for Generating Clinical Compliance Insights. NeSy 2026.')
preprints=['Tripathi, H., Roy, K., Rahimi, S., Neupane, S., & Bozorgzad, S. (2026). From Protocol to Practice: Graded Sepsis Bundle Compliance and Actionable Insights from Real-World ICU Data. medRxiv. DOI: 10.64898/2026.04.23.26351412.']
chapters.append('Roy, K., Gaur, M., Soltani, M., Rawte, V., Kalyan, A., & Sheth, A. (2024). ProKnow: Process Knowledge for Safety Constrained and Explainable Question Generation for Mental Health Diagnostic Assistance in the Age of Large Language Models. Science and Technology – Recent Updates and Future Prospects, Vol. 2.')
# The journal extraction has 16 genuine records; do not parse standalone page numbers as entries.
assert len(journals)==16 and len(chapters)==2
journals=[re.sub(r'\s*\[(?:source|paper|code|preprint|website)\]','',e,flags=re.I) for e in journals]
# Correct publisher author lists for entries that were previously abbreviated.
conferences=[e.replace('Pallagani, V., Roy, K., et al. (2024).','Pallagani, V., Muppasani, B. C., Roy, K., Fabiano, F., Loreggia, A., Murugesan, K., Srivastava, B., Rossi, F., Horesh, L., & Sheth, A. (2024).').replace('Chaudhuri, S. K., Kleppinger, J. W., Nag, R., Roy, K., et al. (2021).','Chaudhuri, S. K., Kleppinger, J. W., Nag, R., Roy, K., Panta, R., Agostinelli, F., Sheth, A., Roy, U. N., James, R. B., & Mandal, K. C. (2021).') for e in conferences]
symposia=[e.replace('Tsakalidis, A., Chim, J., Bilal, I. M., Zirikly, A., Atzil-Slonim, D., Nanni, F., et al. (including K. Roy) (2022).','Tsakalidis, A., Chim, J., Bilal, I. M., Zirikly, A., Atzil-Slonim, D., Nanni, F., Resnik, P., Gaur, M., Roy, K., Inkster, B., Leintz, J., & Liakata, M. (2022).') for e in symposia]

for label,records in [('JOURNAL ARTICLES',journals),('CONFERENCE PAPERS AND DEMONSTRATIONS',conferences),('SYMPOSIUM AND WORKSHOP PAPERS',symposia),('BOOK CHAPTERS',chapters)]:
    story.append(p(label,'sub'))
    pubentries(reverse_chronological(records))
story.append(p('PREPRINTS','sub'))
pubentries(reverse_chronological(preprints))

section('Teaching and mentoring',6)
row('Spring 2027','<b>CS 483/583</b> · Computational Foundations of Machine Learning · The University of Alabama')
row('Fall 2026','<b>CS 696</b> · Graduate Research Mentoring · 3 credits · The University of Alabama')
row('Spring 2026','<b>CS 691</b> · Special Topics: Neurosymbolic Artificial Intelligence · The University of Alabama')
row('Doctoral advising','Ashraf Abdul-Muumin · Department of Computer Science, The University of Alabama')
section('Academic service',7)
story.append(p('EDITORIAL APPOINTMENTS','sub'))
for t in ['Guest Editor · IEEE Internet Computing · <i>Civilizing and Humanizing AI</i>','Guest Editor · Information · <i>Methods for Integrating Information in Data, Language Models, and Knowledge Graphs for Neurosymbolic Learning and Reasoning</i>']:plain(t)
story.append(p('EVENT ORGANIZATION AND PROGRAM COMMITTEES','sub'))
for date,t in [('2026','Program Committee · CNLP4QoL Workshop, IEEE ICHI; TRUSTMORE Workshop, IEEE BigData'),('2025','Program Committee · CLPsych'),('2024','Program Committee · KiL Workshop, ACM KDD; Tutorial Organizer · ISWC'),('2023','Organizing Committee · Knowledge-infused Learning Workshop, ACM KDD; Tutorial Organizer · The Web Conference'),('2020','Program Committee · KiML Workshop, ACM KDD')]:row(date,t)
story.append(p('PEER REVIEW','sub'));plain('Neurosymbolic Artificial Intelligence (2024–2026) · COLING 2025 System Demonstrations')
section('Invited talks and tutorials',8)
for date,t in [('2026','Task-dependent Meta-cognition for General Classes of Problems · University of South Carolina'),('2025','AI in Healthcare · University of South Carolina'),('2024','Healthcare Assistance Challenges-Driven Neurosymbolic AI · Ontolog Summit; Knowledge-infused Neurosymbolic AI for Mental Healthcare · University of Florida; Neurosymbolic Customized and Compact CoPilots · ISWC'),('2023','Causal AI for Web and Health Care · The Web Conference'),('2022','Knowledge-infused Reinforcement Learning · Knowledge Graph Conference'),('2020','Knowledge-infused Statistical Learning for Social Good · PyData Berlin')]:row(date,t)

def decorate(c,doc):
 c.saveState();w,h=letter
 c.setStrokeColor(P);c.setLineWidth(.7);c.line(52,46,w-52,46)
 c.setFont('Lato',7.7);c.setFillColor(M);c.drawString(52,32,'KAUSHIK ROY   /   CURRICULUM VITAE')
 c.setFont('LatoBold',8);c.setFillColor(C);c.drawRightString(w-52,32,f'{doc.page:02d}')
 if doc.page>1:
  c.setFillColor(C);c.rect(52,h-34,26,3,fill=1,stroke=0)
 c.restoreState()
output='files/Kaushik_Roy_CV_2026.pdf'
SimpleDocTemplate(output,pagesize=letter,leftMargin=52,rightMargin=52,topMargin=47,bottomMargin=62,title='Kaushik Roy — Academic Curriculum Vitae',author='Kaushik Roy').build(story,onFirstPage=decorate,onLaterPages=decorate)
print(output,Path(output).stat().st_size)