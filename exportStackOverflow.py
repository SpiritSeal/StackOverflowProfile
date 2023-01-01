import requests
import json

def get_answers_by_user(user_id):
    # Set the base URL for the API
    base_url = "https://api.stackexchange.com/2.2/users/{}/answers".format(user_id)

    # Set the parameters for the API request
    params = {
        "order": "desc",
        "sort": "votes",
        "site": "stackoverflow"
    }

    # Make the request to the API
    response = requests.get(base_url, params=params)

    # Check the status code of the response
    if response.status_code != 200:
        raise Exception("An error occurred while fetching the data: {}".format(response.status_code))

    # Get the data from the response
    data = response.json()

    # Print the data to the console, useful for debugging
    # print(json.dumps(data, indent=4))

    # Print a list of the answers
    for item in data["items"]:
        # Print the full URL to the answer
        print("https://stackoverflow.com/a/{}".format(item["answer_id"]))

def get_questions_by_user(user_id):
    # Set the base URL for the API
    base_url = "https://api.stackexchange.com/2.2/users/{}/questions".format(user_id)

    # Set the parameters for the API request
    params = {
        "order": "desc",
        "sort": "votes",
        "site": "stackoverflow"
    }

    # Make the request to the API
    response = requests.get(base_url, params=params)

    # Check the status code of the response
    if response.status_code != 200:
        raise Exception("An error occurred while fetching the data: {}".format(response.status_code))

    # Get the data from the response
    data = response.json()

    # Print the data to the console, useful for debugging
    # print(json.dumps(data, indent=4))

    # Print a list of the questions
    for item in data["items"]:
        # Print the full URL to the question
        print("https://stackoverflow.com/q/{}".format(item["question_id"]))

def get_user_info(user_id):
    # Set the base URL for the API
    base_url = "https://api.stackexchange.com/2.2/users/{}".format(user_id)

    # Set the parameters for the API request
    params = {
        "order": "desc",
        "sort": "reputation",
        "site": "stackoverflow"
    }

    # Make the request to the API
    response = requests.get(base_url, params=params)

    # Check the status code of the response
    if response.status_code != 200:
        raise Exception("An error occurred while fetching the data: {}".format(response.status_code))

    # Get the data from the response
    data = response.json()

    # Print the data to the console, useful for debugging
    print(json.dumps(data, indent=4))

    # Return json data
    return data["items"][0]

# Use get_user_info to build a markdown profile file
def build_profile(user_id):
    # Get user info
    user = get_user_info(user_id)

        # Build the Markdown profile
    profile = """
Profile image: ![]({})

# {}'s Stack Overflow Profile

## Basics

- Location: {}

## Stats

- Reputation: {}
- Bronze Badges: {}
- Silver Badges: {}
- Gold Badges: {}

## Contact

- Website: {}
- Stack Overflow: https://stackoverflow.com/users/{}/{}
    """.format(user["profile_image"], user["display_name"], user["location"], user["reputation"], user["badge_counts"]["bronze"], user["badge_counts"]["silver"], user["badge_counts"]["gold"], user["website_url"], user["user_id"], user["display_name"])
    
    #.format(user["display_name"], user["location"], user["reputation"], user["badge_counts"]["bronze"], user["badge_counts"]["silver"], user["badge_counts"]["gold"], user["website_url"], user["user_id"], user["display_name"])

    # Return the Markdown profile
    return profile



def __main__():
    # Get the user ID from the command line
    # user_id = sys.argv[1]
    user_id = 14362191
    '''
    # Call the function to get the answers
    get_answers_by_user(user_id)

    # Call the function to get the questions
    get_questions_by_user(user_id)
    '''
    # Call the function to get the reputation and write to profile.md and README.md
    profile = build_profile(user_id)
    with open("profile.md", "w") as f:
        f.write(profile)
    with open("README.md", "w") as f:
        f.write(profile)
        


# Call the main function
if __name__ == "__main__":
    __main__()
