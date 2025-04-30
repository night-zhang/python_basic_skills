"""
数字分隔符
"""
n: int = 10_000_000_000_000
print(n)
n: int = 10_0000_0000_0000
print(n)

n: int = 10000000000000
# 默认只支持, _ 作为分隔符
print(f"{n:,}")  # 10,000,000,000,000
print(f"{n:_}")  # 10_000_000_000_000

print("=============================")
"""
字符串填充
"""
var: str = 'var'
print(f"{var:>20}")  # '               var'
print(f"{var:<20}")  # 'var               '
print(f"{var:^20}")  # '         var         '
print(f"{var:_^20}")  # '______var__________'
print(f"{var:#>20}")  # '############var'
print("=============================")
"""
时间格式化
"""

from datetime import datetime
now: datetime = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")
print(f"{now:%c}")  # CST
print(f"{now:%I%p}")  # 12小时制

print("=============================")
"""
浮点数
"""
n: float = 12345.6789
print(round(n, 2))  # 12345.68
print(f"{n:.2f}")  # 12345.68
print(f"{n:.0f}")  # 12346
print(f"{n:,.1f}")  # 12,345.7


"""
计算，中括号内加等号自动优化打印公式和结果，不加等号只有结果
"""
a: int = 5
b: int = 3
my_var: str = "some var"

print(f"{a + b}")  # 8
print(f"{a + b = }")  # a + b = 8
print(f"{my_var = }")  # my_var = some var

print("=============================")