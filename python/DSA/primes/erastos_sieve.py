def erastos_sieve(arr, index=0):
  sieve = lambda arr, index: ((arr % arr[index]) != 0) | (arr == arr[index])
  def recur(arr, index):
    if len(arr) <= (index+1):
      return arr
    else:
      out = arr[sieve(arr, index)]
      return recur(out, index+1)
  
  return recur(arr, index)