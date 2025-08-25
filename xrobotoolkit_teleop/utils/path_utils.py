import os

PACKAGE_PATH = os.path.dirname(os.path.abspath(__file__))
# Get the workspace root directory (XenseTeleop)
WORKSPACE_ROOT = os.path.dirname(os.path.dirname(PACKAGE_PATH))
ASSET_PATH = os.path.join(WORKSPACE_ROOT, "assets")
