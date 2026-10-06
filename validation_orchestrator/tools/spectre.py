import subprocess
class SpectreAdapter:
    def __init__(self,executable="spectre",mock=True): self.executable,self.mock=executable,mock
    def run(self,cell):
        if self.mock:return 0,f"SPECTRE PASS cell={cell.name}"
        p=subprocess.run([self.executable,cell.netlist],capture_output=True,text=True)
        return p.returncode,p.stdout+p.stderr
