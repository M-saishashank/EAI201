def determine_radius(bot_type):
    if bot_type == 'round':
        return 1
    elif bot_type == 'square':
        return 2
    elif bot_type == 'triangle':
        return 3
    elif bot_type == 'heptagon':
        return 1.5
    return 2


def perform_cleaning(pattern, width, height):
    total_cells = 0
    steps_count = 0
    move_radius = determine_radius(pattern)

    for row_index in range(height):
        if row_index % 2 == 0:
            traversal = range(width)
        else:
            traversal = range(width - 1, -1, -1)

        for col in traversal:
            total_cells += 1
            steps_count += move_radius

    return total_cells, steps_count


def evaluate_shapes():
    bot_shapes = ['round', 'square', 'triangle', 'heptagon']
    w, h = 10, 10
    all_results = []

    for bot in bot_shapes:
        cells_covered, time_needed = perform_cleaning(bot, w, h)
        all_results.append((bot, cells_covered, time_needed))

    top_choice = min(all_results, key=lambda x: x[2])
    return top_choice, all_results


def print_summary(clean_type, substance):
    print(f"\n--- Cleaning Mode: {clean_type} | Target: {substance} ---")
    winner, comparisons = evaluate_shapes()

    print(f"\n>> Optimal Design: {winner[0].title()}")
    print(f"-> Cells Cleared: {winner[1]}")
    print(f"-> Duration: {winner[2]} units")

    print("\n>> Shape-wise Cleaning Duration:")
    for shape, cells, duration in comparisons:
        print(f"- {shape.title()}: {duration} units")

    print()


def handle_solid():
    print("\nSelect solid material:")
    print("1) Dust")
    print("2) Rocks or Papers")
    print("3) Miscellaneous")
    selection = input("Input option (1-3): ")

    if selection == '1':
        print_summary("Solid", "Dust")
    elif selection == '2':
        print_summary("Solid", "Rocks/Papers")
    elif selection == '3':
        print_summary("Solid", "Others")
    else:
        print("Invalid selection. Please retry.")


def handle_liquid():
    print("\nPick a liquid type:")
    print("1) Water")
    print("2) Beverage")
    print("3) Other Liquids")
    option = input("Input choice (1-3): ")

    if option == '1':
        print_summary("Liquid", "Water")
    elif option == '2':
        print_summary("Liquid", "Beverage")
    elif option == '3':
        print_summary("Liquid", "Others")
    else:
        print("Not a valid input. Try again.")


def initiate_cleaning():
    print("\n--- Cleaning Procedure Initiated ---")
    print("1) Clean Solid Debris")
    print("2) Clean Liquid Spills")
    print("3) Return to Main Menu")
    choice = input("Select action (1-3): ")

    if choice == '1':
        handle_solid()
    elif choice == '2':
        handle_liquid()
    elif choice == '3':
        return
    else:
        print("Invalid input. Returning to main menu.")


def rotate_left():
    print("Bot rotated left.")


def rotate_right():
    print("Bot rotated right.")


def engage_dock():
    print("Bot is now docked.")


def main():
    while True:
        print("\n===== Vacuum Bot Console =====")
        print("1) Begin Cleaning Operation")
        print("2) Turn Left")
        print("3) Turn Right")
        print("4) Dock Station")
        print("5) Exit Program")
        user_input = input("Choose from above (1-5): ")

        if user_input == '1':
            initiate_cleaning()
        elif user_input == '2':
            rotate_left()
        elif user_input == '3':
            rotate_right()
        elif user_input == '4':
            engage_dock()
        elif user_input == '5':
            print("Program terminated. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a valid number.")

main()
