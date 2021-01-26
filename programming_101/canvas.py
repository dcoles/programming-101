import json
import uuid

from IPython.display import display, HTML
from google.colab import output


class Canvas:
    def __init__(self, width, height):
        self.id = uuid.uuid4()

        display(HTML(f'''
            <canvas id="canvas_{ self.id.hex }" width="{ "%d" % width }" height="{ "%d" % height }"></canvas>    
            <script>
                let canvas_ctx2d_{ self.id.hex } = canvas_{ self.id.hex }.getContext("2d");
            </script>
        '''))

    def _eval_this(self, js):
        return output.eval_js(f'canvas_{ self.id.hex }.{ js }')

    def _eval_context2d(self, js):
        return output.eval_js(f'canvas_ctx2d_{ self.id.hex }.{ js }')

    @property
    def width(self):
        return self._eval_this('width')

    @property
    def height(self):
        return self._eval_this('height')

    @property
    def line_width(self):
        return self._eval_context2d('lineWidth')

    @line_width.setter
    def line_width(self, width):
        self._eval_context2d(f'lineWidth = { json.dumps(width) }')

    @property
    def fill_style(self):
        return self._eval_context2d('fillStyle')

    @fill_style.setter
    def fill_style(self, style):
        self._eval_context2d(f'fillStyle = { json.dumps(style) }')

    @property
    def stroke_style(self):
        return self._eval_context2d('strokeStyle')

    @stroke_style.setter
    def stroke_style(self, style):
        self._eval_context2d(f'strokeStyle = { json.dumps(style) }')

    def stroke_rect(self, x, y, width, height):
        self._eval_context2d(f'strokeRect({ json.dumps(x) }, { json.dumps(y) }, { json.dumps(width) }, { json.dumps(height) })')

    def fill_rect(self, x, y, width, height):
        self._eval_context2d(f'fillRect({ json.dumps(x) }, { json.dumps(y) }, { json.dumps(width) }, { json.dumps(height) })')

    def move_to(self, x, y):
        self._eval_context2d(f'moveTo({ json.dumps(x) }, { json.dumps(y) })')

    def line_to(self, x, y):
        self._eval_context2d(f'lineTo({ json.dumps(x) }, { json.dumps(y) })')

    def begin_path(self):
        self._eval_context2d('beginPath()')

    def close_path(self):
        self._eval_context2d('closePath()')

    def stroke(self):
        self._eval_context2d('stroke()')

    def fill(self, fill_rule=None):
        if fill_rule:
            self._eval_context2d(f'fill({ json.dumps(fill_rule) })')
        else:
            self._eval_context2d('fill()')
