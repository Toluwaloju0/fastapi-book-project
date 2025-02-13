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
        c.run('scp -i ~/.ssh/id_rsa -r ./* ubuntu@107.23.103.1:/tmp/fast_api')
        con.run('cd /tmp/fast_api && pip3 install -r requirements.txt')
        con.run('sudo pkill fastapi && sudo pkill uvicorn')
        con.run('cd /tmp/fast_api && fastapi run')