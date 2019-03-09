from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

import numpy as np

from templates import Template1


@Template1.main_title_template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_maintitle(s="Lyn UD·SH3 interaction: view from SH3", ax=ax)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
