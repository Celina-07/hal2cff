# +
import ipywidgets as widgets
from IPython.display import display, display_html, Markdown

from hal2cff import hal2cff
# -

# # hal2cff
#
# Turn a [HAL](https://hal.archives-ouvertes.fr) URL into a draft [CITATION.cff](https://citation-file-format.github.io/) file.

url = widgets.Textarea(value="https://hal.archives-ouvertes.fr/hal-01361430v1",placeholder="Type you HAL url",description ="HAL url")
button = button = widgets.Button(
    description='Search',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    icon='check' # (FontAwesome names without the `fa-` prefix)
)
progress_bar = widgets.FloatProgress(
    value=0,
    min=0,
    max=10.0,
    description='Loading:',
    bar_style='info',
    style={'bar_color': '#ffff00'},
    orientation='horizontal',
    layout=widgets.Layout(visibility="hidden")
)

display(widgets.HBox([url, button, progress_bar]))
output = widgets.Output()
display(output)

def generate_cff(_):
    with output:
        output.clear_output()
        progress_bar.layout = widgets.Layout(visibility="visible")
        try:
            result = hal2cff(url.value)
            result_pre = f"<pre>{result}</pre>"
            display_html(result_pre, raw=True)
        finally:
            progress_bar.layout = widgets.Layout(visibility="visible")
            progress_bar.value = 10
            progress_bar.description = "Done !"
            

button.on_click(generate_cff)


