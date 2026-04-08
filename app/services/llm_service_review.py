def generate_ai_review(scan_result: dict) -> dict:
    score = scan_result.get("architecture_score")
    strengths = scan_result.get("strengths", [])
    issues = scan_result.get("issues", [])

    recommendations = []

    if "Missing service layer" in issues:
        recommendations.append("Introduce a service layer to encapsulate business logic.")

    if "Missing repository layer" in issues:
        recommendations.append("Implement a repository pattern for data access abstraction.")

    if "Controllers may access DbContext directly" in issues:
        recommendations.append("Refactor controllers to use services instead of DbContext.")

    if "Dependency Injection not detected" in issues:
        recommendations.append("Configure dependency injection.")

    if "Entity Framework not detected" in issues:
        recommendations.append("Consider using Entity Framework or another ORM.")

    # Risk level
    if score >= 8:
        risk = "Low"
    elif score >= 5:
        risk = "Medium"
    else:
        risk = "High"

    # Summary
    if score >= 8:
        summary = "The project follows strong architectural principles with good separation of concerns."
    elif score >= 5:
        summary = "The project has a reasonable structure but lacks some architectural best practices."
    else:
        summary = "The project has architectural weaknesses that could impact maintainability."

    return {
        "summary": summary,
        "recommendations": recommendations,
        "risk_level": risk,
        "strengths": strengths,
        "issues": issues
    }