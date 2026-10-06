# Automated Custom-Cell Validation Flow Orchestrator
Python 3.11 demo of a custom-cell validation pipeline.

Run:
```bash
python -m venv .venv
# activate the environment
pip install -r requirements.txt
python -m validation_orchestrator.cli --cells config/cells.json --workers 8
pytest -q
```
Default mode is local/mock: proprietary Spectre, Calibre and LSF binaries are not bundled.
Replace the adapters in `validation_orchestrator/tools/` and scheduler in `scheduler.py` for a real site.
