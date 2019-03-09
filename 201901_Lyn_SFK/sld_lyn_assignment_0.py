from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

from templates import Template1


@Template1.main_title_template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_maintitle(s="Lyn's isoforms NMR assignment", ax=ax)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")


