import random
output_mt = ''.join(str(random.getrandbits(1)) for _ in range(1000000))

print(output_mt[:100000])