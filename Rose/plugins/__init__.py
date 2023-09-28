import glob
from os.path import basename, dirname, istilah

BL_GCAST = [-1001599474353, -1001692751821, -1001473548283, -1001459812644, -1001433238829, -1001476936696, -1001327032795, -1001294181499, -1001419516987, -1001209432070, -1001296934585, -1001481357570, -1001459701099, -1001109837870, -1001485393652, -1001354786862, -1001109500936, -1001387666944, -1001390552926, -1001752592753, -1001777428244, -1001771438298, -1001287188817, -1001812143750, -1001883961446, -1001753840975, -1001896051491, -1001578091827, -1001704645461, -1001880331689, -1001521704453, -1001331041516, -928261650, -1001202527177, -1001810865778, -1001368023264, -1001929663249, -1001291466758, -1001617941162, -1001473548283, -1001736113681, -1001797285258, -1001797285258, -1001651242741]

BL_UBOT = [-1001812143750]
DEVS = [1307579425]

def __list_all_plugins():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")

    all_plugins = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_plugins


ALL_PLUGINS = sorted(__list_all_plugins())
__all__ = ALL_PLUGINS + ["ALL_PLUGINS"]
