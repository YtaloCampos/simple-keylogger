# verify arguments
def verify_args(arguments):
  values = []

  i = 0
  for arg in arguments:

    if arg == "--from":
      arg_form = arguments[i+1]
      values.append(arg_form)

    elif arg == "--pass":
      arg_pass = arguments[i+1]
      values.append(arg_pass)

    elif arg == "--to":
      arg_to = arguments[i+1]
      values.append(arg_to)

    i = i + 1

  return values