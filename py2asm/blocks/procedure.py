from py2asm.blocks.block import Block


class Procedure(Block):
    template = """{name} proc
{children}
    RET
{name} endp"""

    def __init__(self, name):
        self.name = name

        super().__init__()

    def render(self):
        return self.template.format(
            name=self.name,
            children=self.render_children()
        )
