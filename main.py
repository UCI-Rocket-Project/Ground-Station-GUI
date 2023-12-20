import click
import clickhouse_connect as clickhouse
from clickhouse_connect.driver.exceptions import OperationalError,  DatabaseError
import os
import sys
import reactivex as rx
import time
'''
TODO(aashay):. ~/.virtualenvs/ucirp/bin/activate.fish
'''

DEBUG = False
dev_dbg_heartbeat = False
dev_dbg_mavlink = True
dev_dbg_clickhosue = False

def mavlink_env_setup():
    os.environ['MAVLINK20'] = '1'
    os.environ['MAVLINK_DIALECT'] = 'ucirp'
    sys.path.append('./mavlink')

def is_prd(DEBUG, flag):
    return not (DEBUG and flag)

def is_dbg(DEBUG, flag):
    return DEBUG and flag

def dbgln(DEBUG, flag, s):
    if is_dbg(DEBUG, flag):
        click.echo(s)


mavlink_env_setup()
import pymavlink as mavlink
from pymavlink import mavutil

'''
Options are also acsessbile via envvars.
- Everything is prefixed with UCIRP
- So format should be UCIRP_$COMMAND_$VAR
See: https://click.palletsprojects.com/en/8.1.x/options/#values-from-environment-variables
'''

class LinkStatus:
    def __init__(self):
        self.clickhouse = (None, None, False)
        self.ecus = []
        self.gui_backends = []
link_status = LinkStatus()

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    if debug:
        click.echo("Started ucirp in debug mode")

def send_sys_status(conn):
    '''
    Tells everyone that we are alive
    '''
    def _send_sys_status(x):
        conn.mav.sys_status_send(
                mavutil.mavlink.MAV_SYS_STATUS_SENSOR_3D_GYRO,
                mavutil.mavlink.MAV_SYS_STATUS_SENSOR_3D_GYRO,
                mavutil.mavlink.MAV_SYS_STATUS_SENSOR_3D_GYRO,
                10,
                12000,
                -1,
                70,
                10,
                0,
                0,
                0,
                0,
                0
                )
    return _send_sys_status

def send_heartbeat(conn):
    '''
    Tells everyone that we are alive
    '''
    def _send_heartbeat(x):
        conn.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ROCKET,
                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 
                                mavutil.mavlink.MAV_MODE_TEST_DISARMED, 
                                0, 
                                mavutil.mavlink.MAV_STATE_UNINIT)
    return _send_heartbeat

def call_recv(conn):
    '''
    Necessary to make sure that connections are not missed.
    '''
    def _call_recv(x):
        # TODO: Should not be ignoring messages
        conn.recv()
    return _call_recv

@click.command()
@click.option('--sensor-data', default='sensors.rp_mav')
@click.option('--ecu-port', default=10000)
@click.option('--ecu-host', default='localhost')
def ecu_emulator(sensor_data, ecu_port, ecu_host):
    click.echo("Hello! I am a rocket. :-)")
    conn = mavutil.mavlink_connection(f'udpin:{ecu_host}:{ecu_port}')
    rx.timer(0.0, 5.0).subscribe(on_next = send_heartbeat(conn))
    rx.timer(0.0, 1.0).subscribe(on_next = call_recv(conn))
    rx.timer(0.0, 31.0).subscribe(on_next = send_sys_status(conn))
    while  True:
        # Let the main thread sleep
        x = input()


@click.command()
@click.option('--ecu-port', default=8888)
@click.option('--ecu-host', default='192.168.0.8')
@click.option('--db-port',  default=8080)
@click.option('--db-host', default='192.168.0.7')
@click.option('--db-database',  default='default')
@click.option('--dev-no-db', default=False)
@click.pass_context
def db_server(ctx, ecu_port, ecu_host, db_port, db_host, db_database, dev_no_db):
    click.echo('Starting splitter for GUI/DB')
    click.echo(f'Expect ECU at {ecu_host}:{ecu_port}')
    click.echo(f'Expect ClickhouseDB at {db_host}:{db_port}')
    DEBUG = True if ctx.obj['DEBUG'] else False
    click.echo(f"DEBUG: {DEBUG}")
    click.echo(f"NoDB: {dev_no_db}")

    if is_prd(DEBUG, dev_no_db):
        try:
            dbgln(DEBUG, dev_dbg_clickhouse, "Connecting to Clickhouse")
            client = clickhouse.get_client(host=db_host,  port=db_port, database=db_database, connect_timeout=1)
            link_status.clickhouse = (db_host, db_port, True)
            dbgln(DEBUG, dev_dbg_clickhouse, "Connected to Clickhouse")
            click.echo(f'Clickhouse {client.server_version}')
        except OperationalError as e:
            click.echo("Could not connect to clickhouse")
            click.echo(type(e))
            click.echo(e)
            exit(1)
        except DatabaseError as e:
            click.echo(f"Unknown server running on {db_host}:{db_port}")
            click.echo(type(e))
            click.echo(e)

    last_ecu_heartbeat = None
    last_ecu_message = None
    dbgln(DEBUG, dev_dbg_mavlink, "Connecting to ECU ")
    conn = mavutil.mavlink_connection(f'udpout:{ecu_host}:{ecu_port}')
    link_status.ecus.append((ecu_host, ecu_port))
    dbgln(DEBUG, dev_dbg_mavlink, "Connected to ECU ")
    rx.timer(0.0, 5.0).subscribe(on_next = send_heartbeat(conn))
    while  True:
        # Let the main thread sleep
        try:
            x = conn.recv_msg()
            if x is not None:
                last_ecu_message = x._timestamp
                print(x)
                if x.id == mavutil.mavlink.MAVLINK_MSG_ID_HEARTBEAT:
                    dbgln(DEBUG, dev_dbg_heartbeat, "Heartbeat'd")
                    last_ecu_heartbeat = x._timestamp
                x = None
        except TimeoutError as ti:
            print(type(ti))
            print(ti)
            print("ECU timed out")
            exit(1)
        # RuntimeError from mavlogfile?
        # if last_ecu_message is not None and last_ecu_message - time.



cli.add_command(db_server)
cli.add_command(ecu_emulator)

if __name__ == '__main__':
    cli(auto_envvar_prefix='UCIRP')

