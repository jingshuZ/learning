"""
给出 m, n 代表生成括号（）和方括号[]的对数.请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 1, m=1，生成结果为：()[], [](), [()], ([])
----------------------------------------------------
思路1：
分左右不分括号先往里面填，left = m_left + n_left; right = m_right + n_right
先输入的左边括号，所以 left < right
m 个'(' + ')' n 个 '[' + ']' 每个括号都不可以出现输入次数以上，count限制
dfs
最后输出的元素里只能有 m个'()' 或者 n 个'[ ]' ，筛选限制
-----------------------------------------------------

思路2：先分括号再分左右往里填
'(' 后不可接 ']' 同样，'[' 后不可接 ')' 左边相异
其他的无限制，for i in s
while (s[i] =='(' and s[i+1] != ']' ) or ( s[i] == '[' and s[i+1] != ')' )
往里按照左右填括号

"""



def generateParenthesis(m, n):
    res = []
    cur_str = ''
    s = m + n
    def dfs(cur_str, left, right):
        if left == 0 and right == 0:
            #if '()' * m in cur_str or '[]' * n in cur_str:
                res.append(cur_str)
                return
        if right < left:
            return
        if left > -n:
            dfs(cur_str + '(', left - 1, right)
        if right > -n:
            dfs(cur_str + ')', left, right - 1)
        if left > 0:
            dfs(cur_str + '[', left - 1, right)
        if right > 0:
            dfs(cur_str + ']', left, right - 1)
            
    dfs(cur_str, s, s)
    return res
print(generateParenthesis(1, 1))





# def generateParenthesis(m, n):
#     res = []
#     cur_str = ''
#     s = m + n
#
#     def dfs(cur_str, left, right, s):
#         if left == s and right == s:
#             if '()' * m in cur_str or '[]' * n in cur_str:
#                 res.append(cur_str)
#
#         if left < right:
#             return
#
#         if left < s and cur_str.count('(') < m:
#             dfs(cur_str + '(', left + 1, right, s)
#
#         if right < s and cur_str.count(')') < m:
#             dfs(cur_str + ')', left, right + 1, s)
#
#         if left < s and cur_str.count('[') < n:
#             dfs(cur_str + '[', left + 1, right, s)
#
#         if right < s and cur_str.count(']') < n:
#             dfs(cur_str + ']', left, right + 1, s)
#
#     dfs(cur_str, 0, 0, s)
#     return res
#
# print(generateParenthesis(1, 1))
#
