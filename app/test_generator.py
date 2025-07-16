
import os
import re
from pathlib import Path

DOWNLOADS_DIR = Path.cwd() / "downloads"
DOWNLOADS_DIR.mkdir(exist_ok=True)

def convert_gherkin_to_pytest(gherkin_text):
    lines = gherkin_text.strip().split("\n")
    scenario = ""
    steps = []
    method_name = "test_generated"

    for line in lines:
        line = line.strip()
        if line.startswith("Scenario:"):
            scenario = line.replace("Scenario:", "").strip()
            method_name = "test_" + re.sub(r'\W+', '_', scenario.lower())
        elif line.startswith(("Given", "When", "Then", "And")):
            steps.append(line)

    code_lines = [
        "import pytest",
        "from playwright.sync_api import Page, expect",
        "",
        f"@pytest.mark.scenario(\"{scenario}\")",
        f"def {method_name}(page: Page):"
    ]

    for step in steps:
        step = step.strip()
        comment = f"    # {step}"
        action = "    pass  # TODO: implement"
        code_lines.append(comment)
        code_lines.append(action)

    return "\n".join(code_lines)


def save_pytest_file(test_code: str, filename: str = "test_generated.py") -> str:
    path = DOWNLOADS_DIR / filename
    path.write_text(test_code)
    return str(path)