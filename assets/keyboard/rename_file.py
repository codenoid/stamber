import glob
import os

a = glob.glob('*.mp3')

for f in a:
	d = f.split("__")
	if len(d) > 1:
		os.rename(f, d[-1])
		print(d[-1])