def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s
    re = ["" for i in range(numRows)]
    for i in range(len(s)):
        pos = i % ((numRows-1)*2)
        if pos > (numRows-1):
            pos = 2*(numRows-1) - pos
        re[pos] += s[i]
    return "".join(re)
print(convert("LEETCODEISHIRING", 3))