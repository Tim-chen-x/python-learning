# 需求：在控制台中央输入你好世界
import shutil

text = "hello world"
# 获取控制台宽度
console_width = shutil.get_terminal_size().columns
# 计算居中位置
centered_text = text.center(console_width)
print(centered_text)