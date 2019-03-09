import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(s="Src Family Kinases", ax=ax)
    
    # text_ = r"""$\bf{Brief\ on\ SFKs:}$

# - SFK: Src Family Kinases

# - $\bf{Src}$, Yes, Fyn, Fgr, $\bf{Lyn}$, Hck, Lck, Blk

# - $\bf{Membrane - associated}$, $\bf{non - receptor}$ tyrosine kinases

# - Signaling intermediaries: cell proliferation, differentiation, apoptosis,
  # migration, and metabolism.

# - v-Src one of the first proteins associated with
  # oncogenesis (Rous sarcome virus).

# - Yet, we still lack complete understanding of c-Src role in
  # tumor development.
    # """
    
    # ax.text(x=0.01, y=0.95, s=text_, **Template1.text_box)
    
    # text_ = r"""$\bf{Structural\ features\ of\ SFKs:}$

# - All SFKs share the same motif:
    # - Disordered region
    # - SH3 domain (regulatory)
    # - SH2 domain (regulatory)
    # - SH1 domain (kinase)
    
    # - High homology in SH1-SH3 domains
    # - Very low sequence homology in Unique Domains

# - Activation / Inhibition:

    # - Phosphorylation of Tyr-530 triggers inter-domain compaction
    # """
    
    # ax.text(x=0.51, y=0.95, s=text_, **Template1.text_box)
    
    ax1 = Template1.add_figure(figure, [-0.05, 0.15, 1, 0.7], "figs/SRC_inkspace_classical.png")
    
    # ax1.set_zorder(1)
    # ax.set_zorder(2)
    
    circle1 = mpatches.Ellipse((0.6, 0.64), 0.15, 0.2, color='r', alpha=0.3)
    
    ax.add_artist(circle1)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")

