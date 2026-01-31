import requests

# function to fetch a random joke
def get_random():
    url = "https://catfact.ninja/fact"
    facts = requests.get(url)

    if facts.status_code == 200:
        factsdata = facts.json()
        return f"{factsdata['setup']} - {factsdata['punchline']}"
    else:
        return "Failed to fetch a fact"


# main function
def main():
    print("Welcome to the random joke generator")

    while True:
        user_input = input("Press Enter to generate a joke or type 'stop' to quit: ")

        if user_input.lower() == 'stop':
            print("Exiting the Joke Generator 👋")
            break
        else:
            random_fact = get_random()
            print(random_fact)


# execute the whole function
if __name__ == "__main__":
    main()
