""" Shadow of the Tomb Raider
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Requires media foundation dlls
    """

    util.protontricks('d3dcompiler_47')

    # If using intel gpu, set vk vendor to -1
    if util.is_intel_gpu():
        util.set_environment('force_vk_vendor', '-1') 
