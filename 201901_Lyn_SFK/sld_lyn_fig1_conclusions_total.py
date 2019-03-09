from matplotlib import pyplot as plt
from matplotlib import patches as mpatches

import numpy as np

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Lyn UD·SH3 interaction: view from SH3", ax=ax)
    
    ax1 = Template1.add_figure(figure, [0.01, 0.38, 0.36, 1], "figs/Lyn_constructs_AB_USH3_vs_SH3.png")
    ax2 = Template1.add_figure(figure, [0.065, 0.44, 0.02, 1], "figs/eyes.png")
    
    
    list_of_figs = [
        "figs/USH4-SH3_LynA.png",
        "figs/USH4-SH3_LynB.png",
        "figs/USH4-SH3_LynA-LynB.png",
        ]
    
    x_pos = np.linspace(0.01, 0.44, 3)
    
    list_of_figures = []
    
    for xx, fig_path in zip(x_pos, list_of_figs):
        
        list_of_figures.append(
            Template1.add_figure(figure, [xx, -0.05, 0.22, 1], fig_path)
            )
    
    
    text_ = r"""
$\bf{Conclusions:}$

- Perturbations far from the connecting
  residues indicate interdomain interactions
    
- Retained low $^1$H dispersion in SH4-UD confirm
  these regions remain disordered upon binding.

- Largest perturbations found in $\beta_2$ and
  $\beta_3$ strands and the connecting n-Src
  loop.

- LynA additionally interacts with RT loop.

- Interaction with nSrc and 3$_{10}$ regions
  is very similar in both isoforms.
"""
    
    ax.text(x=0.67, y=0.8, s=text_, **Template1.text_box)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
