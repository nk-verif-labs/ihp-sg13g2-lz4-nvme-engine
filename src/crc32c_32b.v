`timescale 1ns/1ps
module crc32c_32b (
  input  wire [31:0] crc_in,
  input  wire [31:0] data_in,
  output reg  [31:0] crc_out
);
  integer i;
  reg [31:0] c;
  always @(*) begin
    c = crc_in ^ data_in;
    for (i = 0; i < 32; i = i + 1)
      c = c[0] ? ((c >> 1) ^ 32'h82F63B78) : (c >> 1);
    crc_out = c;
  end
endmodule
