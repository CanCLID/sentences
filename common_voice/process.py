import re
import pandas as pd

han_regex = re.compile(r'[\u3006\u3007\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002ebef\U00030000-\U0003134f]')
is_han = lambda c: bool(han_regex.fullmatch(c))

lines = open("unreviewed.csv", encoding="utf-8").readlines()

for line in lines:
  line = line.strip().split()
  if len(line) < 5 or len(line) >30:
    continue
  else:
