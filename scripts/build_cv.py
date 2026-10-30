#!/usr/bin/env python3
"""Faculty academic CV, October 2026. Rebuilt as a full-length scholarly record.
Current appointments/publications are curated explicitly; pre-2025 bibliography,
tutorials and teaching are reconciled with the author's historical public website.
No prior PDF is read or copied.
"""
from pathlib import Path
import re,html
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,KeepTogether,HRFlowable,KeepInFrame
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from xml.sax.saxutils import escape
OUT=Path("files/Kaushik_Roy_CV_2026.pdf");OUT.parent.mkdir(exist_ok=True)
st=getSampleStyleSheet()
CRIMSON=HexColor("#9E1B32")
INK=HexColor("#20242D")
MUTED=HexColor("#5C6470")
st.add(ParagraphStyle(name="CVName",fontName="Times-Bold",fontSize=27,leading=32,spaceAfter=5,textColor=CRIMSON))
st.add(ParagraphStyle(name="CVHeading",fontName="Helvetica-Bold",fontSize=10.6,leading=14,spaceBefore=19,spaceAfter=8,textColor=CRIMSON,keepWithNext=True,tracking=0.8))
st.add(ParagraphStyle(name="CVSubheading",fontName="Helvetica-Bold",fontSize=9.6,leading=13,spaceBefore=12,spaceAfter=6,textColor=INK,keepWithNext=True))
st.add(ParagraphStyle(name="CVBody",fontName="Helvetica",fontSize=9.1,leading=13.6,spaceAfter=6.5,textColor=INK))
st.add(ParagraphStyle(name="CVFine",fontName="Helvetica",fontSize=8.4,leading=12,spaceAfter=5,textColor=MUTED))
st.add(ParagraphStyle(name="CVEntry",parent=st["CVBody"],leftIndent=12,firstLineIndent=-11,spaceAfter=6.5))
story=[]
def p(t,style="CVBody"):
 story.append(Paragraph(escape(t),st[style]))
def section(t):
 story.append(Spacer(1,5))
 story.append(Paragraph(escape(t.upper()),st["CVHeading"]))
 story.append(HRFlowable(width="100%",thickness=.7,color=HexColor("#DCC6CD"),spaceBefore=0,spaceAfter=10))
def sub(t):p(t,"CVSubheading")
def rows(v):
 for x in v:p("•  "+x,"CVEntry")
p("KAUSHIK ROY","CVName")
p("Ph.D.  |  Assistant Professor, Department of Computer Science  |  The University of Alabama")
p("3031 Cyber Hall, Tuscaloosa, Alabama   •   kroy2@ua.edu   •   (205) 348-2171","CVFine")
p("kauroy1994.github.io/home/   •   ORCID: 0000-0001-6610-7845   •   Google Scholar: LpOo_IUAAAAJ","CVFine")
story.append(HRFlowable(width="100%",thickness=2.2,color=CRIMSON,spaceBefore=10,spaceAfter=15))
section("Research profile")
p("Research on knowledge-infused and neurosymbolic AI that combines neural representations with declarative, procedural and causal structure. Current interests include trustworthy agentic systems, interpretable sequential decisions, foundation models, process-aware reasoning, evaluation, and high-stakes applications in healthcare and manufacturing.")
section("Academic appointments and affiliations")
rows(["2025–present | Assistant Professor, Department of Computer Science, The University of Alabama, Tuscaloosa.","Research affiliation | BRAINS Laboratory, The University of Alabama.","2020–2025 | Graduate Research Assistant, Artificial Intelligence Institute, University of South Carolina."])
section("Education")
rows(["2025 | Ph.D., Computer Science and Engineering, University of South Carolina. Dissertation: Process-Grounded Knowledge-Infused Learning and Decision Making. Advisor: Amit P. Sheth.","2017 | M.S., Computer Science, Indiana University Bloomington. Artificial Intelligence and Machine Learning.","2015 | B.E., Computer Science, R.V. College of Engineering, Bengaluru.","2017–2020 | Doctoral study, University of Texas at Dallas; transferred to University of South Carolina."])
section("Industry and visiting research appointments")
rows(["Summer 2024 | Artificial Intelligence Researcher, Bosch Center for Artificial Intelligence: cognitive-architecture-inspired neurosymbolic methods.","Summer 2023 | Artificial Intelligence Researcher, Bosch Center for Artificial Intelligence: spatiotemporal and causal reasoning.","Summer 2022 | Artificial Intelligence Researcher, Samsung Research America: personalized dialogue systems.","Fall 2021 | Visiting Researcher, The Alan Turing Institute: longitudinal language and moments-of-change research.","2017–2020 | Research Assistant, StARLinG Lab, University of Texas at Dallas: relational learning and sequential decision-making."])
section("Research program and mentoring")
rows(["Neurosymbolic reasoning and knowledge integration: foundation models with explicit process constraints, domain semantics and causal representations.","Auditable agentic AI: evidence-grounded tool use, state tracking, verification and decision traces.","Healthcare AI: mental-health diagnostic support and expert-guided clinical protocol compliance.","Manufacturing AI: process-grounded datasets, anomaly reasoning and human-centered explanations.","Ph.D. student supervised: Ashraf Abdul-Muumin, University of Alabama."])
section("Awards and research support")
rows(["2026 | SCoE CORE Equipment Funding, College of Engineering, The University of Alabama ($30,000); collaborative award with Hongsheng He and Bineet Ghosh.","2026 | University of Alabama Entrepreneurship Institute faculty/staff innovation recognition for an accessible learning platform.","2023–2025 | Research contributions to NSF EAGER #2335967, Knowledge-Guided Neurosymbolic AI with Guardrails for Safe Virtual Health Assistants (PI: Amit Sheth).","2022–2024 | Research contributions associated with NSF EAGER #2133842, Advancing Neurosymbolic AI with Deep Knowledge-Infused Learning (PI: Amit Sheth)."])
section("Peer-reviewed journal publications — 2026")
rows(["Roy, K., Surana, H., Eswaramoorthi, D., Zi, Y., Palit, V., Garimella, R., and Sheth, A. (2026). Exploring the Potential of Large Language Models for Assisting with Mental Health Diagnostic Assessments. ACM Transactions on Computing for Healthcare, 7(3), Article 58. doi:10.1145/3805697.","Ramnani, S., Roy, K., and Sheth, A. (2026). MATRIX: Mental heAlth diagnostics Through Real time Intelligent unified X-AI attribution reasoning. Frontiers in Digital Health, 7, 1621271.","Chattopadhyay, A., Dandekar, R., and Roy, K. (2026). Metatuning: An Empirical Study of Judge-Guided Prompt Refinement and Its Boundary Conditions. Neurosymbolic Artificial Intelligence."])
section("Peer-reviewed journal publications — 2025")
rows(["Zi, Y., Roy, K., and Sheth, A. (2025). Cognitive Neurosymbolic Artificial Intelligence for Complex Decision-Making: Integrating Foundation Models, Cognitive Architectures, and Knowledge. IEEE Intelligent Systems. doi:10.1109/MIS.2025.3561487.","Sheth, A., Roy, K., Venkataramanan, R., Nadimuthu, V., and Shyalika, C. (2025). Composite AI With Custom, Compact, Neurosymbolic Models: The Emergent Enterprise Artificial Intelligence Paradigm. IEEE Internet Computing, 29(2), 37–49.","Sheth, A., Khandelwal, V., Roy, K., Pallagani, V., and Chakraborty, M. (2025). NeuroSymbolic Knowledge-Grounded Planning and Reasoning in Artificial Intelligence Systems. IEEE Intelligent Systems.","Venkataramanan, R., et al., including Roy, K. (2024; online January 2025). Constructing a Metadata Knowledge Graph as an Atlas for Demystifying AI Pipeline Optimization. Frontiers in Big Data, 7, 1476506."])
section("Peer-reviewed journal publications — 2024 and earlier")
rows(["Sheth, A., Roy, K., Purohit, H., and Das, A. (2024). Civilizing and Humanizing Artificial Intelligence in the Age of Large Language Models. IEEE Internet Computing, 28(5).","Roy, K. (2024). Healthcare Assistance Challenges-Driven Neurosymbolic AI. Biomedical Journal of Scientific and Technical Research, 58(2).","Shyalika, C., Roy, K., et al. (2024). RI2AP: Robust and Interpretable 2D Anomaly Prediction in Assembly Pipelines. Sensors, 24(10), Article 3244. doi:10.3390/s24103244.","Sheth, A., and Roy, K. (2024). Neurosymbolic Value-Inspired Artificial Intelligence (Why, What, and How). IEEE Intelligent Systems, 39(1).","Sheth, A., Roy, K., and Gaur, M. (2023). Neurosymbolic Artificial Intelligence (Why, What, and How). IEEE Intelligent Systems, 38(3).","Roy, K., Gaur, M., Soltani, M., Rawte, V., Kalyan, A., and Sheth, A. (2023). ProKnow: Process Knowledge for Safety Constrained and Explainable Question Generation for Mental Health Diagnostic Assistance. Frontiers in Big Data, 5, Article 1056728. doi:10.3389/fdata.2022.1056728.","Sheth, A., Gaur, M., Roy, K., Venkataraman, R., and Khandelwal, V. (2022). Process Knowledge-Infused AI: Toward User-Level Explainability, Interpretability, and Safety. IEEE Internet Computing, 26(5).","Sheth, A., Gaur, M., Roy, K., and Faldu, K. (2021). Knowledge-intensive Language Understanding for Explainable AI. IEEE Internet Computing, 25(5)."])
section("Other published research proceedings")
rows(["Chaudhuri, S. K., Kleppinger, J. W., Nag, R., Roy, K., et al. (2021). A CdZnTeSe Gamma Spectrometer Trained by Deep Convolutional Neural Network for Radioisotope Identification. Hard X-Ray, Gamma-Ray, and Neutron Detector Physics XXIII, SPIE Proceedings, Vol. 11838."])
section("Peer-reviewed conferences and demonstrations — 2026–2025")
rows(["Tripathi, H., Roy, K., Neupane, S., and Rahimi, S. (2026). How Compliant is Sepsis Treatment? An Expert-Guided Neuro-symbolic Pipeline for Generating Clinical Compliance Insights. NeSy 2026 (accepted conference presentation); arXiv:2608.13617.","Garimella, R., Roy, K., Shyalika, C., and Sheth, A. (2026). In-Situ Eval: A Modular Framework for Custom and Real-Time RAG Benchmarking. AAAI 2026 Demonstration Track. doi:10.1609/aaai.v40i48.42348.","Chattopadhyay, A., Dandekar, R., and Roy, K. (2025). Learning and Reasoning with Model-Grounded Symbolic Artificial Intelligence Systems. NeSy 2025, PMLR 284:957–976."])
section("Additional conference and workshop publications")
rows(["Roy, K., Khandelwal, V., Vera, V., Surana, H., Heckman, H., and Sheth, A. (2024). GEAR-Up: Generative AI and External Knowledge-Based Retrieval: Upgrading Scholarly Article Searches for Systematic Reviews. Proceedings of the AAAI Conference on Artificial Intelligence, 38(21), 23823–23825. Demonstration Track. doi:10.1609/aaai.v38i21.30577.","Gupta, S., Agarwal, A., Gaur, M., Roy, K., Narayanan, V., Kumaraguru, P., and Sheth, A. (2022). Learning to Automate Follow-up Question Generation using Process Knowledge for Depression Triage on Reddit Posts. Proceedings of the Eighth Workshop on Computational Linguistics and Clinical Psychology (CLPsych), 137–147. Association for Computational Linguistics. doi:10.18653/v1/2022.clpsych-1.12."])
section("Additional symposium and workshop publications")
rows(["Roy, K., Oltramari, A., Zi, Y., Shyalika, C., Narayanan, V., and Sheth, A. (2024). Causal Event Graph-Guided Language-based Spatiotemporal Question Answering. Proceedings of the AAAI Symposium Series, 3(1), 227–233. doi:10.1609/aaaiss.v3i1.31204.","Roy, K., Zi, Y., Gaur, M., Malekar, J., Zhang, Q., Narayanan, V., and Sheth, A. (2023). Process Knowledge-Infused Learning for Clinician-Friendly Explanations. Proceedings of the AAAI Symposium Series, 1(1), 154–160. doi:10.1609/aaaiss.v1i1.27494.","Tsakalidis, A., Chim, J., Bilal, I. M., et al., including Roy, K. (2022). Overview of the CLPsych 2022 Shared Task: Capturing Moments of Change in Longitudinal User Posts. Proceedings of the Eighth Workshop on Computational Linguistics and Clinical Psychology, 184–198. Association for Computational Linguistics. doi:10.18653/v1/2022.clpsych-1.16."])
section("Published book chapters")
rows(["Roy, K., Wu, S., and Oltramari, A. (2025). Enhancing Foundation Model-Based Reasoning with Neuro-Symbolic Cognitive Methods. In Handbook on Neurosymbolic AI and Knowledge Graphs, IOS Press, pp. 712–739. doi:10.3233/FAIA250228.","Roy, K., Gaur, M., Soltani, M., Rawte, V., Kalyan, A., and Sheth, A. (2024). ProKnow: Process Knowledge for Safety Constrained and Explainable Question Generation for Mental Health Diagnostic Assistance in the Age of Large Language Models. In Science and Technology – Recent Updates and Future Prospects, Vol. 2."])
section("Conference, symposium and workshop proceedings — 2024 and earlier")

raw=Path("_pages/markdown.md").read_text(encoding="utf-8")
start=raw.index("## 📚 Publications")
end=raw.index("## 📹 Tutorials and Talks")
part=raw[start:end]
category=None
buf=[]
def clean(x):
 # Strip Markdown link markup entirely rather than printing inert [paper],
 # [code], [video], [website], or similar pseudo-links in the PDF.
 x=re.sub(r"\[\[([^]]+)\]\]\([^)]*\)", "", x)
 x=re.sub(r"\[([^]]+)\]\([^)]*\)", "", x)
 x=re.sub(r"\[(?:paper|code|video|website|slides|preprint|source|chapter preprint)\]", "", x, flags=re.I)
 x=re.sub(r"\*\*|\*|_", "", x)
 x=re.sub(r"\s+", " ", x)
 return x.strip()

def flush():
 global buf
 if buf:
  txt=clean(" ".join(buf))
  txt=re.sub(r"^\d+\.\s*","",txt)
  if not any(k in txt.lower() for k in ("gear-up: generative ai","learning to automate follow-up question generation","causal event graph-guided language-based spatiotemporal","process knowledge-infused learning for clinician-friendly","overview of the clpsych 2022 shared task")):
   p("•  "+txt)
  buf=[]
for ln in part.splitlines():
 if ln.startswith("### "):
  flush(); category=clean(ln[4:]);
  if "Conference Publications" in category:sub("Conferences and demonstrations")
  elif "Symposium and Workshop Publications" in category:sub("Symposium and workshop proceedings")
 elif re.match(r"^\d+\.\s",ln):
  flush();buf=[ln] if any(x in (category or "") for x in ("Conference Publications","Symposium and Workshop Publications")) else []
 elif buf and ln.strip():
  buf.append(ln)
flush()
section("Invited talks and scholarly tutorials")
rows(["2024 | Neurosymbolic Customized and Compact CoPilots, International Semantic Web Conference.","2024 | Healthcare Assistance Challenges-Driven Neurosymbolic AI, Ontolog Summit.","2024 | Knowledge-infused Neurosymbolic Artificial Intelligence for Mental Healthcare, University of Florida ICCC.","2023 | Causal AI for Web and Health Care, ACM Web Conference.","2022 | Knowledge-infused Reinforcement Learning, Knowledge Graph Conference.","2022 | Neuro-symbolic AI for Mental Healthcare, AI-ML Systems.","2021 | Knowledge-infused NLU for Public Health, IJCAI workshop.","2021 | Knowledge In-Wisdom Out, ICWSM.","2020 | Knowledge-infused Statistical Learning for Social Good, PyData Berlin."])
section("Selected guest lectures")
rows(["2024 | Language Models: BERT, Mamba, and GPT, University of South Carolina CSCE 771.","2024 | AI in Healthcare, University of South Carolina CSCE 791.","2024 | Knowledge Graphs for Enhanced Semantics, UMBC CMSC 691.","2024 | Constrained Optimization, University of South Carolina CSCE 590.","2023 | Transformers and Liquid Time Networks, University of South Carolina CSCE 790.","2023 | Recurrent Neural Networks and Neural ODEs, University of South Carolina CSCE 790.","2023 | Automatic Differentiation and Optimization Strategies, UMBC CMSC 478.","2022 | Interpretable Machine Learning and Hoeffding's Inequality, UMBC CMSC 478."])
section("Teaching and graduate mentoring")
rows(["University of Alabama: computational foundations of machine learning, CS 483/583; course and curriculum preparation.","Foundations of AI and MLOps: curriculum development spanning classical ML, LLMs, retrieval, reproducibility and monitoring.","Graduate mentoring in neurosymbolic AI, causal reasoning, and evidence-grounded AI systems."])
section("Editorial and academic service")
rows(["Guest Editor, IEEE Internet Computing special issue on Civilizing and Humanizing AI.","Guest Editor, Information special issue on Methods for Integrating Information in Data, Language Models, and Knowledge Graphs.","Program Committee, AAAI 2024 Fall Symposium on LLMs for Knowledge Graph and Ontology Engineering.","Organizing Committee, KiL 2023 at KDD.","Organizing Committee, Collaborative Assistants for Society (CASY) 2022.","Hackathon Committee, Knowledge Graph and Semantic Web Conference 2021."])
section("Media, outreach, and public communication")
rows(["AI in the Family (2025), IMDb film listing: imdb.com/title/tt38192436/.","Personal YouTube channel: youtube.com/@kaushikroy4041.","Recorded research talks and tutorials on healthcare AI, social-good ML, and neurosymbolic reasoning."])

def foot(c,d):
 w,h=letter
 c.saveState()
 c.setStrokeColor(HexColor("#E1D4D8"))
 c.setLineWidth(.7)
 c.line(46,49,w-46,49)
 c.setFont("Helvetica",7.8)
 c.setFillColor(MUTED)
 c.drawString(46,35,"KAUSHIK ROY  /  ACADEMIC CURRICULUM VITAE")
 c.drawRightString(w-46,35,f"{d.page:02d}")
 if d.page>1:
  c.setFillColor(CRIMSON)
  c.rect(46,h-37,30,3,fill=1,stroke=0)
 c.restoreState()
SimpleDocTemplate(str(OUT),pagesize=letter,leftMargin=51,rightMargin=51,topMargin=55,bottomMargin=67,title="Kaushik Roy | Academic Curriculum Vitae",author="Kaushik Roy").build(story,onFirstPage=foot,onLaterPages=foot)
print("CV built",OUT,OUT.stat().st_size)
