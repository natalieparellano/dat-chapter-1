def divisible_by_33( numbers ):
  to_return = []
  for num in numbers:
    if num % 33 == 0:
      to_return.append( num )
  return to_return

numbers = [ x for x in range( 1, 999) ]
divisible_by_33( numbers )
