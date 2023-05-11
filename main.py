from firmware_modules import bitmain, microbt, canaan
from reporting_modules import stress_test, report_generation
from web_modules import web_ui

def print_menu():
    print("MinerMatrix Console Menu:")
    print("1. Connect to an ASIC unit")
    print("2. Get current config")
    print("3. Change config")
    print("4. Reboot ASIC unit")
    print("5. Run stress tests")
    print("6. Generate and display reports")
    print("7. Launch Web Interface")
    print("0. Exit")

def print_manufacturers():
    print("Select ASIC Manufacturer:")
    print("1. Bitmain")
    print("2. MicroBT")
    print("3. Canaan")
    print("0. Back to main menu")

def main():
    print_menu()
    option = input("Enter your choice: ")
    try:
        if option == "1":
            print_manufacturers()
            manufacturer = input("Enter the manufacturer number: ")
            if manufacturer.isdigit() and int(manufacturer) in [1, 2, 3]:
                if manufacturer == "1":
                    bitmain.connect()
                elif manufacturer == "2":
                    microbt.connect()
                elif manufacturer == "3":
                    canaan.connect()
            else:
                print("Invalid manufacturer number")

        elif option == "2":
            # Call function to get current config
            pass

        elif option == "3":
            # Call function to change config
            pass

        elif option == "4":
            # Call function to reboot ASIC unit
            pass

        elif option == "5":
            stress_test.run_tests()

        elif option == "6":
            report_generation.generate_report()

        elif option == "7":
            web_ui.launch()

        elif option == "0":
            print("Exiting...")
            return

        else:
            print("Invalid option")

    except Exception as e:
        print(f"Error: {e}")

    main()

if __name__ == '__main__':
    main()
