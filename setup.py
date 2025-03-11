import os
import sys
import subprocess

def run_command(command):
    """Runs a shell command and exits if it fails."""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"ERROR: Command failed - {command}")
        sys.exit(1)

# Detect OS
is_windows = os.name == "nt"
python_exec = sys.executable  # Get the current Python executable

# Clone repo
if not os.path.exists("OM1"):
    print("Cloning repository...")
    run_command("git clone https://github.com/OpenmindAGI/OM1.git")

# Change directory and come out before installing requirements
# os.chdir("..")
run_command(f' pip install uv')
# Create Virtual Environment
run_command("pip install -r requirements.txt")
# Initialize Git Submodules
print("Initializing Git Submodules...")
os.chdir("OM1")
run_command("git submodule update --init")

if not os.path.exists("OM1/.venv"):
    print("Setting up Virtual Environment...")
    run_command("uv venv")


# Install FFmpeg
if is_windows:
    print("Please install FFmpeg manually: https://www.gyan.dev/ffmpeg/builds/ and add the path to bin in system variables")
    print("Please make sure you have MS Visual Studio C++ 14 or higher version installed on your system")
    print("Locate the config folder and add your Openmind API key in /config/spot.json. If you do not already have one, you can obtain a free access key at https://portal.openmind.org/.")
else:
    print("Installing FFmpeg...")
    run_command("sudo apt update && sudo apt install -y ffmpeg || brew install ffmpeg")

print("Setup Complete!")