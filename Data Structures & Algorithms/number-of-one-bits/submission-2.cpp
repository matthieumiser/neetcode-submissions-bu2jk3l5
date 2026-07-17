class Solution {
public:
uint32_t hammingWeight(uint32_t x) {
    x = x - ((x >> 1) & 0x55555555);              // pairs: 2-bit counts
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333); // nibbles: 4-bit counts
    x = (x + (x >> 4)) & 0x0F0F0F0F;               // bytes: 8-bit counts
    return (x * 0x01010101) >> 24;                 // sum the 4 bytes
}
};
