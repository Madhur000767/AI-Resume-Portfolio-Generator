import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


with open("resume.txt", "r") as file:
    resume_text = file.read()


if len(resume_text.strip()) < 20:
    print("Resume is empty or too short")
    exit()


print("Resume loaded successfully!")

prompt = f"""
Convert this resume into JSON format.

Resume:
{resume_text}

Return only JSON.

Important:
- projects should be list of objects with title key
- education should be list of objects with degree and institution
- contact should include email, phone, github, linkedin

JSON format:

{{
"name":"",
"headline":"",
"summary":"",
"skills":[],
"education":[],
"experience":[],
"projects":[],
"achievements":[],
"contact":{{}}
}}
"""

print("Sending resume to Gemini...")

result = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

response = result.text

print("Gemini Response:")
print(response)

import json

# Gemini response ko JSON mein convert karo
resume_data = json.loads(response)

# New data ko resume_data.json mein save karo
with open("resume_data.json", "w", encoding="utf-8") as f:
    json.dump(resume_data, f, indent=4, ensure_ascii=False)

print("✓ resume_data.json updated successfully.")


# Generate portfolio HTML from resume data

html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{resume_data["name"]} - Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

    <h1>{resume_data["name"]}</h1>
    <h2>{resume_data.get("headline", "")}</h2>

    <h3>Professional Summary</h3>
    <p>{resume_data.get("summary", "")}</p>

    <h3>Skills</h3>
    <p>{", ".join(resume_data.get("skills", []))}</p>

    <h3>Education</h3>
    <p>
"""

for edu in resume_data.get("education", []):
    html += f"""
        Degree: {edu.get("degree", "")}<br>
        Institution: {edu.get("institution", "")}<br>
        Year: {edu.get("year", "")}<br>
        Score: {edu.get("score", "")}<br><br>
    """

html += """
    </p>

    <h3>Projects</h3>
    <p>
"""

for project in resume_data.get("projects", []):
    html += f"""
        <b>{project.get("title", "")}</b><br>
        {project.get("description", "")}<br>
        Technologies: {", ".join(project.get("technologies", []))}<br><br>
    """

html += """
    </p>

    <h3>Achievements</h3>
    <p>
"""

for achievement in resume_data.get("achievements", []):
    html += f"{achievement}<br>"

html += f"""
    </p>

    <h3>Contact</h3>
    <p>
        Email: {resume_data["contact"].get("email", "")}<br>
        Phone: {resume_data["contact"].get("phone", "")}<br>
        GitHub: {resume_data["contact"].get("github", "")}<br>
        LinkedIn: {resume_data["contact"].get("linkedin", "")}
    </p>

</body>
</html>
"""

with open("portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✓ portfolio.html generated successfully.")