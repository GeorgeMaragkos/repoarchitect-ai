from pathlib import Path

IGNORED_FOLDERS = {"bin", "obj", ".git", ".vs", "node_modules"}


def scan_project_structure(project_path: Path) -> dict:
    file_count = 0
    folder_count = 0

    detected_files = []
    detected_folders = {
        "Controllers": False,
        "Services": False,
        "Repositories": False,
        "Data": False
    }

    is_aspnet_project = False
    uses_dependency_injection = False
    uses_ef_core = False
    controller_dbcontext_violation = False

    for path in project_path.rglob("*"):
        if any(part in IGNORED_FOLDERS for part in path.parts):
            continue

        if path.is_file():
            file_count += 1

            if path.name.endswith(".csproj"):
                detected_files.append(".csproj")
                is_aspnet_project = True

            if path.name == "Program.cs":
                detected_files.append("Program.cs")

                content = path.read_text(encoding="utf-8", errors="ignore")

                if "builder.Services" in content:
                    uses_dependency_injection = True

            if path.suffix == ".cs":
                content = path.read_text(encoding="utf-8", errors="ignore")

                if any(keyword in content for keyword in [
                    "DbContext",
                    "DbSet<",
                    "UseSqlServer",
                    "UseNpgsql",
                    "UseMySql",
                    "UseSqlite"
                ]):
                    uses_ef_core = True

                if "Controllers" in path.parts and "DbContext" in content:
                    controller_dbcontext_violation = True

        elif path.is_dir():
            folder_count += 1

            if path.name in detected_folders:
                detected_folders[path.name] = True

    architecture_warnings = []

    if not detected_folders["Services"]:
        architecture_warnings.append("No service layer detected")

    if not detected_folders["Repositories"]:
        architecture_warnings.append("No repository layer detected")

    if controller_dbcontext_violation:
        architecture_warnings.append("Controllers may access DbContext directly")

    architecture_score = 10

    if not detected_folders["Services"]:
        architecture_score -= 2

    if not detected_folders["Repositories"]:
        architecture_score -= 1

    if not uses_dependency_injection:
        architecture_score -= 2

    if not uses_ef_core:
        architecture_score -= 1

    if controller_dbcontext_violation:
        architecture_score -= 2

    architecture_score = max(0, architecture_score)

    strengths = []

    if uses_dependency_injection:
        strengths.append("Dependency Injection configured")

    if detected_folders["Controllers"]:
        strengths.append("Controllers layer present")

    if uses_ef_core:
        strengths.append("Entity Framework usage detected")

    if not controller_dbcontext_violation:
        strengths.append("Controllers appear clean (no direct DbContext usage)")

    issues = []

    if not detected_folders["Services"]:
        issues.append("Missing service layer")

    if not detected_folders["Repositories"]:
        issues.append("Missing repository layer")

    if not uses_dependency_injection:
        issues.append("Dependency Injection not detected")

    if not uses_ef_core:
        issues.append("Entity Framework not detected")

    if controller_dbcontext_violation:
        issues.append("Controllers may access DbContext directly")

    return {
        "project_path": str(project_path),
        "file_count": file_count,
        "folder_count": folder_count,
        "detected_files": list(set(detected_files)),
        "detected_folders": detected_folders,
        "is_aspnet_project": is_aspnet_project,
        "uses_dependency_injection": uses_dependency_injection,
        "uses_ef_core": uses_ef_core,
        "controller_dbcontext_violation": controller_dbcontext_violation,
        "architecture_warnings": architecture_warnings,
        "architecture_score": architecture_score,
        "strengths": strengths,
        "issues": issues
    }