tasks = {}
next_id = 1

while True:
    print("\n1.Add 2.View 3.Complete 4.Delete 5.Exit")
    choice = input("Choose: ")

    if choice == '1':
        desc = input("Enter task: ")
        tasks[next_id] = {"desc": desc, "done": False}
        print(f"Added: {desc}")
        next_id += 1

    elif choice == '2':
        if not tasks: print("No tasks")
        for id, t in tasks.items():
            status = "✓" if t["done"] else "○"
            print(f"{id}. [{status}] {t['desc']}")

    elif choice == '3':
        num = int(input("Task ID to complete: "))
        if num in tasks: tasks[num]["done"] = True; print("Done!")
        else: print("ID not found")

    elif choice == '4':
        num = int(input("Task ID to delete: "))
        if num in tasks: tasks.pop(num); print("Deleted!")
        else: print("ID not found")

    elif choice == '5': break
    else: print("Invalid choice")