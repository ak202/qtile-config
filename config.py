from libqtile.config import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
import subprocess

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),

    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),
        
    Key(
        [mod], "q",
        lazy.layout.flip()
    ),        
                
    Key(
        [mod, "shift"], "q",
        lazy.layout.swap_left()
    ),        

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    
    Key([mod, 'control'], "q", lazy.spawn("audacious -r")),
    Key([mod, 'control'], "e", lazy.spawn("audacious -f")),
    Key([mod, 'shift'], "1", lazy.spawn("xflux -z 02144")),
    Key([mod, 'shift'], "2", lazy.spawn("killall xflux")),
    Key([mod], "e", lazy.spawn("sakura")),
    Key([mod], "c", lazy.spawn("thunar")),
    Key([mod], "x", lazy.spawn("firefox")),
    Key([mod], "z", lazy.spawn("thunderbird")),
    Key([mod, 'shift'], "z", lazy.spawn("eclipse")),
    Key([mod], "m", lazy.spawn("python2 itz_script.py")),
    Key([mod, 'shift'], "x", lazy.spawn("bash ss")),
    Key([mod, "shift"], "j", lazy.layout.grow()),
    Key([mod], "j", lazy.layout.shrink()),  
    Key([mod], "y", lazy.spawn("bash ss")),  

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
]

groups = [
    Group("a"),
    Group("s"), 
    Group("d"), 
    Group("f"), 
    Group("u"),
    Group("i"),
    Group("o"),
    Group("p"), 
]

#groups = [
#    [Group("a"), Group("u")]
#    [Group("s"), Group("i")]
#    [Group("d"), Group("o")]
#    [Group("f"), Group("p")]
#]


for i in range(0,4):
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], groups[i].name, lazy.group[groups[i].name].toscreen())
    )
    keys.append(
        Key([mod, "control"], groups[(i)].name, lazy.group[groups[(i+4)].name].toscreen())
    )
    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, 'shift'], groups[i].name, lazy.window.togroup(groups[i].name))
    )
    keys.append(
        Key([mod, "shift", "control"], groups[i].name, lazy.window.togroup(groups[i+4].name))
    )

dgroups_key_binder = None
dgroups_app_rules = []

layouts = [
    layout.Max(),
    layout.MonadTall(),
    layout.Stack(stacks=2)
]

screens = [
    Screen(
        bottom = bar.Bar(
                    [
                        widget.GroupBox(),
                        widget.Prompt(),
                        widget.WindowName(),
                        widget.TextBox("", name="bg"),
                        widget.TextBox("", name="task"),
                        widget.TextBox("", name="wl"),    
                        widget.TextBox("", name="points"),
                        widget.Systray(),
                        widget.Clock(),
                    ],
                    30,
                ),
    ),
]

main = None
follow_mouse_focus = True
cursor_warp = False
floating_layout = layout.Floating()
mouse = ()
auto_fullscreen = True
widget_defaults = {}

