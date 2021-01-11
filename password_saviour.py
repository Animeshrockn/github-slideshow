import requests
import hashlib
import sys

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RunTimeError('Error in API, please check')
  return res


def password_checker(hashes,hash_to_check):
  hash1 = (line.split(':') for line in hashes.text.splitlines())
  for h,count in hash1:
    if h==hash_to_check:
      return count
  return 0


def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char,tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return password_checker(response,tail)
  

def main(argvs):
  for password in argvs:
    count = pwned_api_check(password)
    if count:
      print(f'Password {password} is breached {count} time....Better to change your password')
    else:
      print(f'Password {password} is never breached ....you are good to use it !')
  return 'done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))



