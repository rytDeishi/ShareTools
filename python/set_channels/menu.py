import nuke

import set_channels

toolbar = nuke.menu('Nuke').addMenu('rd_tools')
toolbar.addCommand('Set Channels', 'set_channels.set_channels()', 'alt+shift+v')
