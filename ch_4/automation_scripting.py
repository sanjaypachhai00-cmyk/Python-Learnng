# 🗺️ The Automation Landscape

# Domain	          Common Tools
# Files & folders	  pathlib, shutil, os, glob
# Text / data      	  csv, json, re, pandas
# Shell & processes	  subprocess, shlex, os.system
# Web scraping	      requests, httpx, bs4, playwright
# Web automation	  playwright, selenium
# OS automation	      pyautogui, keyboard, mouse
# Scheduling	      schedule, APScheduler, cron, Task Scheduler
# CLI tools	          argparse, click, typer, rich
# Cloud / DevOps	  boto3, docker, paramiko, fabric
# Email / messaging	  smtplib, imaplib, slack_sdk
# Excel / Office	  openpyxl, xlsxwriter, python-docx
# PDF	              pypdf, pdfplumber, reportlab
# Monitoring files	  watchdog
# Notifications	      plyer, win10toast, notifiers

# Automation Best Practices
# ✅ pathlib over os.path
# ✅ subprocess with list args — never os.system
# ✅ logging over print
# ✅ main() -> int + if __name__ == "__main__" + sys.exit(main())
# ✅ Env vars / .env for secrets, never hardcode
# ✅ check=True + timeout= on every subprocess / HTTP call
# ✅ Retries with backoff for network calls
# ✅ Idempotent — safe to re-run
# ✅ Lock files to prevent concurrent runs
# ✅ --dry-run flag for destructive actions
# ✅ Argparse / Typer — no raw sys.argv parsing
# ✅ Type hints + ruff + mypy — even for scripts
# ✅ Tests for the tricky parts — parsing, transformations
# ✅ Structure as a package when it grows beyond 200 lines

               #SEE YOU LATER