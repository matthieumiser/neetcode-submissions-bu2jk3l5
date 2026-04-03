class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        position = list(position)
        speed = list(speed)

        fleets = 0
        last_hours = 0
        for i in range(len(position) - 1, -1, -1):
            hours = (target - position[i]) / speed[i] 
            if hours > last_hours:
                fleets += 1
                last_hours = hours
            
        return fleets
