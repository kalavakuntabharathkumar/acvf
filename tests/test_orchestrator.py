from validation_orchestrator.orchestrator import *
def test_cells(): assert len(load_cells("config/cells.json"))==8
def test_run(tmp_path):
    r=ValidationOrchestrator(2,tmp_path).run(load_cells("config/cells.json")[:2])
    assert r["total_stages"]==6 and r["passed"]==6
