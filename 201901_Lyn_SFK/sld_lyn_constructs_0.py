from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Experimental approach", ax=ax)
    
    ax1 = Template1.add_figure(figure, [-0.05, 0.2, 0.6, 0.6], "figs/lyn_graphical_abs.png")
    
    ax1.axis("on")
        
    ax1.tick_params(
        axis='both',
        which='both',
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
        )
        
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")


