#!/usr/bin/env python3
"""A fabfile to set up the server"""

from fabric import Connection, task

@task
def deploy(c):
    """Deploy app to the server"""

    with Connection(
        host='107.23.103.1',
        user='ubuntu',
        connect_kwargs={
            "key_filename": 'id_rsa'
        }
    ) as con:
        con.run('mkdir -p /tmp/fast_api')
        c.run('tar -czvf archive.tar.gz ./*')
        con.put('archive.tar.gz', remote='/tmp/fast_api')
        con.run('cd /tmp/fast_api && tar --overwrite -xzvf archive.tar.gz && pip3 install -r requirements.txt')
        con.run('sudo pkill fastapi && sudo pkill uvicorn')
        con.run('cd /tmp/fast_api && fastapi run')