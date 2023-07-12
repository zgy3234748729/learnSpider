import re

content = 'Extra sting Hello 1234567 World_THis is a Regex Demo Extra    stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)