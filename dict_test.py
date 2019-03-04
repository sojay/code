runner_lst = {'Francis': 'Ikeja', 'Amanda': 'Costain', "Juliet": 'Lagos Island'}

tasker_location = 'Ikeja'

print([loc for loc, run in runner_lst.items() if run == tasker_location])