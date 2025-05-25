class LinearCongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def generate_bitstream(self, bit_count):
        bitstream = []
        while len(bitstream) < bit_count:
            # Generate the next random number
            random_number = self.next()
            # Convert it to binary and extract the bits
            bits = bin(random_number)[2:]  # Convert to binary and remove '0b' prefix
            # Add the bits to the bitstream
            bitstream.extend(int(bit) for bit in bits)

        # Trim the bitstream to the desired length
        return bitstream[:bit_count]

if __name__ == "__main__":
    # Define LCG parameters
    seed = 42          # Initial seed
    a = 1664525        # Multiplier
    c = 1013904223     # Increment
    m = 2**32          # Modulus

    # Create the LCG instance
    lcg = LinearCongruentialGenerator(seed, a, c, m)

    # Generate a bitstream of 1000 bits
    bitstream = lcg.generate_bitstream(1000)
    # Convert the bitstream to a string without commas or spaces
    bitstream_str = ''.join(map(str, bitstream))
    print("Generated Bitstream:", bitstream_str)
