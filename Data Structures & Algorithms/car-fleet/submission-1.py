class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        position = list(position)
        speed = list(speed)

        stack = []
        for i in range(len(position) - 1, -1, -1):
            hours = (target - position[i]) / speed[i] 
            if stack and stack[-1] >= hours:
                continue
            stack.append(hours)
        return len(stack)
