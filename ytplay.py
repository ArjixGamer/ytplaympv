import subprocess, os, sys
from stream_redirect import Redirect
query = sys.argv[1:]
r = Redirect(stdout=True, stderr=True)
with r:
	subprocess.run(f'youtube-dl "ytsearch1: {query}" -f best -g')

video_link = r.stdout
command = f'mpv "{video_link}"'
os.system(command)