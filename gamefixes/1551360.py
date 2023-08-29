""" Forza Horizon 5
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    # If using intel gpu, set vk vendor to 0x1002
    if util.is_intel_gpu():
        util.set_environment('force_vk_vendor', '0x1002') 
