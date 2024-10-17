class Star_Cinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, rows, cols, hall_no=None):
        hall = Hall(rows, cols, hall_no)
        self._hall_list.append(hall)

    def get_hall(self, hall_no):
        if 0 < hall_no <= len(self._hall_list):
            return self._hall_list[hall_no - 1]
        else:
            print("Invalid hall number.")
            return None


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self.hall_no = hall_no
        self._show_list = []
        self._seats = {}

    def entry_show(self, id, movie_name, time):
        self._show_list.append((id, movie_name, time))
        self._seats[id] = self.make_seat()

    def make_seat(self):
        return [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, id, seat_input):
        if id in self._seats:
            matrix = self._seats[id]
            try:
                seats = [tuple(map(int, seat.split(','))) for seat in seat_input.split()]
                for i, j in seats:
                    i -= 1
                    j -= 1
                    if 0 <= i < self._rows and 0 <= j < self._cols:
                        if matrix[i][j] == 1:
                            print(f"Seat [{i + 1}, {j + 1}] is already booked.")
                        else:
                            matrix[i][j] = 1
                            print(f"Seat [{i + 1}, {j + 1}] is successfully booked.")
                    else:
                        print(f"Invalid seat coordinates [{i + 1}, {j + 1}].")
            except ValueError:
                print("Invalid seat input format. Use comma-separated values like '1,1 2,2'.")
        else:
            print("Invalid show ID.")

    def view_show_list(self):
        if not self._show_list:
            print("No shows available.")
        else:
            for show in self._show_list:
                print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id in self._seats:
            matrix = self._seats[id]
            available_seats = sum(row.count(0) for row in matrix)
            total_seats = self._rows * self._cols
            print(f"\nAvailable Seats: {available_seats}/{total_seats}")
            for row in matrix:
                print(row)
        else:
            print("Invalid show ID.")


def run_counter(hall):
    while True:
        print("\nOptions:")
        print("1: View Show List")
        print("2: View Available Seats")
        print("3: Book Seats")
        print("4: Exit")
        option = int(input("Enter your choice (1-4): "))

        if option == 1:
            hall.view_show_list()
        elif option == 2:
            show_id = int(input("Enter show ID: "))
            hall.view_available_seats(show_id)
        elif option == 3:
            hall.view_show_list()
            show_id = int(input("Enter show ID: "))
            if any(show[0] == show_id for show in hall._show_list):
                hall.view_available_seats(show_id)
                seat_input = input("Enter seat numbers to book (e.g., '1,1 2,2'): ")
                hall.book_seats(show_id, seat_input)
            else:
                print("Invalid show ID.")
        elif option == 4:
            break
        else:
            print("Invalid choice, please try again.")


# Main program
star_cinema = Star_Cinema()
star_cinema.entry_hall(6, 7, 1)
star_cinema.entry_hall(4, 5, 2)

hall1 = star_cinema.get_hall(1)
hall1.entry_show(1, "Arya 2", "6:00 PM")
hall1.entry_show(2, "International Khiladi", "8:00 PM")

hall2 = star_cinema.get_hall(2)
hall2.entry_show(1, "Tur Naam", "6:00 PM")
hall2.entry_show(2, "Premi", "9:00 PM")

while True:
    print("\nMain Menu:")
    print("1: Select Hall")
    print("2: Exit")
    main_choice = int(input("Enter your choice (1-2): "))

    if main_choice == 1:
        for i, hall in enumerate(star_cinema._hall_list, start=1):
            print(f"{i}: Hall {i}")
        selected_hall = int(input(f"Select a hall (1-{len(star_cinema._hall_list)}): "))
        hall = star_cinema.get_hall(selected_hall)
        if hall:
            run_counter(hall)
    elif main_choice == 2:
        print("Thank you for using the cinema booking system.")
        break
    else:
        print("Invalid choice.")
