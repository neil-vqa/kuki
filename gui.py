import os
import webview
from kuki.serve import app
from dotenv import load_dotenv

load_dotenv()

dev_var = os.environ.get("DEV", False)
is_dev = dev_var in ["1", "True", "true"]

if __name__ == "__main__":
    webview.create_window(
        "Kuki | Simple Speech-to-Text App", app, height=600, width=400
    )
    webview.start(debug=is_dev)
