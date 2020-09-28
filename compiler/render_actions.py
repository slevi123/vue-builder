

def default_render_action(codeblock):
    codeblock.rendered = f"\t{codeblock.name}: {{\n\t\t{codeblock.content}\n\t}}"


def default_render_action_visible(codeblock):
    codeblock.rendered = f"\n\t{codeblock.name}: {{{codeblock.content}}}"


def default_render_action_min(codeblock):
    codeblock.rendered = f"{codeblock.name}: {{{codeblock.content}}}"
