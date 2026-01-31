import requests

# function to fetch a random joke
def get_random():
    url = "https://official-joke-api.appspot.com/random_joke"
    joke = requests.get(url)

    if joke.status_code == 200:
        jokedata = joke.json()
        return f"{jokedata['setup']} - {jokedata['punchline']}"
    else:
        return "Failed to fetch a joke"


# main function
def main():
    print("Welcome to the random joke generator")

    while True:
        user_input = input("Press Enter to generate a joke or type 'stop' to quit: ")

        if user_input.lower() == 'stop':
            print("Exiting the Joke Generator 👋")
            break
        else:
            random_joke = get_random()
            print(random_joke)


# execute the whole function
if __name__ == "__main__":
    main()
