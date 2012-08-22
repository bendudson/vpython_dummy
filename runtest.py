
## Set the logging to catch events
import logging

# Create a custom handler for events
from handler import VisualHandler
h = VisualHandler() # Keep a handle to interrogate later

# Add the handler
log = logging.getLogger('visual')
log.addHandler(h)

## Import the code to run it

import test

## Remove our handler, so no more accidental logs 
log.removeHandler(h)

## Inspect events

print("Code created the following visual objects:")
for name in h.created:
    print("\t%s : %d" % (name, len(h.created[name])))

