def divisible_by_33( numbers ):
  to_return = []
  for num in numbers:
    if num % 33 == 0:
      to_return.append( num )
  return to_return
