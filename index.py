import os
import time
import shutil
os.system("clear")
# --------- Helper Functions ---------
def info(msg):
    print(f"\033[1;32m[✔]\033[0m {msg}")

def install_if_missing(module_name, pip_name=None):
    try:
        __import__(module_name)
        info(f"Module '{module_name}' already installed.")
    except ModuleNotFoundError:
        info(f"Installing module: {module_name}")
        os.system(f"pip install {pip_name or module_name}")

def is_command_available(cmd):
    return shutil.which(cmd) is not None

# --------- Install Python Modules ---------
install_if_missing("prompt_toolkit")
install_if_missing("rich")
install_if_missing("requests")
install_if_missing("colorama")

# --------- Install Ruby + lolcat if not present ---------
if not is_command_available("lolcat"):
    info("Installing ruby & lolcat...")
    os.system("pkg install ruby -y")
    os.system("gem install lolcat")

# --------- Final Check ---------
if is_command_available("lolcat"):
    info("lolcat installed successfully!")
else:
    print("\033[1;31m[✘] lolcat installation failed! Manual install may be required.\033[0m")

# --------- Start Your Tool ---------
os.system('clear')
os.system('echo "🚀 Starting Your Tool..." | lolcat')
time.sleep(1)

os.system("python fuck.py")