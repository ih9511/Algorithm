def solution(routes):
    camera = 0
    routes = sorted(routes)
    # routes.append([30001, 30001])
    routes.append([float('inf'), float('inf')])
    check = routes[0]
    
    for i in range(len(routes) - 1):
        if routes[i + 1][0] <= check[1]:
            check[0] = routes[i + 1][0]
        if routes[i + 1][0] > check[1]:
            camera += 1
            check = routes[i + 1]
        if routes[i + 1][1] < check[1]:
            check[1] = routes[i + 1][1]
    
    return camera