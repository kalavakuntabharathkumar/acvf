from concurrent.futures import ThreadPoolExecutor
class LocalParallelScheduler:
    def __init__(self,workers=4): self.workers=workers
    def map(self,fn,items):
        with ThreadPoolExecutor(max_workers=self.workers) as e:return list(e.map(fn,items))
class LsfScheduler(LocalParallelScheduler):
    def submit_command(self,command,queue="normal",cores=1):
        return f"bsub -q {queue} -n {cores} {command}"
