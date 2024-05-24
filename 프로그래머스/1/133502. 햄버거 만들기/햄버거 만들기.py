def solution(ingredient):
    cnt = 0
    stack = []
    
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if len(stack) >= 4:
            #print(stack, stack[len(stack)-4 : ])
            if stack[len(stack)-4 : ] == [1, 2, 3, 1]:
                cnt += 1
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
        # if len(stack) >= 4:
        #     if stack[-5 : -1] == [1, 2, 3, 1]:
        #         cnt += 1
        #         stack.pop()
        #         stack.pop()
        #         stack.pop()
        #         stack.pop()

    return cnt