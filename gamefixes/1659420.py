""" Uncharted Collection
"""
#pylint: disable=C0103

from protonfixes import util
import multiprocessing


def main():
    """ Legacy Collection
    """

    if multiprocessing.cpu_count() > 16:
        util.set_environment('WINE_CPU_TOPOLOGY', '16:0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15')

    # If using intel gpu, set VKD3D_FEATURE_LEVEL to 12_0
    if util.is_intel_gpu():
        util.set_environment('VKD3D_FEATURE_LEVEL', '12_0') 
