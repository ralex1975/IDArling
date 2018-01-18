import idc

from events import Event


class UndefinedEvent(Event):
    _type = 'undefined'

    def __init__(self, ea):
        super(UndefinedEvent, self).__init__()
        self['ea'] = ea

    def __call__(self):
        idc.del_items(self['ea'])
