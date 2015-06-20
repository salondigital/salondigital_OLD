"""
    Plugin for executing programs
"""

import sys

# plugin constants
__plugin__ = "SalonDigital Plugin"
__author__ = "Tocinillo"
__version__ = "0.1"

if __name__ == "__main__":
    import resources.lib.executor as plugin
    plugin.Main()

sys.modules.clear()
