import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Make a GET request
        response = requests.get(url)

        # Handle response errors
        if response.status_code != 200:
            print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
            return

        users = response.json()

        # Handle empty list
        if not users:
            print("No users found.")
            return

        # Loop through users
        for i, user in enumerate(users, start=1):
            name = user.get("name", "N/A")
            username = user.get("username", "N/A")
            email = user.get("email", "N/A")
            city = user.get("address", {}).get("city", "N/A")

            print(f"User {i}:")
            print(f"Name: {name}")
            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"City: {city}")
            print("-" * 40)

        # Printing users whose city starts with 'S'
        print("\nUsers from cities starting with 'S':")
        for user in users:
            city = user.get("address", {}).get("city", "")
            if city.startswith("S"):
                print(f"- {user.get('name')} ({city})")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")

# Run the function
if __name__ == "__main__":
    fetch_users()
