from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Lyn's isoforms NMR assignment", ax=ax)
    
    ax1 = Template1.add_figure(figure, [0.01, 0.3, 0.36, 1], "figs/Lyn_family_and_constructs_lined.png")
    
    text_ = r"""$\bf{Collaborators:}$
    
    - Szymon Zerko and Dr. Wiktor Kozminski
        University of Warsaw, Poland.

$\bf{Techniques:}$

    - 278K (UD) and 298K (UD-SH3)
    - temperature curve for assignment transfer

Pons' Lab:
    - Combination of 3D BEST-TROSY (NUS) experiments

Kozminski's Lab:
    - Combination of 3D and 5D NUS experiments
"""
    
    ax.text(x=0.02, y=0.6, s=text_, **Template1.text_box)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")


