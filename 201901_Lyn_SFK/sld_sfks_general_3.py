import matplotlib.pyplot as plt

from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(ax, "SFKs and their Unique Domain")
    
    ax1 = Template1.add_figure(figure, [0.2, 0.2, 0.6, 0.6], "figs/src_scheme.png")
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
