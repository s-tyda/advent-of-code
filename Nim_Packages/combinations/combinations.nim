proc comb[T](a: openarray[T]; n: int; use: seq[bool]): seq[seq[T]] =
  result = newSeq[seq[T]]()
  var use = use
  if n <= 0: return
  for i in 0  .. a.high:
    if not use[i]:
      if n == 1:
        result.add(@[a[i]])
      else:
        use[i] = true
        for j in comb(a, n - 1, use):
          result.add(a[i] & j)

proc combinations*[T](a: openarray[T], n: int): seq[seq[T]] =
  var use = newSeq[bool](a.len)
  comb(a, n, use)