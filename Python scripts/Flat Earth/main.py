""" Interface for a globe earth calculator """
import tkinter
import handler
import fe_imperial as imp


def calculate():
    """ Display results """
    reset_results()
    try:
        if OBS_HEIGHT.get():
            obs_height = float(OBS_HEIGHT.get())
            ANGLE.result['text'] = round(imp.angle(obs_height), 2)
            HORIZON.result['text'] = round(imp.horizon(obs_height), 2)
            if OBJ_HEIGHT.get() and DISTANCE.get():
                obj_height = float(OBJ_HEIGHT.get())
                distance = float(DISTANCE.get())
                visible, percent, hidden = imp.visible(obs_height, obj_height, distance)
                VISIBLE.result['text'] = round(visible, 2)
                VIS_PERCENTAGE.result['text'] = round(percent, 2)
                HIDDEN.result['text'] = round(hidden, 2)
                if PERCENTAGE.get():
                    percentage = float(PERCENTAGE.get())
                    angle = imp.refraction(obs_height, obj_height, distance, percentage)
                    REFRACTION.result['text'] = round(angle, 2)
    except ValueError:
        ERROR['text'] = 'All fields must have\nnumerical values'


def reset_results():
    """ Clear answer to previous queries """
    ANGLE.result['text'] = ''
    HORIZON.result['text'] = ''
    VISIBLE.result['text'] = ''
    HIDDEN.result['text'] = ''
    REFRACTION.result['text'] = ''
    ERROR['text'] = ''


WINDOW = tkinter.Tk()
WINDOW.iconify()
WINDOW.config(padx=16, pady=16, bg='white')
WINDOW.title('Globe Earth calculator')
WINDOW.bind('<Return>', lambda key: calculate())
WINDOW.minsize(640, 240)

# IMPERIAL
CONFIG = {
    'label': {
        'padx': 4,
        'pady': 4,
        'bg': WINDOW['bg'],
    }


}
OBS_HEIGHT = handler.Field(WINDOW, 'Observer height', **CONFIG)
OBS_HEIGHT.grid(row=0)

OBJ_HEIGHT = handler.Field(WINDOW, 'Object height', **CONFIG)
OBJ_HEIGHT.grid(row=1)

DISTANCE = handler.Field(WINDOW, 'Distance', **CONFIG)
DISTANCE.grid(row=2)

PERCENTAGE = handler.Field(WINDOW, 'Percentage', **CONFIG)
PERCENTAGE.grid(row=3)

ERROR = tkinter.Label(WINDOW, fg='#ff3f1f', **CONFIG['label'])
ERROR.grid(row=5, column=0)

SEP = tkinter.Label(WINDOW, padx=16, bg=WINDOW['bg'])
SEP.grid(column=2)

ANGLE = handler.Result(WINDOW, text='Angular drop: ', unit='°', **CONFIG)
ANGLE.grid(row=0, column=3)

HORIZON = handler.Result(WINDOW, text='Distance to horizon: ', unit='mi', **CONFIG)
HORIZON.grid(row=1, column=3)

VISIBLE = handler.Result(WINDOW, text='Visible: ', unit='ft', **CONFIG)
VISIBLE.grid(row=2, column=3)

VIS_PERCENTAGE = handler.Result(WINDOW, text='Percentage: ', unit='%', **CONFIG)
VIS_PERCENTAGE.grid(row=3, column=3)

HIDDEN = handler.Result(WINDOW, text='Hidden: ', unit='ft', **CONFIG)
HIDDEN.grid(row=4, column=3)

REFRACTION = handler.Result(WINDOW, text='Refraction needed: ', unit='°', **CONFIG)
REFRACTION.grid(row=5, column=3)

CALCULATE = tkinter.Button(
    WINDOW,
    text='Calculate',
    command=calculate
)
CALCULATE.grid(row=5, column=1)

WINDOW.mainloop()
