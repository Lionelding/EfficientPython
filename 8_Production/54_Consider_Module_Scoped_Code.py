# Item 54: Consider Module-Scoped Code
"""
1. Tailor a module's content to different deployment enviornments by using normal python statements in module scope
"""

import sys

# Example 1: The production and development environments are different

TESTING = True
if TESTING:
	print('Development Environment')

else:
	print('Production Enviornment')

print(sys.platform.upper())