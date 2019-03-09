import matplotlib.pyplot as plt


from templates import Template1


@Template1.template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    Template1.add_suptitle(ax=ax, s="The Lyn case")
    
    list_of_figures = [
        Template1.add_figure(figure, [0, 0.6, 0.3, 0.3], "figs/SFKs_tree.png"),
        Template1.add_figure(figure, [0.37, 0.39, 0.6, 1], "figs/SFKs_general_construct.png"),
        ]
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
