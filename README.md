# RepoArchitect AI

RepoArchitect AI is an AI-assisted architecture reviewer for ASP.NET Core repositories.  
It analyzes a codebase structure, detects architectural patterns, and produces a quality score with strengths and issues.

## 🚀 Features (Current MVP)

- Upload ASP.NET Core project (.zip)
- Automatic repository extraction
- Architecture structure detection
- Dependency Injection detection
- Entity Framework detection
- Controller → DbContext anti-pattern detection
- Architecture warnings
- Architecture quality score (0–10)
- Strengths and issues analysis

## 🧠 Example Output

```json
{
  "architecture_score": 7,
  "strengths": [
    "Dependency Injection configured",
    "Controllers layer present"
  ],
  "issues": [
    "Missing service layer",
    "Missing repository layer"
  ]
}
