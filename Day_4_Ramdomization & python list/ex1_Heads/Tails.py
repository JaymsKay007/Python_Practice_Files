''' 
INSTRUCTION...
Heads or Tails...
You're going to write a virtual toss program. It will randomly tell the user "Heads or Tails".
IMPORTANT: The first letter should be capitalize and spelt exactly like in the example e.g. Heads, not heads.

1 means Heads
0 means Tails
'''

import random

coin = random.randint(0, 1)

if coin == 0:
    print("Tails")
else:
    print("Heads")
