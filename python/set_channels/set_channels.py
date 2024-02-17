import nuke

def set_channels():

    ch = nuke.selectedNode().channels()
    ch_list = [item.split('.')[0] for item in ch]

    ch = []

    for i in ch_list:
        if i not in ch:
            ch.append(i)

    ch = ' '.join(ch)

    panel = nuke.Panel('channels')
    panel.addEnumerationPulldown('channels', ch)

    if not panel.show():
        return
    
    channels = panel.value("channels")
    
    for shuffle in nuke.selectedNodes('Shuffle2'):
        shuffle['in1'].setValue(channels)
        shuffle['label'].setValue('[value in1]')


