from dataclasses import dataclass,asdict
@dataclass
class Cell: name:str; corner:str; netlist:str
@dataclass
class JobResult:
    cell:str; stage:str; status:str; return_code:int; message:str; attempts:int=1
    def to_dict(self): return asdict(self)
