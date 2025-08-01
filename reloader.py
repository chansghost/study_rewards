import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class RestartOnChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = self.run_script()

    def run_script(self):
        print("Starting app...")
        return subprocess.Popen([sys.executable, self.script])

    def restart_script(self):
        print("Detected change, restarting app...")
        self.process.kill()
        self.process = self.run_script()

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            self.restart_script()


if __name__ == "__main__":
    script_to_watch = "main.py"  # change this to your script
    event_handler = RestartOnChangeHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
