#/usr/bin/python3
import os
print('download and install snap...')
os.system('sudo apt install snap')
print('install rustup...')
os.system('snap install rustup --classic')
print('install latest stable rust...')
os.system('rustup toolchain install stable')
