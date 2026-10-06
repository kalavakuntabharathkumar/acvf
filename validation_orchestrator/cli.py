import argparse
from .orchestrator import *
def main():
    p=argparse.ArgumentParser();p.add_argument("--cells",default="config/cells.json");p.add_argument("--workers",type=int,default=4);p.add_argument("--output",default="runs/latest");a=p.parse_args()
    r=ValidationOrchestrator(a.workers,a.output).run(load_cells(a.cells))
    print(f"Validated {r['total_cells']} cells / {r['total_stages']} stages; PASS={r['passed']} FAIL={r['failed']} RETRY={r['retries']}")
if __name__=="__main__":main()
