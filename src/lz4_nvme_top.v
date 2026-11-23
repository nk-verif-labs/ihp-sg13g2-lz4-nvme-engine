`timescale 1ns/1ps
module lz4_nvme_top (
  input  wire        clk, rst_n, s_valid, m_ready, tlast,
  input  wire [31:0] s_data,
  output wire        s_ready,
  output reg         m_valid, m_last, match_hit,
  output reg  [31:0] m_data, crc32c_out
);
  reg [31:0] hist [0:7];
  reg [31:0] crc_acc;
  wire [31:0] crc_next;
  wire [2:0] h_idx = s_data[2:0] ^ s_data[10:8] ^ s_data[18:16];
  wire hit = (hist[h_idx] == s_data) && (s_data != 32'd0);
  crc32c_32b u_crc (.crc_in(crc_acc), .data_in(s_data), .crc_out(crc_next));
  assign s_ready = !m_valid || m_ready;
  integer k;
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      m_valid <= 0; m_last <= 0; match_hit <= 0; m_data <= 0; crc_acc <= 32'hFFFFFFFF; crc32c_out <= 0;
      for (k = 0; k < 8; k = k + 1) hist[k] <= 0;
    end else if (s_ready) begin
      m_valid <= s_valid; m_last <= s_valid & tlast;
      if (s_valid) begin
        match_hit <= hit;
        m_data <= hit ? {16'hF004, 13'd0, h_idx} : s_data;
        hist[h_idx] <= s_data;
        crc_acc <= tlast ? 32'hFFFFFFFF : crc_next;
        crc32c_out <= ~crc_next;
      end
    end
  end
endmodule
