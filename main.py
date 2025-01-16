from experiments import *

if __name__ == "__main__":
    print("Choose an experiment to run:")
    print("[0] Experiment 0")
    print("[1] Experiment 1")
    print("[2] Experiment 2")
    print("[3] Experiment 3")
    print("[4] Experiment 4")
    choice = input("Choice: ")

    if choice == "0":
        Experiment_0()
    elif choice == "1":
        Experiment_1()
    elif choice == "2":
        Experiment_2()
    elif choice == "3":
        Experiment_3()
    elif choice == "4":
        Experiment_4()
    else:
        print("Invalid choice.")