import re

# 判斷係唔係漢字
han_regex = re.compile(
    r'[\u3006\u3007\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002ebef\U00030000-\U0003134f]')
punc_regex = re.compile(r'[，。？！：；“”]')
def is_han(c): return bool(han_regex.fullmatch(c) or punc_regex.fullmatch(c))


lines = open("./unreviewed.csv", encoding="utf-8").readlines()
lines = list(set(lines))

output = open("./unreviewed.txt", "w", encoding="utf-8")

for line in lines:
    line = list(line.strip())
    length = len(line)

    if length < 5 or length > 30:
        continue
    else:
        num_han = sum([is_han(c) for c in line])
        if num_han / length > 0.9:
            output.writelines("".join(line) + "\n")
