import re

# 所以说，在做匹配的时候，字符串中间尽量使用非贪梦匹配，也就是用.*？代替.*，以免出现匹配结果缺失的情况。
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
