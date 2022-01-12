from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the grid2viz app"""
    Popen(["grid2viz", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])