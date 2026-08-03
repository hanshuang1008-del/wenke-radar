"""pytest 公共配置：把项目根目录加进导入路径"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pytest
import config


@pytest.fixture(autouse=True)
def generic_test_profile(monkeypatch):
    """通用单测使用开源基线画像；个人产品画像由专门用例单独验证。

    这样配置文件可以按个人需求修改，而通用过滤/渲染契约不会因为默认城市、届别、
    方向变化而产生与功能无关的失败。
    """
    personal_excludes = set(getattr(config, "PRODUCT_PROFILE_EXCLUDE_TITLE_KEYWORDS", []))
    base_excludes = [kw for kw in config.EXCLUDE_TITLE_KEYWORDS if kw not in personal_excludes]
    monkeypatch.setattr(config, "FILTER_BY_DIRECTION", True)
    monkeypatch.setattr(config, "TARGET_DIRECTIONS", None)
    monkeypatch.setattr(config, "TARGET_GRAD_YEARS", [2025, 2026, 2027])
    monkeypatch.setattr(config, "CAMPUS_FOCUS_YEARS", None)
    monkeypatch.setattr(config, "TARGET_CITIES", [])
    monkeypatch.setattr(config, "STRICT_TARGET_CITIES", False)
    monkeypatch.setattr(config, "SOCIAL_MAX_EXPERIENCE_YEARS", 2)
    monkeypatch.setattr(config, "EXCLUDE_TITLE_KEYWORDS", base_excludes)
