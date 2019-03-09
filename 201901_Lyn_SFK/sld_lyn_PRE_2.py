from matplotlib import pyplot as plt

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, **kwargs):
    
    Template1.add_suptitle(s="Lyn C3-MTSL in USH3 constructs", ax=ax)
    
    ax1 = Template1.add_figure(figure, [0.5, 0.4, 0.5, 1], "figs/Lyn_constructs_AB_USH3_vs_SH3_para_vs_dia.png")
    # ax2 = Template1.add_figure(figure, [0.09, 0.42, 0.02, 1], "figs/eyes.png")
    
    ax3 = Template1.add_figure(figure, [-.025, 0.2, 0.6, 1], "figs/LynAB_PRE_UD.png")
    
    ax4 = Template1.add_figure(figure, [-.025, -0.25, 0.6, 1], "figs/LynAB_PRE_SH3.png")
    
    ax.set_zorder(4)
    ax1.set_zorder(3)
    ax3.set_zorder(2)
    ax4.set_zorder(1)
    
    # text_ = r"""$\bf{Conclusions:}$

# - SH4-Unique Domains show relaxation enhancement
  # higher than expected for a random-coil model.


# - Disordered regions are in a more compacted state.


# - There are no clear differences between the PRE
  # profiles in the SH3 domain for both LynA and LynB.

  
# - Confirms that SH4 does not interact with the SH3
  # domain and scans the domain's surface equally
  # in both isoforms.
# """
    
    # ax.text(x=0.6, y=0.7, s=text_, **Template1.text_box)
    
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
