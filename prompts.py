from langchain_core.prompts import ChatPromptTemplate


skill_extraction_prompt = ChatPromptTemplate.from_template(
    """
You are an expert resume analyzer.

Extract technical and soft skills from the given text.

Return ONLY valid JSON in this format:
{{
  "skills": ["skill1", "skill2", "skill3"]
}}

Text:
{text}
"""
)


match_explanation_prompt = ChatPromptTemplate.from_template(
    """
You are an expert ATS resume analyzer.

Explain the resume-job match result.

Final Score: {final_score}/100

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Resume:
{resume_text}

Job Description:
{job_description}

Give output in this format:

Match Summary:
...

Strengths:
- ...

Missing Skills:
- ...

Improvement Suggestions:
- ...
"""
)


career_prediction_prompt = ChatPromptTemplate.from_template(
    """
You are an expert AI career advisor.

Analyze the candidate's resume and predict the best career path.

Use the candidate's:
- Skills
- Projects
- Experience
- Tools
- Education

Choose the best-fit field from these categories:
1. Machine Learning / AI
2. Data Science / Analytics
3. Web Development
4. Backend Development
5. Frontend Development
6. Cloud / DevOps
7. Cybersecurity
8. Mobile App Development
9. UI/UX Design
10. General Software Engineering

Resume:
{resume_text}

Give output in this format:

Best Fit Field:
...

Confidence Level:
High / Medium / Low

Recommended Roles:
- ...

Why This Field Fits:
- ...

Skill Gaps:
- ...

Next Learning Steps:
- ...

Best Project To Build Next:
...
"""
)

rag_prompt = ChatPromptTemplate.from_template(
    """
You are a resume assistant.

Answer the question only using the resume context below.

If the answer is not available in the resume, say:
"Not found in the resume."

Resume Context:
{context}

Question:
{question}
"""
)