"""
Modul action má na starosti zpracování příkazů.
"""

print(f"===== Modul {__name__} ===== START")
####################################################################################
is_active = False  # hra čeká na spuštění

_NAME_2_ACTION = {

}


def execute_command(command: str) -> str:
	command = command.strip()
	if command == '':
		return _execute_empty_command()
	elif is_active:
		return _execute_standard_command()
	else:
		return f("Prvním příkazem není startovací příkaz.\n"
		         "Hru, která neběží, je možné spustit pouze strtovacím příkazem.")


def _execute_empty_command() -> str:
	global is_active
	if is_active:
		return f"Prázdný příkaz lze použít pouze pro start hry."
	else:
		is_active = True
		_initialize()
		return f"Vítejte!\nToto je příběh o Červené Karkulce, babičce a vlkovi.\n" \
		       f"Svými příkazy řídíte Karkulku, aby donesla věci babičce.\n" \
		       f"Nebudete-li si vědět rady, zadejte znak ?."


def _execute_standard_command(command: str) -> str:
	words = command.lower().split()
	action_name = words[0]
	try:
		action = _NAME_2_ACTION[action_name]
	except KeyError:
		return f"Tento příkaz neznám: {action_name}"
	return action.execute(words)


def _initialize() -> None:
	pass


####################################################################################
print(f"===== Modul {__name__} ===== STOP")
