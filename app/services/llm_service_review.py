def generate_ai_review(scan_result: dict) -> str:
    score = scan_result.get("architecture_score")
    strengths = scan_result.get("strengths", [])
    issues = scan_result.get("issues", [])

    review = f"""
Architecture Score: {score}/10

Strengths:
- {"\n- ".join(strengths) if strengths else "None detected"}

Issues:
- {"\n- ".join(issues) if issues else "No major issues"}

Summary:
"""

    if score >= 8:
        review += "The project follows strong architectural practices and is well-structured."
    elif score >= 5:
        review += "The project has a decent structure but could benefit from improvements."
    else:
        review += "The project has architectural issues that should be addressed."

    return review.strip()