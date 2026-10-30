#!/usr/bin/env python3
"""Build a printable academic CV from the maintained scholarly archive."""
from pathlib import Path
import re, html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter

OUT=Path("files/Kaushik_Roy_CV_2026.pdf")
OUT.parent.mkdir(exist_ok=True)
s=getSampleStyleSheet()
s.add(ParagraphStyle(name="CVTitle",parent=s["Title"],fontName="Helvetica-Bold",fontSize=21,leading=26,textColor=HexColor("#9E1B32"),spaceAfter=8))
s.add(ParagraphStyle(name="CVHeading",parent=s["Heading2"],fontSize=12,leading=16,textColor=HexColor("#9E1B32"),spaceBefore=15,spaceAfter=6))
s.add(ParagraphStyle(name="CVSub",parent=s["Heading3"],fontSize=10,leading=14,spaceBefore=10,spaceAfter=4))
s.add(ParagraphStyle(name="CVBody",parent=s["BodyText"],fontSize=8.7,leading=12.5,spaceAfter=5))
s.add(ParagraphStyle(name="CVSmall",parent=s["BodyText"],fontSize=8,leading=11,spaceAfter=4,textColor=HexColor("#555555")))
story=[]
def para(text,style="CVBody"):
    text=html.escape(text).replace("&amp;","&amp;")
    story.append(Paragraph(text,s[style]))
def section(text):para(text,"CVHeading")
def bullet(text):para("•  "+text)
para("KAUSHIK ROY","CVTitle")
para("Assistant Professor of Computer Science | The University of Alabama | Tuscaloosa, AL","CVBody")
para("kroy2@ua.edu | https://kauroy1994.github.io/home/ | https://scholar.google.com/citations?user=LpOo_IUAAAAJ","CVSmall")
section("ACADEMIC APPOINTMENTS")
bullet("2025–present: Assistant Professor, Department of Computer Science, The University of Alabama.")
section("EDUCATION")
bullet("Ph.D., Computer Science and Engineering, University of South Carolina, 2025. Dissertation: Process-Grounded Knowledge-Infused Learning and Decision Making. Advisor: Amit Sheth.")
bullet("M.S., Computer Science, Indiana University Bloomington, 2017.")
bullet("B.E., Computer Science, R.V. College of Engineering, 2015.")
section("RESEARCH INTERESTS")
para("Neurosymbolic and knowledge-infused AI; process-grounded learning; causal reasoning; trustworthy and agentic AI; sequential decision-making; healthcare and manufacturing applications.")
section("RESEARCH APPOINTMENTS AND AFFILIATIONS")
for x in ["BRAINS Lab, The University of Alabama — research affiliation.","Artificial Intelligence Institute, University of South Carolina — Graduate Research Assistant, 2020–2025.","Bosch Center for Artificial Intelligence — AI Researcher, summer 2024 and summer 2023.","Samsung Research America — AI Researcher, summer 2022.","The Alan Turing Institute — Visiting Researcher, fall 2021.","StARLinG Lab, University of Texas at Dallas — Research Assistant, 2017–2020."]:bullet(x)
section("RESEARCH SUPPORT AND PROPOSAL ACTIVITY")
for x in ["2026 UA SCoE CORE Equipment Funding ($30,000 multi-investigator award) — listed collaborator; individual allocation not asserted.","Contributor to NSF EAGER #2335967, Knowledge-Guided Neurosymbolic AI with Guardrails for Safe Virtual Health Assistants (PI: Amit Sheth).","Contributor to NSF EAGER #2133842, Advancing Neurosymbolic AI with Deep Knowledge-Infused Learning (PI: Amit Sheth).","2026: Research proposal development in trustworthy neurosymbolic AI, manufacturing datasets, and causal decision support; submissions are not represented as awards."]:bullet(x)
section("PEER-REVIEWED PUBLICATIONS AND SCHOLARLY OUTPUTS")
para("The following is a consolidated record of newer publications and the bibliography from the author's earlier public academic CV. Publication metadata should be checked against publisher records for formal applications.","CVSmall")
for x in ["Roy, K., et al. (2026). Exploring the Potential of Large Language Models for Assisting with Mental Health Diagnostic Assessments. ACM Transactions on Computing for Healthcare.","Ramnani, S., Roy, K., and Sheth, A. (2026). MATRIX: Mental heAlth diagnostics Through Real time Intelligent unified X-AI attribution reasoning. Frontiers in Digital Health.","Chattopadhyay, A., Dandekar, R., and Roy, K. (2026). Metatuning: An Empirical Study of Judge-Guided Prompt Refinement and Its Boundary Conditions. Neurosymbolic Artificial Intelligence.","Tripathi, H., Roy, K., Neupane, S., and Rahimi, S. (2026). How Compliant is Sepsis Treatment? An Expert-Guided Neuro-symbolic Pipeline for Generating Clinical Compliance Insights. NeSy 2026.","Garimella, R., Roy, K., et al. (2026). In-Situ Eval: A Modular Framework for Custom and Real-Time RAG Benchmarking. AAAI Demonstration Track."]:bullet(x)
archive=Path("_pages/markdown.md").read_text(encoding="utf8")
lines=archive.splitlines()
active=False
for line in lines:
    if line.startswith("## 📚 Publications"):active=True;continue
    if line.startswith("## 📹 Tutorials and Talks"):break
    if not active:continue
    if line.startswith("### "):
        section(re.sub(r"[^A-Za-z0-9 ,&/()-]","",line[4:]).strip().upper())
    elif re.match(r"^\d+\.\s",line):
        cleaned=re.sub(r"\[\[([^]]+)\]\]\([^)]*\)",r" [\1]",line)
        cleaned=re.sub(r"\[([^]]+)\]\([^)]*\)",r"\1",cleaned)
        cleaned=re.sub(r"[*_`]+","",cleaned)
        cleaned=re.sub(r"^\d+\.\s*","",cleaned)
        bullet(cleaned[:850])
section("SELECTED TALKS AND TUTORIALS")
for x in ["2024: Neurosymbolic Customized and Compact CoPilots, International Semantic Web Conference tutorial.","2024: Healthcare Assistance Challenges-Driven Neurosymbolic AI, Ontolog Summit invited talk.","2024: Knowledge-infused Neurosymbolic AI for Mental Healthcare, University of Florida ICCC.","2023: Causal AI for Web and Health Care, ACM Web Conference tutorial.","2022: Knowledge-infused Reinforcement Learning, Knowledge Graph Conference tutorial.","2020: Knowledge-infused Statistical Learning for Social Good Applications, PyData Berlin."]:bullet(x)
section("SELECTED PROFESSIONAL SERVICE")
for x in ["Guest Editor, IEEE Internet Computing special issue on Civilizing and Humanizing AI.","Guest Editor, Information special issue on information integration, language models, and knowledge graphs.","Program Committee, AAAI 2024 Fall Symposium on Large Language Models for Knowledge Graph and Ontology Engineering.","Organizing Committee, KiL 2023 at KDD.","Organizing Committee, Collaborative Assistants for the Society (CASY), 2022."]:bullet(x)
section("MENTORING AND TEACHING")
bullet("Doctoral student supervision: Ashraf Abdul-Muumin, University of Alabama.")
bullet("Curriculum development: Computational Foundations of Machine Learning (CS 483/583); AI and MLOps topics.")
section("MEDIA AND OUTREACH")
bullet("AI in the Family (2025) — film listed on IMDb, https://www.imdb.com/title/tt38192436/ (specific credit should be verified).")
bullet("Recorded public talks and tutorials on YouTube; see faculty website's Beyond Research page.")
para("Updated October 2026 | Generated from the author's academic website and archived public CV. This is a faculty-website CV, not a certified grant or immigration dossier.","CVSmall")
def page(canvas,doc):
    canvas.setStrokeColor(HexColor("#9E1B32"));canvas.line(44,42,568,42)
    canvas.setFont("Helvetica",8);canvas.setFillColor(HexColor("#666666"))
    canvas.drawString(44,30,"KAUSHIK ROY | ACADEMIC CURRICULUM VITAE")
    canvas.drawRightString(568,30,str(doc.page))
SimpleDocTemplate(str(OUT),pagesize=letter,rightMargin=44,leftMargin=44,topMargin=44,bottomMargin=57,title="Kaushik Roy - Academic Curriculum Vitae").build(story,onFirstPage=page,onLaterPages=page)
print("Wrote",OUT)
