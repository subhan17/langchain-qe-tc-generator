
import os
import re
from pathlib import Path

DOWNLOADS_DIR = Path.cwd() / "downloads"
DOWNLOADS_DIR.mkdir(exist_ok=True)

def convert_gherkin_to_pytest(gherkin_text):
    # lines = gherkin_text.strip().split("\n")
    # scenario = ""
    # steps = []
    # method_name = "test_generated"
    #
    # for line in lines:
    #     line = line.strip()
    #     if line.startswith("Scenario:"):
    #         scenario = line.replace("Scenario:", "").strip()
    #         method_name = "test_" + re.sub(r'\W+', '_', scenario.lower())
    #     elif line.startswith(("Given", "When", "Then", "And")):
    #         steps.append(line)
    #
    # code_lines = [
    #     "import pytest",
    #     "from playwright.sync_api import Page, expect",
    #     "",
    #     f"@pytest.mark.scenario(\"{scenario}\")",
    #     f"def {method_name}(page: Page):"
    # ]
    #
    # for step in steps:
    #     step = step.strip()
    #     comment = f"    # {step}"
    #     action = "    pass  # TODO: implement"
    #     code_lines.append(comment)
    #     code_lines.append(action)
    #
    # return "\n".join(code_lines)
    lines = gherkin_text.strip().split("\n")
    test_cases = []
    test_func = ""

    for line in lines:
        if line.strip().startswith("Scenario:"):
            if test_func:
                test_cases.append(test_func)  # Save previous
            scenario_name = line.split("Scenario:")[1].strip().replace(" ", "_")
            test_func = f"\ndef test_{scenario_name}():\n"
        elif line.strip().startswith(("Given", "When", "Then", "And", "But")):
            test_func += f"    # {line.strip()}\n"

    if test_func:  # Final one
        test_cases.append(test_func)

    return "\n".join(test_cases)

def save_pytest_file(test_code: str, filename: str = "test_generated.py") -> str:
    path = DOWNLOADS_DIR / filename
    path.write_text(test_code)
    return str(path)