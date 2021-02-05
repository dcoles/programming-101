import uuid

from ipykernel.comm import Comm
from IPython.display import display, HTML


class Canvas:
    def __init__(self, width, height):
        self.id = uuid.uuid4()
        self.width = width
        self.height = height

        context = {'id': self.id.hex, 'width': width, 'height': height}
        display(HTML('''
            <canvas id="canvas_%(id)s" width="%(width)d" height="%(height)d"></canvas>
            <script>
                Jupyter.notebook.kernel.comm_manager.register_target("canvas_%(id)s", (comm, msg) => {
                    const ctx = canvas_%(id)s.getContext("2d");

                    comm.on_msg((msg) => {
                        const eventName = msg.content.data[0];
                        const eventData = msg.content.data[1];
                        switch (eventName) {
                            // Properties
                            case 'lineWidth':
                            case 'strokeStyle':
                            case 'fillStyle':
                                ctx[eventName] = eventData[0];
                                break;

                            // Methods
                            case 'beginPath':
                            case 'lineTo':
                            case 'moveTo':
                            case 'stroke':
                            case 'fill':
                                ctx[eventName].apply(ctx, eventData);
                                break;

                            default:
                                console.log('Unknown event: ' + eventName);
                        }
                    });
                });
            </script>
        ''' % context))

        self.comm = Comm(f'canvas_{self.id.hex}')

    def emit(self, event_name, *args):
        self.comm.send([event_name, *args])

    @property
    def line_width(self):
        return NotImplemeted

    @line_width.setter
    def line_width(self, width):
        self.emit('lineWidth', [width])

    @property
    def fill_style(self):
        return NotImplemeted

    @fill_style.setter
    def fill_style(self, style):
        self.emit('fillStyle', [style])

    @property
    def stroke_style(self):
        return NotImplemeted

    @stroke_style.setter
    def stroke_style(self, style):
        self.emit('strokeStyle', [style])

    def stroke_rect(self, x, y, width, height):
        self.emit('strokeRect', [x, y, width, height])

    def fill_rect(self, x, y, width, height):
        self.emit('fillRect', [x, y, width, height])

    def move_to(self, x, y):
        self.emit('moveTo', [x, y])

    def line_to(self, x, y):
        self.emit('lineTo', [x, y])

    def begin_path(self):
        self.emit('beginPath')

    def close_path(self):
        self.emit('closePath')

    def stroke(self):
        self.emit('stroke')

    def fill(self, fill_rule=None):
        self.emit('fill', [fill_rule] if fill_rule is not None else [])
