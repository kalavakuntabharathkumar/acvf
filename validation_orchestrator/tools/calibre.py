import subprocess
class CalibreAdapter:
    def __init__(self,executable="calibre",mock=True): self.executable,self.mock=executable,mock
    def run(self,cell,mode):
        if self.mock:return 0,f"CALIBRE {mode.upper()} PASS cell={cell.name}"
        p=subprocess.run([self.executable,"-runset",f"runsets/{mode}.runset"],capture_output=True,text=True)
        return p.returncode,p.stdout+p.stderr
