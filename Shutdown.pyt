import subprocess

def shutdown(delay: int = 0):
    """Shuts down the computer after a specified delay (in seconds)."""
    subprocess.run["shutdown", "/s", "/t", str(delay)], shell=True