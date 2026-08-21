# AI-Assisted Resume → Portfolio Generator

A simple Python application that reads resume text from a file, sends it to the
Gemini API with a controlled prompt, receives structured JSON, and generates a
local HTML portfolio webpage (`portfolio.html`).

## 1. Project Overview

- Input: `resume.txt` (plain text resume)
- Processing: Python cleans the text, sends it to Gemini, and parses the JSON response
- Output: `portfolio.html` (built from `template.html` + `style.css`)

## 2. Setup Instructions

### Step 1 — Clone the repository
```bash
git clone <your-repo-url>
cd resume-portfolio-generator
```

### Step 2 — Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Get a Gemini API key
1. Go to Google AI Studio: https://aistudio.google.com/
2. Create an API key.
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Open `.env` and paste your key:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```
   Never commit `.env` to GitHub — it is already listed in `.gitignore`.

### Step 5 — Add your resume
Replace the contents of `resume.txt` with real (or safe test) resume text.
Do not include passwords, ID numbers, or financial details — see Section 6.

### Step 6 — Run the program
```bash
python main.py
```

### Step 7 — View the result
Open `portfolio.html` in any web browser.

## 3. Workflow

1. Read and clean `resume.txt`.
2. Build a controlled prompt and send the cleaned text to Gemini.
3. Receive the response and parse it as JSON (safely, with fallbacks).
4. Insert the parsed data into `template.html`.
5. Save the final result as `portfolio.html`.
6. Manually verify every generated detail against the original resume.

## 4. Prompt Design

The prompt sent to Gemini (see `build_prompt()` in `main.py`) is written to:
- Include the full cleaned resume text.
- Instruct Gemini to use **only** information present in the resume.
- Explicitly forbid inventing skills, experience, projects, achievements,
  companies, dates, or links.
- Define an exact JSON schema Gemini must follow.
- Require empty strings/lists for missing information instead of guesses.
- Request JSON only — no markdown, no extra commentary.

## 5. Project Structure

```
resume-portfolio-generator/
  main.py            # Main program: read, call Gemini, parse, generate HTML
  resume.txt          # Sample resume input (replace with your own)
  template.html        # HTML template with {{PLACEHOLDER}} tags
  style.css            # Portfolio styling
  requirements.txt     # Python dependencies
  README.md            # This file
  .gitignore
  .env.example
  portfolio.html       # Generated output (created after running main.py)
```

## 6. Responsible AI and Privacy

- Do not include passwords, government ID numbers, financial details, or
  other highly sensitive information in any resume used for testing.
- Never upload the real API key to GitHub or include it in screenshots.
- Gemini is never called from browser-side JavaScript — only from the
  Python backend — so the API key is never exposed to the browser.
- Every generated skill, project, date, company, achievement, and link
  must be checked against the original resume before the portfolio is
  considered final.

## 7. Limitations and Hallucination Risks

- Gemini's output is a **draft**. Even with strict prompt instructions,
  language models can occasionally rephrase or misrepresent details.
- The program validates that the response is valid JSON, but it does
  **not** independently verify that every fact matches the resume —
  this must be done manually (see Testing below).
- If the resume text is ambiguous or poorly formatted, extracted fields
  may be incomplete; missing fields are simply left empty rather than
  guessed.

## 8. Testing

| Test case | Expected behaviour | Result |
|---|---|---|
| Missing `resume.txt` | Clear error, program stops safely | |
| Empty or very short resume | Rejected with a useful message | |
| Valid resume | `portfolio.html` generated successfully | |
| Resume with missing sections | Available sections shown, nothing invented | |
| Missing API key | Configuration error shown | |
| API failure | Handled without crashing | |
| Invalid JSON response | Clear error, program stops safely | |

(Fill in the "Result" column with Pass/Fail and screenshots when testing.)

## 9. AI Usage Log

| AI tool used | Prompt / request given | What it generated | What was changed/corrected |
|---|---|---|---|
| | | | |
| | | | |

## 10. Team

| Name | Role / contribution |
|---|---|
| | |
| | |
| | |
| | |
| | |
