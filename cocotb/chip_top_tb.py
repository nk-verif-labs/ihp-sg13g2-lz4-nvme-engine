import glob, os
from pathlib import Path
from cocotb_tools.runner import get_runner

root = Path(__file__).resolve().parent.parent
gl = os.getenv("GL") == "1"
sources = [root / "src" / "crc32c_32b.v", root / "src" / "lz4_nvme_top.v"]
defines = {}
if gl:
    pdk_root, pdk = os.environ["PDK_ROOT"], os.getenv("PDK", "ihp-sg13g2")
    sources = [root / "final" / "nl" / "lz4_nvme_top.nl.v"] + sorted(
        Path(p) for p in glob.glob(f"{pdk_root}/{pdk}/libs.ref/sg13g2_stdcell/verilog/*.v")
    )
    defines = {"FUNCTIONAL": 1, "UNIT_DELAY": "#0"}
runner = get_runner("icarus")
runner.build(sources=sources, hdl_toplevel="lz4_nvme_top", defines=defines, build_dir=root / "cocotb" / "sim_build", always=True)
runner.test(hdl_toplevel="lz4_nvme_top", test_module="test_lz4_nvme", build_dir=root / "cocotb" / "sim_build")
