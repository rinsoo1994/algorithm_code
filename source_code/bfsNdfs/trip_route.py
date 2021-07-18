result = []

import copy


def dfs(start, tickets, is_use, route):
    global result
    if len(route) == len(tickets) + 1:
        result.append(copy.deepcopy(route))
        return

    for idx, ticket in enumerate(tickets):
        if ticket[0] == start and not is_use[idx]:
            route.append(ticket[1])
            is_use[idx] = True
            dfs(ticket[1], tickets, is_use, route)
            is_use[idx] = False
            route.pop(-1)


def solution(tickets):

    is_use = [False for _ in tickets]

    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            is_use[idx] = True
            route = []
            route.extend(ticket)
            dfs(ticket[1], tickets, is_use, route)
            is_use[idx] = False

    global result
    res = min(result)
    # print(res)
    return res


solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	)

