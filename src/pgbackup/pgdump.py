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
