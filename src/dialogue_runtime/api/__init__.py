# -*- coding: utf-8 -*-
"""
dialogue_runtime API模块

提供基于FastAPI的Web服务接口。
"""

from dialogue_runtime.api.server import AtguiguServer, create_app

__all__ = [
    "AtguiguServer",
    "create_app",
]
