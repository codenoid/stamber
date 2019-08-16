import glob
import os
import json

a = glob.glob('*.wav')

print(json.dumps(a))

# for f in a:
# 	d = f.split("__")
# 	if len(d) > 1:
# 		os.rename(f, d[-1])
# 		print(d[-1])