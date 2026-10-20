# One-time setup on Windows. Run from the repo root:  .\setup.ps1
# If PowerShell refuses to run scripts, first run once:
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

$ErrorActionPreference = "Stop"

if (-not (Test-Path .venv)) {
    python -m venv .venv
}
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

Write-Host "`n--- Bell-state sanity check ---"
python hello.py

Write-Host "`n--- Test suite (unimplemented sessions skip) ---"
pytest -q

if (-not (Test-Path .git)) {
    git init
    git add -A
    git commit -m "Scaffold: environment, tests, agent rules"
}
