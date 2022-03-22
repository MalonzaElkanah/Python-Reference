import sys, pyperclip
passwords = {"email": "qwd1ene3r30kf34kk3kkk7j5k2", "luggage": "1234", "blog": "iki7jkh4o9u6uh9m7rf7loo0p7"}

if sys.argv<2:
    print("Usage: Python pw.py - Copy [Account] password")
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
