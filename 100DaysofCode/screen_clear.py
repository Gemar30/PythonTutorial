import os
from time import sleep
# The screen clear function
def clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')

# wait for 5 seconds to clear screen
sleep(3)
# now call function we defined above
clear()