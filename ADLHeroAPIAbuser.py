import requests
import threading
import curses

gold = ""
exp = ""
reqresult = ""
awardWeaponIds = []
awardItemList = []

cookies = {
    'GCILB': '""',
    'PHPSESSID': '',
    'username': '',
    'token': '',
    'logined': 'true'
}

def perform_attack():
    global gold, exp, reqresult, awardWeaponIds, awardItemList
    try:
        response = requests.post(
            "https://adl.edu.tw/heroApi/planetWarBattle",
            cookies=cookies,
            json={
                "learnLid": 100,
                "hid": 249743,
                "gameSec": 0.0,
                "dieEnemys": [{"enemyId": 4, "enemyCount": 1000000}],
                "setWeapons": [],
                "overWaveCount": 1000000
            }
        )
        result = response.json()
        gold = result.get('goldCoin', 'N/A')
        exp = result.get('heroExpNow', 'N/A')
        reqresult = result.get('result', 'N/A')
        awardWeaponIds = result.get('awardWeaponIds', [])
        awardItemList = result.get('awardItemList', [])
    except Exception as e:
        print(f"Error during API request: {e}")

def main():
    thread_count = int(input("Enter the number of threads: "))
    threads = []

    for i in range(thread_count):
        thread = threading.Thread(target=perform_attack)
        threads.append(thread)
        thread.start()
        print(f"Thread {i+1} started!")

    try:
        stdscr = curses.initscr()
        while True:
            stdscr.erase()
            stdscr.addstr(f"Result: {reqresult}\n")
            stdscr.addstr(f"Gold: {gold}\n")
            stdscr.addstr(f"Exp: {exp}\n")
            stdscr.addstr(f"Awarded Weapons: {awardWeaponIds}\n")
            stdscr.addstr(f"Awarded Items: {awardItemList}\n")
            stdscr.refresh()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        curses.endwin()

if __name__ == '__main__':
    main()
