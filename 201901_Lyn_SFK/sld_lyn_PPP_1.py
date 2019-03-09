from matplotlib import pyplot as plt

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, **kwargs):
    
    Template1.add_suptitle(s="Lyn USH3 vs PPP", ax=ax)
    
    ax1 = Template1.add_figure(figure, [-0.05, 0.15, 1, 0.7], "figs/SRC_inkspace_UD.png")
    
    
    # ax1 = Template1.add_figure(figure, [0.01, 0.42, 0.35, 1], "figs/Lyn_constructs_AB_USH3_PPP.png")
    # ax3 = Template1.add_figure(figure, [0.01, 0.19, 0.5, 1], "figs/LynAB_vs_PPP_CSPs.png")
    
    # ax1.set_zorder(3)
    # ax3.set_zorder(1)
    
    # ax2 = Template1.add_figure(figure, [0.01, -0.06, 0.35, 1], "figs/Lyn_constructs_AB_USH3_PPP_vs_SH3-PPP.png")
    # ax4 = Template1.add_figure(figure, [0.01, -0.29, 0.5, 1], "figs/USH3_SH3_vs_PPP_CSPs.png")
    
    # ax2.set_zorder(1)
    # ax4.set_zorder(1)
    
    # ax.set_zorder(2)
    
    # text_ = r"""$\bf{Conclusions:}$

# - Binding of PPP affects the regions where
  # UD binds the SH3 domain.
  
# - As expected, PPP displaces the Unique Domain
  # from the interation.

# - However, UD-SH3 interaction is partially maintained
  # for both LynA and LynB in the nSrc and 3$_10$ region.

# - Interaction between UD and the RT loop is completely
  # abolished.

# - In the presence of saturating conditions of PPP
  # LynA and LynB behave the same.
# """
    
    # ax.text(x=0.6, y=0.8, s=text_, **Template1.text_box)
    
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")

