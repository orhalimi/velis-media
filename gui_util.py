text_label = None


def update_ui_message(message=""):
    if text_label:
        text_label.set(message)


def set_label(label):
    global text_label
    text_label = label
