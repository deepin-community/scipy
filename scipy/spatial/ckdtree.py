# This file is not meant for public use and will be removed in SciPy v2.0.0.
# Use the `scipy.spatial` namespace for importing the functions
# included below.

import warnings
from . import _ckdtree


__all__ = [  # noqa: F822
    'cKDTree',
    'cKDTreeNode',
    'coo_entries',
    'operator',
    'ordered_pairs',
    'os',
    'scipy',
    'threading',
]


def __dir__():
    return __all__


def __getattr__(name):
    if name not in __all__:
        raise AttributeError(
            "scipy.spatial.ckdtree is deprecated and has no attribute "
            f"{name}. Try looking in scipy.spatial instead.")

    warnings.warn(f"Please use `{name}` from the `scipy.spatial` namespace, "
                  "the `scipy.spatial.ckdtree` namespace is deprecated.",
                  category=DeprecationWarning, stacklevel=2)

    return getattr(_ckdtree, name)
