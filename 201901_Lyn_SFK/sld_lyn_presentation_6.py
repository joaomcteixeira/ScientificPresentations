import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(ax=ax, s="The Lyn case")
    
    list_of_figures = [
        Template1.add_figure(figure, [0, 0.6, 0.3, 0.3], "figs/SFKs_tree.png"),
        Template1.add_figure(figure, [0.37, 0.39, 0.6, 1], "figs/LynAB_general_construct.png"),
        Template1.add_figure(figure, [0.04, -.1, 0.9, 0.4], "figs/Lyn_FASTA_2.png"),
        ]
    
    ax.text(x=0.1, y=0.4, va="center", ha="center", s="LynA", color=Template1.color, fontsize=20, zorder=1)
    ax.text(x=0.24, y=0.4, va="center", ha="center", s="LynB", color="red", fontsize=20, zorder=1)
    
    ax.arrow(x=0.165, y=0.6, dx=-0.05, dy=-0.15, head_length=0.015, head_width=0.01, color="black")
    ax.arrow(x=0.165, y=0.6, dx=0.05, dy=-0.15, head_length=0.015, head_width=0.01, color="black")
    
    # rect = mpatches.Rectangle((0.54, 0.5), 0.45, 0.2, ec="none", facecolor="white", alpha=0.7)
    # ax.add_artist(rect)
    # ax.set_zorder(2)
    
    list_of_figures[1].set_zorder(1)
    
    text_ = r"""$\bf{Known\ Biological\ Implications:}$
- Lyn mainly expressed in hematopoietic cells
- Direct relation with immunological responses
- LynB -> alternative splicing
  - 21 a.a. insert at UD
- Correct LynA::LynB ratio required for normalized responses. 
- ONLY LynA promotes invasion in Breast Cancer (overexpression)
- STRUCTURAL origin remains obscure.
"""
    ax.text(
        x=0.4,
        y=0.74,
        s=text_,
        color="black",
        fontname=Template1.font,
        linespacing=2,
        va="top",
        ha="left",
        fontsize=14,
        )
    
    ax.text(
        x=0.4,
        y=0.24,
        s=(
            "Alvarez-Errico, D., et.al. (2010). The Journal of Immunology, 184(9), 5000–5008.\n"
            "Tornillo, G., et. al. (2018). Cell Reports, 3674–3692."
            ),
        **Template1.references_props
        )
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
