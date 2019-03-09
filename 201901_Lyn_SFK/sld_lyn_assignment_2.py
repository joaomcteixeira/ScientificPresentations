from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Lyn's isoforms NMR assignment", ax=ax)
    
    ax1 = Template1.add_figure(figure, [0.01, 0.3, 0.36, 1], "figs/Lyn_family_and_constructs_lined.png")
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")


