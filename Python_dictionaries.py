eu_capitals = {
"Austria": "Vienna",
"Belgium": "Brussels",
"France": "Paris",
"Germany": "Berlin",
"Liechtenstein": "Vaduz",
"Luxembourg": "Luxembourg City",
"Monaco": "Monte Carlo",
"The Netherlands": "Amsterdam",
"Switzerland": "Bern"
}
print(f"Some EU countries and their capitals: {eu_capitals}")

#task 12

contact_book = {}
print("Commands: 'add', 'view', 'search', 'exit'")
while True:
    # 2. Get user input for the action
    choice = input("\nEnter command: ").lower()
    # 3. Handle 'ADD' logic
    if choice == "add":
        name = input("Enter contact name: ").strip().title()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")