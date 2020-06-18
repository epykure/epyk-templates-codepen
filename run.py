
import config

import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, "..", "epyk-ui"))

folder = "stackblitz"
script_name = "codepen_buttons"

__import__("%s.%s" % (folder, script_name))
