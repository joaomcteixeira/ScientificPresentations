from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.collections import PatchCollection

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Conclusion", ax=ax)
    
    ax1 = Template1.add_figure_border(
        figure,
        [-.1, 0.1, 0.8, 0.8],
        "figs/lyn_graphical_abs.png"
        )
    
    
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")


