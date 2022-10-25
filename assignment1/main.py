#!usr/bin/env python3
import json
import math
import sys
import os
import numpy as np

INPUT_FILE = 'testdata.json'  # Constant variables are usually in ALL CAPS


class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name
        self.gender = gender
        self.preferences = preferences
        self.grad_year = grad_year
        self.responses = responses


# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):
    total_score = 0
    grade_weight = 3
    answer_weight = 2

    # homophobic checking of preferences
    if user1.gender == user2.gender:
        total_score = 0
        return 0
    #print("year: " + str(1.0 / (grade_weight * (1 + abs(user1.grad_year - user2.grad_year)))))
    total_score += 1.0 / (grade_weight * (1 + abs(user1.grad_year - user2.grad_year)))

    # Add to score depending on how close responses are
    for i in range(len(user1.responses)):
        if user1.responses[i] == user2.responses[i]:
            #print("answers:" + str(1.0 / (answer_weight * (1 + rarity[i][user2.responses[i]]))))
            total_score += 1.0 / (answer_weight * (1 + rarity[i][user2.responses[i]]))

    return total_score


if __name__ == '__main__':
    # Make sure input file is valid
    if not os.path.exists(INPUT_FILE):
        print('Input file not found')
        sys.exit(0)

    users = []
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            new_user = User(user_obj['name'], user_obj['gender'],
                            user_obj['preferences'], user_obj['gradYear'],
                            user_obj['responses'])
            users.append(new_user)

    rarity = np.zeros((len(users[0].responses), 6))

    # Make table with rarity of the responses
    for i in range(len(users)):
        user = users[i]
        responses = user.responses
        for j in range(len(responses)):
            rarity[j][responses[j]] += 1

            # if users[i].responses[i] == users[j].responses[i]:
            #     percentage += 1

            # print(users[i].responses[i])

        # rarity.append(percentage)

    print(rarity)


    for i in range(len(users) - 1):
        for j in range(i + 1, len(users)):
            user1 = users[i]
            user2 = users[j]
            score = compute_score(user1, user2)
            print('Compatibility between {} and {}: {}'.format(user1.name, user2.name, score))
