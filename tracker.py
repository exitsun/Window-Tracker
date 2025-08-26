from Xlib import X, display
import time

def get_active_window_title():
    d = display.Display()
    root = d.screen().root
    window_id = root.get_full_property(
        d.intern_atom('_NET_ACTIVE_WINDOW'), X.AnyPropertyType
    ).value[0]
    window = d.create_resource_object('window', window_id)
    window_name = window.get_full_property(
        d.intern_atom('_NET_WM_NAME'), 0
    )
    if window_name:
        return window_name.value.decode('utf-8')
    return None

while True:
    print(get_active_window_title())
    time.sleep(1)



