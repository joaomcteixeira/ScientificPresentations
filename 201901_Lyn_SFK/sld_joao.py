from matplotlib import pyplot as plt
# from matplotlib import patches as mpatches
# from matplotlib.collections import PatchCollection

from templates import Template1


@Template1.page0
def slide(page_number, figure=None, ax=None, **kwargs):
    
    # coimbra
    
    ax1 = Template1.add_figure(
        figure,
        [0.01, 0.65, 0.3, 0.3],
        "figs/coimbra.png"
        )
    
    ax.text(
        x=0.01,
        y=0.5,
        s="University of Coimbra,\nPortugal",
        **Template1.big_title_props,
        )
    
    ax.text(
        x=0.01,
        y=0.48,
        s=(
            "Biochemistry,\n"
            "Contrast agents - protein interactions\n"
            "Saturation Transfer Difference (STD) NMR\n"
            "Dr. Carlos Geraldes"
            ),
        **Template1.text_box
        )
    

    
    # florence
    ax2 = Template1.add_figure(
        figure,
        [0.35, 0.5, 0.3, 0.3],
        "figs/florence.jpg"
        )
    
    ax.text(
        x=0.35,
        y=0.4,
        s="CERM, Florence, Italy",
        **Template1.big_title_props,
        )
    
    ax.text(
        x=0.35,
        y=0.38,
        s=(
            "PhD,\n"
            "MMP driven collagenolysis\n"
            "Multidomain dynamics, paramagnetic NMR\n"
            "Dr. Claudio Luchinat"
            ),
        **Template1.text_box
        )
    
    # barcelona
    ax3 = Template1.add_figure(
        figure,
        [0.68, 0.3, 0.3, 0.3],
        "figs/barcelona.jpeg"
        )
    
    ax.text(
        x=0.68,
        y=0.2,
        s="BioNMR Group, Barcelona",
        **Template1.big_title_props,
        )
    
    ax.text(
        x=0.68,
        y=0.18,
        s=(
            "Postdoc,\n"
            "Signaling pathways, ...\n" 
            "Structural biology, IDPs, Farseer-NMR"
            "\n"
            "Dr. Miquel Pons"
            ),
        **Template1.text_box
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
        linespacing=1.5,
        )
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")

