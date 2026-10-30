#!/usr/bin/env python3
"""Rebuild a new CV from current public faculty-site publication records, not old CVs."""
from pathlib import Path
from html.parser import HTMLParser
from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from xml.sax.saxutils import escape
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.records=[];self.in_item=False;self.current=""
 def handle_starttag(self,tag,attrs):
  if tag=="div" and ("class","pub-item") in attrs:self.in_item=True;self.current=""
 def handle_data(self,data):
  if self.in_item:self.current+=data+" "
 def handle_endtag(self,tag):
  if tag=="div" and self.in_item:
   self.records.append(" ".join(self.current.split()));self.in_item=False
source=Path("_pages/publications.md").read_text(encoding="utf-8")
parser=Parse();parser.feed(source)
s=getSampleStyleSheet();s.add(ParagraphStyle(name="CVHeader",parent=s["Heading2"],textColor=HexColor("#9e1b32"),spaceBefore=16))
story=[]
def line(t):story.append(Paragraph(escape(t),s["BodyText"]))
def head(t):story.append(Paragraph(escape(t),s["CVHeader"]))
story.append(Paragraph("KAUSHIK ROY",s["Title"]))
line("Assistant Professor of Computer Science | The University of Alabama | kroy2@ua.edu | 3031 Cyber Hall")
head("Research")
line("Neurosymbolic AI; process-grounded learning; causal reasoning; trustworthy agents; explainable decisions; healthcare and manufacturing.")
head("Appointments and affiliations")
for t in ["2025–present: Assistant Professor, University of Alabama","Research affiliate: BRAINS Lab, University of Alabama","2020–2025: Graduate Research Assistant, Artificial Intelligence Institute, University of South Carolina"]:line(t)
head("Education")
for t in ["Ph.D. Computer Science and Engineering, University of South Carolina, 2025; advisor Amit Sheth; dissertation Process-Grounded Knowledge-Infused Learning and Decision Making","M.S. Computer Science, Indiana University Bloomington, 2017","B.E. Computer Science, R.V. College of Engineering, 2015"]:line(t)
head("Research experience")
for t in ["Bosch Center for Artificial Intelligence: summer 2023 and summer 2024","Samsung Research America: summer 2022","The Alan Turing Institute: fall 2021","StARLinG Lab, University of Texas at Dallas: 2017–2020"]:line(t)
head("Research support and proposal activity")
for t in ["2026: collaborator, UA SCoE CORE Equipment Funding, multi-investigator award ($30,000 total; no individual allocation claimed)","Contributions to NSF EAGER #2335967 and #2133842 (PI Amit Sheth)","2026: proposals and concepts in trustworthy AI, manufacturing data and causal decision support; not claimed as awarded funding"]:line(t)
head("Publications — current verified website bibliography")
for item in parser.records:line("• "+item)
head("Additional research outputs")
for t in ["Ramnani, Roy and Sheth (2026). MATRIX: Mental heAlth diagnostics Through Real time Intelligent unified X-AI attribution reasoning. Frontiers in Digital Health.","Pallagani, Roy et al. (2024). On the Prospects of Incorporating Large Language Models in Automated Planning and Scheduling. ICAPS.","Roy, Khandelwal et al. (2024). GEAR-Up: Generative AI and External Knowledge-Based Retrieval. AAAI.","Roy, Gaur et al. (2023). Proknow: Process Knowledge for Safety Constrained and Explainable Question Generation. Frontiers in Big Data.","Roy, Zhang, Gaur and Sheth (2021). Knowledge-infused Policy Gradients with Upper Confidence Bound for Relational Bandits. ECML PKDD."]:line("• "+t)
head("Selected invited talks and service")
for t in ["ISWC 2024 tutorial: Neurosymbolic Customized and Compact CoPilots","Ontolog Summit 2024: Healthcare Assistance Challenges-Driven Neurosymbolic AI","University of Florida ICCC 2024 invited talk","Guest Editor: IEEE Internet Computing and Information special issues","Program Committee: AAAI 2024 Fall Symposium on LLMs for KG and Ontology Engineering","Organizing Committee: KiL 2023 at KDD; CASY 2022"]:line("• "+t)
head("Mentoring and outreach")
line("Ph.D. student: Ashraf Abdul-Muumin. Curriculum development: CS 483/583 Computational Foundations of Machine Learning.")
line("Film: AI in the Family (2025), IMDb tt38192436. Personal YouTube: youtube.com/@kaushikroy4041.")
head("Verification")
line("UA directory: eng.ua.edu/eng-directory/dr-kaushik-roy/ | ORCID: 0000-0001-6610-7845 | Scholar Commons dissertation 8563")
line("Prepared October 2026 from newly curated public records and current publication entries; this is a selected CV.")
out=Path("files/Kaushik_Roy_CV_2026.pdf");out.parent.mkdir(exist_ok=True)
SimpleDocTemplate(str(out),pagesize=letter).build(story)
print("Built",out,len(parser.records))
