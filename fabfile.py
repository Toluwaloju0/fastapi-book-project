#!/usr/bin/env python3
"""A fabfile to set up the server"""

from fabric import Connection, task

@task
def deploy(c):
    """Deploy app to the server"""

    with Connection(
        host='54.86.69.72',
        user='ubuntu',
        connect_kwargs={
            "key_filename": '~/.ssh/id_rsa'
        }
    ) as con:
        con.run('mkdir -p /tmp/fast_api')
        c.run('tar -czvf archive.tar.gz ./*')
        con.put('archive.tar.gz', remote='/tmp/fast_api')
        con.run('cd /tmp/fast_api && tar --overwrite -xzvf archive.tar.gz && pip3 install -r requirements.txt')
        c.run('rm -f archive.tar.gz')
        con.run('rm -f /tmp/fast_api/archive.tar.gz && sudo pkill fastapi && sudo pkill uvicorn')
        con.run('cd /tmp/fast_api && fastapi run')