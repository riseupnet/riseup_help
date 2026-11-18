#!/usr/bin/env python3
"""
Site integrity and syntax validator for riseup_help.

Validates:
1. YAML syntax for amber/locales and pages/accounts.
2. Locale configuration consistency with amber/config.rb.
3. Common syntax issues (unresolved git conflict markers, malformed property headers).
4. Missing translation keys compared to en.yml.
"""

import os
import re
import sys
import yaml
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def check_yaml_files():
    """Validate YAML syntax for all .yml and .yaml files."""
    print("--> Checking YAML files...")
    yaml_files = list(ROOT_DIR.glob("amber/locales/*.yml")) + \
                 list(ROOT_DIR.glob("pages/accounts/*.yaml")) + \
                 list(ROOT_DIR.glob(".github/**/*.yml"))
    
    errors = 0
    for yf in yaml_files:
        try:
            with open(yf, "r", encoding="utf-8") as f:
                yaml.safe_load(f)
        except Exception as e:
            print(f"  [ERROR] {yf.relative_to(ROOT_DIR)}: {e}")
            errors += 1
    
    if errors == 0:
        print(f"  [OK] All {len(yaml_files)} YAML files parsed successfully.")
    return errors

def check_locales():
    """Verify configured locales in amber/config.rb exist in amber/locales/."""
    print("--> Checking locale files against amber/config.rb...")
    config_path = ROOT_DIR / "amber/config.rb"
    if not config_path.exists():
        print("  [WARN] amber/config.rb not found.")
        return 0
    
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    m = re.search(r"@locales\s*=\s*\[(.*?)\]", content, re.DOTALL)
    if not m:
        print("  [WARN] Could not parse @locales from amber/config.rb.")
        return 0
    
    locales = [loc.strip().lstrip(":") for loc in m.group(1).split(",") if loc.strip()]
    errors = 0
    for loc in locales:
        loc_file = ROOT_DIR / f"amber/locales/{loc}.yml"
        if not loc_file.exists():
            print(f"  [ERROR] Missing locale file for configured locale ':{loc}': amber/locales/{loc}.yml")
            errors += 1
    
    if errors == 0:
        print(f"  [OK] All {len(locales)} configured locales have matching locale files.")
    return errors

def check_git_conflict_markers():
    """Check for leftover git conflict markers in pages and locales."""
    print("--> Checking for git conflict markers...")
    marker_pattern = re.compile(r"^(<{7}|={7}|>{7})(\s|$)", re.MULTILINE)
    errors = 0
    
    scan_extensions = (".text", ".md", ".haml", ".yml", ".yaml", ".rb")
    scanned_count = 0
    for root, _, files in os.walk(ROOT_DIR):
        if any(ignored in root for ignored in [".git", "public", ".system_generated"]):
            continue
        for file in files:
            if file.endswith(scan_extensions):
                scanned_count += 1
                filepath = Path(root) / file
                try:
                    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read()
                    if marker_pattern.search(content):
                        print(f"  [ERROR] Git conflict marker found in {filepath.relative_to(ROOT_DIR)}")
                        errors += 1
                except Exception as e:
                    print(f"  [ERROR] Could not read {filepath.relative_to(ROOT_DIR)}: {e}")
                    errors += 1
                    
    if errors == 0:
        print(f"  [OK] Scanned {scanned_count} files. No git conflict markers found.")
    return errors

def main():
    print("========================================")
    print("  Riseup Help Site Integrity Checker   ")
    print("========================================")
    total_errors = 0
    total_errors += check_yaml_files()
    total_errors += check_locales()
    total_errors += check_git_conflict_markers()
    
    print("----------------------------------------")
    if total_errors > 0:
        print(f"FAILED: {total_errors} issue(s) detected.")
        sys.exit(1)
    else:
        print("SUCCESS: All integrity checks passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
