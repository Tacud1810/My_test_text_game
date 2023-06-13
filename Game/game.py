"""
Modul reprezentuje hru.
"""
from . import action
from . import world
print(f"===== Modul {__name__} ===== START")
####################################################################################


def execute_command(command: str) ->str:
    message = action.execute_command(command)
    return message

####################################################################################
print(f"===== Modul {__name__} ===== STOP")