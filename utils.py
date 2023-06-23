import copy
import time
import random
import math as mt
import numpy as np
import pandas as pd
import seaborn as sns
import networkx as nx
import moviepy.editor as mpy
import matplotlib.pyplot as plt

from matplotlib import cm
from fa2 import ForceAtlas2
from moviepy.video.io.bindings import mplfig_to_npimage

palette = {
    "sys1":{
        "active": '#4472C4',
        "destroyed": '#E7E6E6',
        "under_attack": '#DAE3F3'
    },
    "sys2":{
        "active": '#FF9300',
        "destroyed": '#E7E6E6',
        "under_attack": '#FBE5D6'
    }
}

forceatlas2 = ForceAtlas2(
    outboundAttractionDistribution=True,  # Dissuade hubs
    linLogMode=False,  # NOT IMPLEMENTED
    adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
    edgeWeightInfluence=1.0,

    # Performance
    jitterTolerance=1.0,  # Tolerance
    barnesHutOptimize=True,
    barnesHutTheta=1.2,
    multiThreaded=False,  # NOT IMPLEMENTED

    # Tuning
    scalingRatio=2.0,
    strongGravityMode=False,
    gravity=5.0,

    # Log
    verbose=True)

