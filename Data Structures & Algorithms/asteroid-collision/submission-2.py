class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                if not stack:
                    res.append(asteroid)
                    continue

                # stack is not empty
                last_pos = stack[-1]

                # remove from stack until minus asteroid is fully beaten.
                while abs(asteroid) > last_pos:
                    stack.pop() # remove the positive
                    
                    # update the positive
                    if stack: 
                        last_pos = stack[-1]
                    else:
                        # all pos are done.
                        res.append(asteroid)
                        break

                # if they are equal; we remove both.
                if last_pos == abs(asteroid):
                    stack.pop()
                
        res.extend(stack)
        return res
                    
