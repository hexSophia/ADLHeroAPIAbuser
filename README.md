
# ADLHero API Abuse - Proof of Concept (PoC)

This repository demonstrates a Proof of Concept (PoC) for spamming the ADLHero API to manipulate game mechanics, such as earning in-game rewards like gold coins, experience, and items.

## ⚠️ Disclaimer

This repository is for educational purposes only. Unauthorized use of this script may violate the terms of service of the targeted API or platform and could result in account bans, legal action, or other consequences. Use responsibly and ensure you have proper authorization before running this script.

---

## Features

- **API Exploitation**: Automates sending crafted requests to the ADLHero API.
- **Threading**: Supports multi-threading for increased request frequency.
- **Curses UI**: Displays live feedback of request results and awarded items in the terminal.

---

## Requirements

- Python 3.x
- `requests` library: `pip install requests`

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/adlhero-api-abuse-poc.git
   cd adlhero-api-abuse-poc
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Edit the `cookies` in the script with valid credentials from the targeted API.

4. Run the script:
   ```bash
   python adlhero_api_abuse.py
   ```

5. Enter the number of threads to spawn and monitor the results in the terminal UI.

---

## Example Output

```
Threads: 10
Thread 1 started!
Thread 2 started!
...
Result: Success
Gold: 12345
Exp: 54321
Awarded Weapons: [1, 2, 3]
Awarded Items: [{"itemId": "item1", "quantity": 1}]
```

---

## License

This project is open-source under the MIT License. Please review the LICENSE file for more information.

---

## Contributing

Contributions are welcome! Please create a pull request or submit issues for any bugs or suggestions.
