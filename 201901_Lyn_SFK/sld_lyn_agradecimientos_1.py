from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.collections import PatchCollection

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, **kwargs):
    
    Template1.add_suptitle(s="Acknowledgements", ax=ax)
    
    path = "figs/photo_mpons.png"
    ax1 = Template1.add_figure(figure, [0.4, 0.35, 0.1, 1], path)
    
    path = "figs/UB_logo_home_nou.png"
    ax3 = Template1.add_figure(figure, [0.14, 0.8, 1, 0.1], path)
    
    path = "figs/photo_wiktor.png"
    ax2 = Template1.add_figure(figure, [0.4, 0.1, 0.1, 1], path)
    
    path = "figs/wiktor_group.png"
    ax4 = Template1.add_figure(figure, [0.18, 0.56, 1, 0.07], path)
    
    
    text_ = r"""$\bf{Miquel\ Pons'\ Lab:}$

- Héctor Fuentes (Msc.)
- Stase Bielskute (Visiting Student)
- Marga Gairi (NMR Facility)
- Miquel Pons

$\bf{Kozminski's\ Lab:}$

- Disordered Region assignments
- Szymon Zerko
- Wiktor Kozminski

"""
    
    ax.text(x=0.1, y=0.9, s=text_, **Template1.text_box)
    
    
    text_ = r"""$\bf{Some\ data:}$

- +100 NMR experiments, including assignment and
  interaction assays.

"""
    
    ax.text(x=0.1, y=0.4, s=text_, **Template1.text_box)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")


