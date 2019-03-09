from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Experimental approach", ax=ax)
    
    ax1 = Template1.add_figure_border(figure, [-0.05, 0.2, 0.6, 0.6], "figs/lyn_graphical_abs.png")
    
    ax2 = Template1.add_figure(figure, [0.47, 0.2, 0.5, 1], "figs/Lyn_family_and_constructs.png")
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")

