import os
import sys

# 在 Windows 上，添加 DLL 搜索路径
if sys.platform == 'win32':
    api_dir = os.path.dirname(os.path.abspath(__file__))
    os.add_dll_directory(api_dir)

from .vnctpmd import MdApi      # noqa
from .vnctptd import TdApi      # noqa
from .ctp_constant import *     # noqa
