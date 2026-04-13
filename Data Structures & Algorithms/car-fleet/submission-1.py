class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleet = currentTime = 0
        print(sorted(pairs, reverse=True))
        for dist, speed in sorted(pairs, reverse=True):
            destination_time = (target - dist)/speed
            if currentTime < destination_time:
                fleet += 1
                currentTime = destination_time

        return fleet