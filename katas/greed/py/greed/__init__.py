# Implement functions here
def template(arg):
    result = f"Doing something with {arg}"
    return result


class Greed:
    some_val = False

    def __init__(self):
        self.some_val = True

    def get_some_val(self):
        print(self.some_val)

    def set_some_val(self):
        self.some_val = not self.some_val

    def score(self, dice):
        total_score = 0
        freq = [0, 0, 0, 0, 0, 0, 0]
        for n in dice:
            freq[n] += 1

        # Frequency 1
        if freq[1] == 1:
            total_score += 100

        if freq[5] == 1:
            total_score += 50

        # Frequency 3
        if freq[1] >= 3:
            total_score += 1000

        if freq[2] >= 3:
            total_score += 200

        if freq[3] >= 3:
            total_score += 300

        if freq[4] >= 3:
            total_score += 400

        if freq[5] >= 3:
            total_score += 500

        if freq[6] >= 3:
            total_score += 600

        #     i 0 1 2 3 4 5 6
        # freq=[0,0,0,0,4,1,0]
        pairs = 0
        straight = 0
        for n in freq:
            if n == 4:
                total_score *= 2
            if n == 5:
                total_score *= 4
            if n == 6:
                total_score *= 8
            if n == 2:
                pairs += 1
            if n == 1:
                straight += 1

        if pairs == 3:
            total_score += 800

        if straight == 6:
            total_score = 1200

        return total_score
