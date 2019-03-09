from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.collections import PatchCollection

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Conclusion", ax=ax)
    
    ax1 = Template1.add_figure_border(
        figure,
        [-0.1, 0.1, 0.8, 0.8],
        "figs/Graphical_Abstract.png"
        )
    
    text_ = r"""$\bf{Conclusions}$

- Lyn's Unique Domain interaction with SH3 domain
  displays characteristics of a fuzzy interaction as in Src.

- This interaction differs between Lyn's natural isoforms.

- Both Lyn A and B share UD·SH3 interaction at nSrc loop
  and 3$_{10}$ region (perturbations).

- Lyn A has additional interactions with RT Loop.

- Contrary to Src, the SH4 domain does NOT interact with
  the SH3 domain.

- Lyn B Unique Domain is more compact than that of Lyn A.

- PPP displaces interactions at the RT loop, yet iterations
  at the nSrc loop are partially maintained.
"""
    
    ax.text(
        x=0.6,
        y=0.9,
        s=text_,
        **Template1.text_box
        )
    
    ref = "Teixeira, J. M. C., et.al. (2018). Molecules, 23(11)"
    
    ax.text(
        x=0.64,
        y=0.1,
        s=ref,
        **{**Template1.text_box, **{"color": Template1.color}}
        )
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")


