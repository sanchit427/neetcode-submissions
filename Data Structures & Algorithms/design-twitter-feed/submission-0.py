class Twitter:

    def __init__(self):
        self.tweets={}
        self.following={}
        self.time=1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        users={userId}
        users.update(self.following.get(userId, set()))
        all_tweets = []
        for user in users:
            if user in self.tweets:
                all_tweets.extend(self.tweets[user])
        all_tweets.sort(reverse=True)
        all_tweets = all_tweets[:10]
        result = []

        for time, tweetId in all_tweets[:10]:
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId]=set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
         if followerId in self.following:
            self.following[followerId].discard(followeeId)
        
