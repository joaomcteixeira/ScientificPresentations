import numpy as np

import matplotlib.pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.collections import PatchCollection

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(ax, "Brief highligh on Src's Unique Domain")
    
    path = "figs/photo_mpons.png"
    ax0 = Template1.add_figure(figure, [0.88, 0.35, 0.1, 1], path)
    
    ax1 = Template1.add_figure(figure, [-0.05, 0.15, 1, 0.7], "figs/SRC_inkspace_classical.png")
    
    rect = mpatches.Rectangle((0.04, 0.04), 0.9, 0.9, ec="none",
        facecolor="white", alpha=0.95)
    
    ax.add_artist(rect)
    
    ax0.set_zorder(10)
    ax1.set_zorder(1)
    ax.set_zorder(2)
    
    # add titulares
    list_of_fig_paths = [
        "figs/paper_2009.png",
        "figs/paper_2013_1.png",
        "figs/paper_2013_2.png",
        "figs/paper_2015.png",
        "figs/paper_2017.png",
        ]
    
    y_pos_array = np.linspace(0.3, -0.2, 6)
    
    list_of_figures = []
    
    for y_pos, fig_path in zip(y_pos_array, list_of_fig_paths):
        
        list_of_figures.append(
            Template1.add_figure_border(figure, [0.03, y_pos, 0.4, 1], fig_path)
            )
        
        
    for layer_level, ax_i in enumerate(list_of_figures, start=3):
        
        # ax_i.axis("on")
        
        # ax_i.tick_params(
            # axis='both',
            # which='both',
            # bottom=False,
            # left=False,
            # labelbottom=False,
            # labelleft=False,
            # )
        
        ax_i.set_zorder(layer_level)
    
    # adds reference list
    list_of_references = [
        "· Pérez, Y., et.al (2009). Journal of Molecular Biology, 391(1), 136–148.",
        "· Pérez, Y., et.al. (2013). Scientific Reports, 3, 1295.",
        "· Amata, I., et.al. (2013). Chembiochem, 14(14), 1820–1827.",
        "· Maffei, M., et. al. (2015). Structure, 893–902.",
        "· Arbesú, M., et.al. (2017). Structure, 25(4), 630–640.e4.",
        ]
    
    bullet_count = np.linspace(0.94, 0.6, 10)
    
    for y_pos, ref in zip(bullet_count, list_of_references):
    
        ax.text(y=y_pos, x=0.46, s=ref, **Template1.references_props)
    
    
    # add text box
    # rect2 = mpatches.FancyBboxPatch((0.5, 0.1), 0.45, 0.5, boxstyle=mpatches.BoxStyle("Round", pad=0.02))
    # patches = [rect2]
    # collection = PatchCollection(patches, facecolor="white", edgecolor="black", linewidth=1)
    # ax.add_collection(collection)
    
    # text_ = r"""
# $\bf{Summary:}$

# - Members of the Src family of kinases (SFK) share well-conserved sequence
  # features involving aromatic residues in their Unique domains.

# - SFK's UD sequences encodes specificity to input signals.

# - Shared mechanism among SFK's connecting disordered and structured domains
  # and SFK's kinase activity.

# """

    text_ = r"""
$\bf{Evolutionary\ conservation\ of\ implicit\ features\ in}$
  $\bf{SFKs\ Unique\ Domain}$
  
  - specificity to input signals

  - Proline - Phenylalanine combination

"""
    
    ax.text(x=0.45, y=0.55, s=text_, **Template1.text_box)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
