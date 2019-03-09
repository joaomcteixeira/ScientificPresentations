import numpy as np

from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Lyn UD·SH3 interaction: view from UDs", ax=ax)
    
    ax1 = Template1.add_figure(figure, [0.01, 0.38 - .15, 0.5, 1], "figs/lynA-UD_vs_LynAUSH3.png")
    ax2 = Template1.add_figure(figure, [0.01, 0.2 - .15, 0.68, 1], "figs/Lyn_UD_LynA_CSPs.png")
    
    ax3 = Template1.add_figure(figure, [0.01, 0.38 - .55, 0.5, 1], "figs/LynB-USH3_vs_LynAUSH3_constructs.png")
    ax4 = Template1.add_figure(figure, [0.01, 0.2 - .55, 0.68, 1], "figs/Lyn_UD_LynB_CSPs.png")
    
    
    ax5 = Template1.add_figure(figure, [0.04, 0.77 - .5, 0.02, 1], "figs/eyes.png")
    ax6 = Template1.add_figure(figure, [0.03, 0.37 - .5, 0.02, 1], "figs/eyes.png")
    
    # conclusions
    text_ = r"""
$\bf{Conclusions:}$

- In contrast to what was found for Src,
  the initial 18 residues (SH4+) are not
  affected by the presence of the SH3,
  for both LynA and B.
  
- Only the UD interacts with the SH3.

- The most affected region is that absent
  in LynB (alternative-splicing).
    
    

- The last 16 residues of the UD interact
  with the nSrc and 3$_{10}$ loops in SH3.

- LynA region 23-43 interacts with RT loop.

- Reg. 23-43 perturns interactions with nSrc
  loop and 3$_{10}$ region.
"""
    
    ax.text(x=0.7, y=0.85, s=text_, **Template1.text_box)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
