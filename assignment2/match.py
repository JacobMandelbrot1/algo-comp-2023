import numpy as np
from typing import List, Tuple



def run_matching(scores: List[List], gender_id: List, gender_pref: List) -> List[Tuple]:

    length = len(gender_pref)
    p_preferences = {}
    a_preferences = {}
    matched = {}
    unmatched = []
    compatible = False

    proposers = [0, 1, 2, 3, 4]
    rejecters = [5, 6, 7, 8, 9]
    rejecters_copy = rejecters.copy()

    for i in range(0, length // 2):
        p_preferences[i] = scores[i]

    for i in range(length // 2, length):
        a_preferences[i] = scores[i]

        # for i, person in enumerate(scores):
        #     for j, person_scores in enumerate(person):
        #         print(person_scores)

    for p in proposers:
        for r in rejecters:
            #if gender_pref[p] == gender_id[r] and gender_pref[r] == gender_id[p]:
            if r not in matched:   # If rejecter is not matched, match them
                    matched[r] = p
                    print("match:" + str(p) + "And" + str(r))
                    rejecters_copy.remove(r)
                    break

            else:   # If rejector is already matched, compare the new person and the current match
                if scores[p][r] > scores[matched[r]][r]:
                    unmatched.append(matched[r])
                    matched[r] = p
                    print("matchagain:" + str(p) + "And" + str(r))
                    break

    for i in rejecters_copy:
        unmatched.append(i)

    new_prop = []
    new_rej = []

    for i in range(0, len(unmatched) // 2):
        new_prop.append(unmatched[i])

    for i in range(len(unmatched) // 2, len(unmatched)):
        new_rej.append(unmatched[i])

        for p in new_prop:
            for r in new_rej:

                #if gender_pref[p] == gender_id[r] and gender_pref[r] == gender_id[p]:
                if r not in matched:  # If rejecter is not matched, match them
                    print("match:" + str(p) + "And" + str(r))
                    matched[r] = p
                    break
                else:  # If rejector is already matched, compare the new person and the current match
                    if scores[p][r] > scores[matched[r]][r]:
                        unmatched.append(matched[r])
                        matched[r] = p
                        print("matchagain:" + str(p) + "And" + str(r))
                        break

    print("matched:" + str(matched))
    print("unmatched:" + str(unmatched))

    matches = [(k, v) for k, v in matched.items()]
    print(matches)

    return matches




    """
    TODO: Implement Gale-Shapley stable matching!
    :param scores: raw N x N matrix of compatibility scores. Use this to derive a preference rankings.
    :param gender_id: list of N gender identities (Male, Female, Non-binary) corresponding to each user
    :param gender_pref: list of N gender preferences (Men, Women, Bisexual) corresponding to each user
    :return: `matches`, a List of (Proposer, Acceptor) Tuples representing monogamous matches

    Some Guiding Questions/Hints:
        - This is not the standard Men proposing & Women receiving scheme Gale-Shapley is introduced as
        - Instead, to account for various gender identity/preference combinations, it would be better to choose a random half of users to act as "Men" (proposers) and the other half as "Women" (receivers)
            - From there, you can construct your two preferences lists (as seen in the canonical Gale-Shapley algorithm; one for each half of users
        - Before doing so, it is worth addressing incompatible gender identity/preference combinations (e.g. gay men should not be matched with straight men).
            - One easy way of doing this is setting the scores of such combinations to be 0
            - Think carefully of all the various (Proposer-Preference:Receiver-Gender) combinations and whether they make sense as a match
        - How will you keep track of the Proposers who get "freed" up from matches?
        - We know that Receivers never become unmatched in the algorithm.
            - What data structure can you use to take advantage of this fact when forming your matches?
        - This is by no means an exhaustive list, feel free to reach out to us for more help!
    """

    




if __name__ == "__main__":
    raw_scores = np.loadtxt('raw_scores.txt').tolist()
    genders = []
    with open('genders.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            genders.append(curr)

    gender_preferences = []
    with open('gender_preferences.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            gender_preferences.append(curr)

    gs_matches = run_matching(raw_scores, genders, gender_preferences)
