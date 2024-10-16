from orbit.utils.xml import XmlDataAdaptor
from epics import caput

def set_from_mstate(filename: str, verbose: bool = False) -> None:
    """Load quadrupole parameters from .mstate file."""
    state_da = XmlDataAdaptor.adaptorForFile(filename)
    for item in state_da.data_adaptors[0].data_adaptors:
        pv_name = item.getParam("setpoint_pv")
        pv_val = float(item.getParam("setpoint"))
        caput(pv_name,pv_val)
        if verbose:
            print(f"set {pv_name} {pv_val}")
 
if __name__ == "__main__":
    quad_params_from_mstate('settings_bend2_hdr_240821.mstate',verbose=True)
        
