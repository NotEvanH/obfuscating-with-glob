import glob
import os

def main():
    print("Hello There!")
    target = input("Enter the 'LOLbin' you want to target (e.g. calc.exe): ")
    target = os.path.join("C:\\Windows\\System32", target)

    if not os.path.exists(target):
        print("Not a valid target..")
        return

    parts = target.split("\\")
    print("Split path:", parts)

    obfuscated_command = parts[0] + "\\"
    current_path = parts[0] + "\\"

    for index in range(1, len(parts)):
        part = parts[index]
        best_obfuscation = None

        for i in range(1, len(part) + 1):
            wildcard = "?" * i + part[i:]
            test_path = os.path.join(current_path, wildcard)

            matches = glob.glob(test_path)
            if len(matches) == 1:
                best_obfuscation = wildcard
            else:
                break

        if best_obfuscation:
            print(f"[+] Maximally obfuscated '{part}' as '{best_obfuscation}'")
            obfuscated_command = os.path.join(obfuscated_command, best_obfuscation)
            current_path = os.path.join(current_path, part)
        else:
            print(f"[-] Could not uniquely obfuscate: {part}")
            return

    print("\nFinal Obfuscated Path:")
    print(obfuscated_command)

if __name__ == "__main__":
    main()
