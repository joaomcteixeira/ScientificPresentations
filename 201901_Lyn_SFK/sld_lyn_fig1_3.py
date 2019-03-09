from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

import numpy as np

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Lyn UD·SH3 interaction: view from SH3", ax=ax)
    
    ax1 = Template1.add_figure(figure, [0.01, 0.38, 0.36, 1], "figs/Lyn_constructs_AB_USH3_vs_SH3.png")
    ax2 = Template1.add_figure(figure, [0.065, 0.44, 0.02, 1], "figs/eyes.png")
    ax2.set_zorder(3)

    
    list_of_figs = [
        "figs/USH4-SH3_LynA.png",
        "figs/USH4-SH3_LynB.png",
        ]
    
    x_pos = np.linspace(0.01, 0.65, 3)
    
    list_of_figures = []
    
    for xx, fig_path in zip(x_pos, list_of_figs):
        
        list_of_figures.append(
            Template1.add_figure(figure, [xx, -0.08, 0.27, 1], fig_path)
            )
        
        list_of_figures[-1].set_zorder(1)
    
    ax.set_zorder(2)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
