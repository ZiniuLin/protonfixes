""" Death Stranding Director's Cut
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    # If using intel gpu, set VKD3D_FEATURE_LEVEL to 12_0
    if util.is_intel_gpu():
        util.set_environment('VKD3D_FEATURE_LEVEL', '12_0') 
