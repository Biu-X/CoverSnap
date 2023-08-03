import sys
from pathlib import Path

# 获取项目根目录的绝对路径
root_path = Path(__file__).resolve().parent.absolute() / 'src' / 'coversnap'

# 将项目根目录添加到模块搜索路径中
sys.path.insert(0, str(root_path))

print(str(root_path) + ' added to sys.path successfully.')
