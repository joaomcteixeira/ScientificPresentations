import numpy as np

import matplotlib.pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.collections import PatchCollection

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(ax, "Src's Unique Domain")
    
    #ax1 = Template1.add_figure(figure, [0.2, 0.2, 0.6, 0.6], "figs/src_scheme.png")
    ax1 = Template1.add_figure(figure, [-0.05, 0.15, 1, 0.7], "figs/SRC_inkspace_classical.png")
    
    rect = mpatches.Rectangle((0.04, 0.04), 0.9, 0.9, ec="none",
        facecolor="white", alpha=0.8)
    
    ax.add_artist(rect)
    
    #ax2 = Template1.add_axis(figure, [0.1, 0.1, 0.8, 0.8])
    
    #rect = mpatches.Rectangle((0.1, 0.1), 0.8, 0.8, ec="none", zorder=10)
    #patches = [rect]
    
    #collection = PatchCollection(patches, alpha=0.9, color="white")
    
    #ax2.add_collection(collection)
    
    ax1.set_zorder(1)
    ax.set_zorder(2)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
