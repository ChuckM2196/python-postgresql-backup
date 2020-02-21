import subprocess
import sys

'''
Grabs backup info from postgreSQL as url, pipes stdout to file instead of screen
'''
def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print (f"Error: {err}")
        sys.exit(1)

def dump_file_name(url, timestamp='None'):
    db_name = url.split("/")[-1]
    d_name = db_name.split("?")[0]
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db.name}.sql"
