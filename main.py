data_filename = "states.txt"
state_sequence = []
states_counts = dict()
states_dict = dict()
repeated_patterns = dict()


def load_data():
    global states_dict, states_counts
    file = open(data_filename, "r")
    for state in file:
        state = state.strip()
        state_sequence.append(state)
        if state not in states_dict:
            states_dict[state] = dict()
            states_counts[state] = 1
        else:
            states_counts[state] += 1


def run_markov_analysis():
    global states_dict, states_counts
    n = 1
    while True:
        # Counting the transitions between states
        for i in range(0, len(state_sequence) - n):
            a = ""
            for k in range(i, i + n):
                a += state_sequence[k]
            b = state_sequence[i + n]

            if a in states_dict:
                state = states_dict[a]
                if b not in state:
                    state[b] = 1
                else:
                    state[b] += 1

        # Picking the state which occur contiguously
        # more than 1 time and making them a single state
        temp_states_dict = dict()
        temp_states_count = dict()
        for a in states_dict.keys():
            for b in states_dict[a].keys():
                if states_dict[a][b] > 1:
                    state_key = a + b
                    temp_states_count[state_key] = states_dict[a][b]
                    temp_states_dict[state_key] = dict()
                    repeated_patterns[state_key] = states_dict[a][b]
        if len(temp_states_dict.keys()) > 0:
            states_dict = temp_states_dict
            states_counts = temp_states_count
        else:
            print("Exit")
            break
        n += 1


load_data()
run_markov_analysis()
# print(states_counts)
# print(states_dict)
print(repeated_patterns)
