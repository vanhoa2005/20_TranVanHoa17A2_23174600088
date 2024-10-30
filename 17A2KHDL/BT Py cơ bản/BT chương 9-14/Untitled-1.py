def is_palindrome(n):
  
  n_str = str(n)
  return n_str == n_str[::-1]





def is_prime(n):
  """
  Kiểm tra số nguyên tố.

  Tham số:
    n: Số nguyên dương.

  Trả về:
    True nếu n là số nguyên tố, False nếu không.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

for i in range(1,1001) :
  if is_palindrome(i) is True :
    print(i)