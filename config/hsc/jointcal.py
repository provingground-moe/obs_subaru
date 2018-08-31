import os.path
from lsst.utils import getPackageDir

filterMapFile = os.path.join(getPackageDir("obs_subaru"), "config", "hsc", "filterMap.py")
config.photometryRefObjLoader.load(filterMapFile)
config.astrometryRefObjLoader.load(filterMapFile)
