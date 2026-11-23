# IHP SG13G2 Hardware LZ4 + Castagnoli CRC-32C NVMe Engine

<a href="https://github.com/nk-verif-labs/ihp-sg13g2-lz4-nvme-engine/actions/workflows/ci.yml"><img src="https://github.com/nk-verif-labs/ihp-sg13g2-lz4-nvme-engine/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>

Synthesizable 32-bit AXI4-Stream hardware **LZ4 rolling-hash match engine** paired with a single-cycle **Castagnoli CRC-32C (`0x82F63B78`)** integrity datapath, hardened on **IHP SG13G2 (130nm BiCMOS)** via LibreLane (`50 MHz`, `45%` utilization) and verified across RTL & post-PnR Gate-Level Cocotb CI ([run 45130706417](https://github.com/nk-verif-labs/ihp-sg13g2-lz4-nvme-engine/actions/runs/45130706417)).

## Quick start
    nix develop --command make clone-pdk
    nix develop --command make sim
    nix develop --command make librelane-nodrc
    nix develop --command make sim-gl

## Need something similar?
NK Verif Labs offers verification and RTL-to-GDSII services. Email **nkveriflabs@gmail.com**.
