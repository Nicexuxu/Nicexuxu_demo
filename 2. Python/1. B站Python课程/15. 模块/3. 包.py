import pack     # 导入pack这个文件夹
'''
__init__.py：
    import de1          # 这种语句会让python解释器直接在当前(3. 包.py)目录下查找，并写入缓存
    import de2
    from . import de1   # 写入缓存后不会再重复导入同名的模块
    from . import de2
'''

pack.de1.de1fun()       # 虽然是导入pack后使用的模块，但实际上因为导入时的机制，看似访问pack的de1，实际上是当前目录的de1

'''
我在a.py里面调用了pack_dict这个包，包里面的__init__.py内容是：
import de1
from . import de1
如果a.py的同目录下有de1，pack_dict里面也有de1，那么会调用哪个

初始执行情况
当你在 a.py 中导入 pack_dict 包时（例如使用 import pack_dict 语句），Python 会开始执行 pack_dict 包下的 __init__.py 文件来初始化这个包。
在 __init__.py 文件中存在 import de1 和 from. import de1 这两个导入语句：
对于 import de1：
Python 会按照常规的模块搜索路径去查找名为 de1 的模块。搜索路径首先会包含当前执行文件（也就是 a.py）所在的目录，所以它会优先找到 a.py 同目录下的 de1 模块并尝试导入它。
如果这个模块能够被正常导入（比如模块本身语法正确、不存在缺失依赖等情况），那么就会将该 de1 模块的内容加载到 pack_dict 包的命名空间中（通过 __init__.py 来定义包的初始命名空间）。
对于 from. import de1：
这是相对导入语句，它明确表示要从当前包（也就是 pack_dict 包自身）中导入名为 de1 的模块。Python 会基于当前包的结构去查找对应的模块。
不过在执行到这行代码时，前面已经通过 import de1 导入了 a.py 同目录下的 de1 模块，并且 Python 模块有缓存机制，已经导入过的模块不会重复导入（默认情况下，后续再次遇到相同的导入语句基本会使用缓存中的模块对象），
所以这里相对导入语句基本不会再去重新查找和导入模块了，而是也会使用之前已经导入的那个 a.py 同目录下的 de1 模块（假设没有其他特殊情况改变模块导入的逻辑和缓存机制等）。
'''