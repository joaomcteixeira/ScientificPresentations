
from matplotlib import pyplot as plt

from templates import Template1


@Template1.main_title_template
def slide(page_number, figure=None, ax=None, title="", **kwargs):
    
    text_ = """What about other SFKs?

The Lyn case.
"""
    
    Template1.add_maintitle(s=text_, ax=ax)
    
    return figure, ax


if __name__ == "__main__":
    
    slide(1)
    
    plt.savefig("slide.pdf")
