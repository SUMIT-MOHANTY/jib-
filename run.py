#!/usr/bin/env python3
import os
import sys

# Add workspace to Python path so 'app' module can be found
workspace = os.path.dirname(os.path.abspath(__file__))
if workspace not in sys.path:
    sys.path.insert(0, workspace)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
