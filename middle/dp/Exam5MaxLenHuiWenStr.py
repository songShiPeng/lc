"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""
import math


def dp(s: str) -> str:
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    maxi=0
    maxj=0
    maxl=0
    for i in range(len(s) -1 , -1, -1):
        for j in range(i,len(s)):
            if s[i] == s[j]:
                if(j - i < 2):
                    dp[i][j] = True
                elif i+1 > len(s) - 1 and j -1 < 0:
                    dp[i][j] = False
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False
            if dp[i][j] and j - i > maxl:
                maxi = i
                maxj = j
                maxl = j -i

    return s[maxi:maxj+1]


# 马拉车
def manarcher(os: str) -> str:
    # 先加#
    s = '#' + '#'.join(os) + '#'
    # RL[i]表示第i个字符为中心的最长回文半径
    RL = [0 for i in range(len(s))]
    max_rl = 0
    # 当前可以触达的最右侧位置
    MAX_RIGHT = 0
    # MAX_RIGHT对应的位置
    pos = 0
    for i in range(len(s)):
        #如果小于最右侧，则可以服用对称轴的RL[j]，取RL[j]和MAX_RIGHT-i的较小值
        if i < MAX_RIGHT:
            if RL[pos * 2 - i] < MAX_RIGHT - i:
                RL[i] = RL[pos * 2 - i]
            else:
                RL[i] = MAX_RIGHT - i
        #无论是否服用，都需要扩散
        # 以RL[i]的值为基础扩散
        for j in range(RL[i] + 1, len(s)):
            if i-j >-1 and i + j < len(s) and s[i - j] == s[i + j]:
                RL[i] = j
            else:
                break
        # 扩散之后更新pos和maxright
        if (i + RL[i] > MAX_RIGHT):
            MAX_RIGHT = i + RL[i]
            pos = i
        if RL[i] > RL[max_rl]:
            max_rl = i
    return s[max_rl - RL[max_rl]:max_rl + RL[max_rl]].replace('#','')

print(dp("aaabaaaa"))
