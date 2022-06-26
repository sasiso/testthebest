identifiers = [
    dict(vid=0x30C4, pid=0x03EA),  # cerberus production
    dict(vid=0x30C4, pid=0x03EB),  # cerberus developer
    dict(vid=0x30C4, pid=0x03EC),  # cerberus dev+msc
    dict(name="Lumos Camera Reader"),
]
def f(vid=0,pid=0, name=None):
    print(vid,pid,name)
for kwargs in identifiers:
    f(**kwargs)
