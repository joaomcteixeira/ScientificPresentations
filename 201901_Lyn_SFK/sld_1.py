from matplotlib import pyplot as plt
# from matplotlib import patches as mpatches
# from matplotlib.collections import PatchCollection

from templates import Template1


@Template1.page0
def slide(page_number, figure=None, ax=None, **kwargs):
    
    Template1.add_maintitle(
        ax=ax,
        s=(
            "Lyn's is a member of the Src Family Kinases..."
            )
        )
    
    sig = r"""$\bf{João\ M.C.\ Teixeira}$
http://bit.ly/joaomcteixeira"""
    
    ax.text(
        x=0.01,
        y=0.02,
        s=sig,
        fontname=Template1.font,
        color=Template1.color,
        fontsize=12,
        )
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
