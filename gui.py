import os
import webview
from dotenv import load_dotenv
from streamlit import config as _config
from streamlit.web.bootstrap import run
from multiprocessing import Process

load_dotenv()

dev_var = os.environ.get("DEV", False)
is_dev = dev_var in ["1", "True", "true"]


def run_streamlit_app():
    _config.set_option("server.headless", True)
    run("st_ui.py", args=[], flag_options=[], is_hello=False)


if __name__ == "__main__":
    streamlit_process = Process(target=run_streamlit_app)
    streamlit_process.start()

    def on_closed():
        if streamlit_process.is_alive():
            streamlit_process.terminate()

    window = webview.create_window(
        title="Kuki | Simple Speech-to-Text App",
        url="http://localhost:8501",
        width=350,
        height=550,
    )
    window.events.closed += on_closed
    webview.start(debug=is_dev)
