from functools import reduce
a = [31, 12, 4, 6, 2]
print(reduce(lambda x, y: x * y, a))

import math
print(math.prod(a))
