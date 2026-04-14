class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        if len(self.tweet_map[userId]) > 10:
            self.tweet_map[userId].pop(0)
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []

        heap = []
        self.follow_map[userId].add(userId)

        for folowee in self.follow_map[userId]:
            if folowee in self.tweet_map:
                index = len(self.tweet_map[folowee]) - 1
                count, twwt = self.tweet_map[folowee][index]
                heapq.heappush_max(heap,[count, twwt, folowee, index-1])

        
        while heap and len(result) <10:
            count, twwt, folowee, index = heapq.heappop_max(heap)
            result.append(twwt)

            if index >= 0:
                time, tweetId = self.tweet_map[folowee][index]
                heapq.heappush_max(heap, [time, tweetId, folowee, index-1])

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


