import os
import requests

def join_waitlist(file_path):
    with open(file_path, 'r') as file:
        addresses = file.readlines()

    url_base = 'https://choizzy.io/api/waitlist/join?address={}'

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    for address in addresses:
        address = address.strip()
        if not address:
            continue

        url = url_base.format(address)

        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                print(f"Успешно! Вы присоединились к списку ожидания с адресом {address}")
            else:
                print(f"Ошибка {res.status_code}")
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при выполнении запроса для адреса {address}: {e}')

def show_dev_info():
    print()
    print("\033[32m" + "VERSION: " + "\033[37m" + "1.0" + "\033[37m")
    print("\033[32m"+"DEV: " + "\033[37m" + "https://t.me/HashAlchemist" + "\033[37m")
    print()

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'addresses.txt')
    join_waitlist(file_path)
    show_dev_info()

if __name__ == "__main__":
    main()