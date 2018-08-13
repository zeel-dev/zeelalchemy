# vim: set fileencoding=utf-8 :
"""

~~~~~~~~~~~
Dictalchemy
~~~~~~~~~~~

"""
from __future__ import absolute_import, division

from zeelalchemy.classes import DictableModel
from zeelalchemy.utils import make_class_dictable, asdict
from zeelalchemy.errors import (DictalchemyError, UnsupportedRelationError,
                                MissingRelationError)

__all__ = [DictableModel,
           make_class_dictable,
           asdict,
           DictalchemyError,
           UnsupportedRelationError,
           MissingRelationError]
