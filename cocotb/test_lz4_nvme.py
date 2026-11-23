import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

def sw_crc32c(words):
    c = 0xFFFFFFFF
    for w in words:
        c ^= w
        for _ in range(32): c = ((c >> 1) ^ 0x82F63B78) if (c & 1) else (c >> 1)
    return c ^ 0xFFFFFFFF

@cocotb.test()
async def test_lz4_and_crc32c(dut):
    cocotb.start_soon(Clock(dut.clk, 20, unit="ns").start())
    dut.rst_n.value = 0; dut.s_valid.value = 0; dut.m_ready.value = 1; dut.tlast.value = 0; dut.s_data.value = 0
    for _ in range(3): await RisingEdge(dut.clk)
    dut.rst_n.value = 1; words = [0x4E564D65, 0x12345678, 0x4E564D65]
    for i, w in enumerate(words):
        dut.s_valid.value = 1; dut.s_data.value = w; dut.tlast.value = int(i == len(words) - 1)
        await RisingEdge(dut.clk); await Timer(1, unit="ns")
        if i == 2: assert int(dut.match_hit.value) == 1
    assert int(dut.crc32c_out.value) == sw_crc32c(words)
