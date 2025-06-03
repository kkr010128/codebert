import time
start = time.time()


import random
from typing import List


def score_by_simple_method(schedule, loss_list, satisfied_matrix):
    prev_list = [-1] * 26
    plus = 0
    minus = 0
    for day, open_contest in enumerate(schedule):
        prev_list[open_contest] = day
        plus += satisfied_matrix[day][open_contest]

        for contest, prev_day in enumerate(prev_list):
            spend = day - prev_day
            loss_base = loss_list[contest]
            minus += loss_base * spend

    return plus - minus


def schedule_to_dict(schedule, days):
    dict = {contest: [-1] for contest in range(26)}
    for day, contest in enumerate(schedule):
        dict[contest].append(day)

    for contest in range(26):
        dict[contest].appned(days)

    return dict


class Node:
    def __init__(self, contest, last_day):
        self.contest = contest
        self.prev_day = -1
        self.next_day = last_day


def schedule_to_linked(schedule, last_day):
    linked_schedule = []
    prev_list = [-1] * 26
    for day, contest in enumerate(schedule):
        cur_node = Node(contest, last_day)
        prev_day = prev_list[contest]
        cur_node.prev_day = prev_day
        if prev_day != -1:
            prev_node = linked_schedule[prev_day]
            prev_node.next_day = day

        prev_list[contest] = day
        linked_schedule.append(cur_node)

    return linked_schedule


def is_exchangeable(day1, day2, linked_schedule: List[Node]):
    """
    swap先が同じコンテストの時 False
    swap先が同コンテストの前後開催を超えている場合 False
    ex. schedule: [1, 2, 3, 4, 3, 5, 6]
        swap target:     ^        ^
    day1 = 2 (0-indexed)
    day2 = 5
    schedule[day1].next = 4

    """

    if linked_schedule[day1].contest == linked_schedule[day2].contest:
        return False

    node1 = linked_schedule[day1]
    node1_prev = node1.prev_day
    node1_next = node1.next_day

    if day2 < node1_prev or node1_next < day2:
        return False

    node2 = linked_schedule[day2]
    node2_prev = node2.prev_day
    node2_next = node2.next_day

    if day1 < node2_prev or node2_next < day1:
        return False

    return True


def swap_contests_in_linked_schedule(day1, day2, linked_schedule: List[Node], last_day):
    node1 = linked_schedule[day1]
    node1_prev = node1.prev_day
    node1_next = node1.next_day

    node2 = linked_schedule[day2]
    node2_prev = node2.prev_day
    node2_next = node2.next_day

    linked_schedule[day1], linked_schedule[day2] = linked_schedule[day2], linked_schedule[day1]  # swap

    if node1_prev != -1:
        linked_schedule[node1_prev].next_day = day2
    if node1_next != last_day:
        linked_schedule[node1_next].prev_day = day2

    if node2_prev != -1:
        linked_schedule[node2_prev].next_day = day1
    if node2_next != last_day:
        linked_schedule[node2_next].prev_day = day1


def calc_score_change_by_shift(contest, prev, before_center, after_center, next, loss_list, satisfied_matrix):
    loss_base = loss_list[contest]
    before_spend1 = before_center - prev
    before_spend2 = next - before_center
    before_loss = loss_base * (before_spend1 * (before_spend1-1) + before_spend2 * (before_spend2-1)) // 2
    before_get = satisfied_matrix[before_center][contest]
    before_score = before_get - before_loss

    after_spend1 = after_center - prev
    after_spend2 = next - after_center
    after_loss = loss_base * (after_spend1 * (after_spend1-1) + after_spend2 * (after_spend2-1)) // 2
    after_get = satisfied_matrix[after_center][contest]
    after_score = after_get - after_loss

    score_change = after_score - before_score
    return score_change


def calc_score_change_by_swap(day1, day2, linked_schedule: List[Node], loss_list, satisfied_matrix):
    node1 = linked_schedule[day1]
    change_score1 = calc_score_change_by_shift(node1.contest, node1.prev_day, day1, day2, node1.next_day, loss_list, satisfied_matrix)
    node2 = linked_schedule[day2]
    change_score2 = calc_score_change_by_shift(node2.contest, node2.prev_day, day2, day1, node2.next_day, loss_list, satisfied_matrix)

    return change_score1 + change_score2


days = int(input())
loss_list = list(map(int, input().split()))
satisfied_matrix = [list(map(int, input().split())) for _ in range(days)]
schedule = [i % 26 for i in range(days)]
linked_schedule = schedule_to_linked(schedule, days)
base_score = score_by_simple_method(schedule, loss_list, satisfied_matrix)

loops = 0
while time.time() - start < 1.8:
    loops += 1
    day1 = random.randint(0, days - 25)
    swap = []
    best = 0
    for day2 in range(day1+1, day1+25):
        if is_exchangeable(day1, day2, linked_schedule):
            change_score = calc_score_change_by_swap(day1, day2, linked_schedule, loss_list, satisfied_matrix)

            if change_score > best:
                swap = [day1, day2]
                best = change_score

    if swap:
        day1, day2 = swap
        swap_contests_in_linked_schedule(day1, day2, linked_schedule, days)
        base_score += best


ans = [node.contest + 1 for node in linked_schedule]
print(*ans, sep="\n")
