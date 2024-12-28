# 每一个以拓展名py结尾的python源代码文件都是一个模块
# 模块名同样也是一个标识符，需要符合标识符的命名规则
# 在模块中定义的全局变量，函数，类都是提供给外界直接使用的工具
# 模块就好比是工具包，要想使用这个工具包中的工具，就需要先导入这个模块
import mokuai_demo
print(mokuai_demo.mk_demo1)

# 如果模块名太长不好记忆，可以使用as指定模块的名称，以方便在代码中使用
# 注意：模块别名应该使用大驼峰命名法
import mokuai_demo as Mkd
print(Mkd.mk_demo1)

# 如果希望从某一模块中导入部分工具，就可以使用from ... import的方式导入单个工具(from ... import *可以导入所有工具，但不推荐使用)
# 导入之后：
#   访问不需要通过模块名.
#   可以直接使用模块提供的工具：全局变量，函数，类
from mokuai_demo import mk_demo1
print(mk_demo1)

# 注意：
#   如果两个模块存在同名的函数，那么后导入的模块会覆盖先导入的函数
#   可以使用as更改别名
from mokuai_demo import mk_demo1 as mkdddd
print(mkdddd)

# 模块的搜索顺序：
#   在导入模块时，python解释器会先搜索当前目录指定模块名的文件，如果有就导入
#   如果没有，再搜索系统目录
#   在开发时，给文件起名不要和系统的模块文件重名
import random
random.randint(1, 2)

# python中每一个模块都有一个内置属性__file__可以查看模块的完整路径
print(random.__file__)