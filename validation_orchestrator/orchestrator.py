import json,time
from pathlib import Path
from .models import Cell,JobResult
from .tools.spectre import SpectreAdapter
from .tools.calibre import CalibreAdapter
from .scheduler import LocalParallelScheduler
from .classifier import LogClassifier
class ValidationOrchestrator:
    def __init__(self,workers=4,output_dir="runs/latest",mock=True):
        self.out=Path(output_dir);self.out.mkdir(parents=True,exist_ok=True)
        self.spectre=SpectreAdapter(mock=mock);self.calibre=CalibreAdapter(mock=mock)
        self.scheduler=LocalParallelScheduler(workers);self.classifier=LogClassifier()
    def validate_cell(self,c):
        out=[]
        for s in ["spectre","drc","lvs"]:
            code,log=self.spectre.run(c) if s=="spectre" else self.calibre.run(c,s)
            cls=self.classifier.classify(log)
            out.append(JobResult(c.name,s,"PASS" if code==0 else cls,code,log))
        return out
    def run(self,cells):
        t=time.time();groups=self.scheduler.map(self.validate_cell,cells)
        rs=[x for g in groups for x in g]
        report={"duration_seconds":round(time.time()-t,3),"total_cells":len(cells),"total_stages":len(rs),
        "passed":sum(x.status=="PASS" for x in rs),"failed":sum(x.status=="FAIL" for x in rs),
        "retries":sum(x.status=="RETRY" for x in rs),"results":[x.to_dict() for x in rs]}
        (self.out/"report.json").write_text(json.dumps(report,indent=2));return report
def load_cells(path):
    return [Cell(**x) for x in json.loads(Path(path).read_text())]
