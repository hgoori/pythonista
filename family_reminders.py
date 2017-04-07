import reminders
import appex, ui

def todo_list():
    todo = reminders.get_reminders(completed=False)

    l = list()
    for r in todo:
        if r.notes is None:
            continue
            
        if r.notes.lower() != 'mkr':
            continue

        l.append(r.title)

    return l

def main():
    tl = todo_list()

    tv = ui.TextView(font=('Menlo', 16),
        alignment=ui.ALIGN_CENTER,
        editable=False,
        selectable=False)
    tv.text = '\n'.join(tl)
    tv.background_color = (0.85, 0.85, 0.85, 0.6)

    appex.set_widget_view(tv)

if __name__ == '__main__':
    main()
