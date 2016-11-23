import got3

def main():
	
	def printTweet(descr, t):
		print(descr)
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)

	# Örnek 1 - Kullanıcı adına göre arama
	tweetCriteria = got3.manager.TweetCriteria().setUsername('HaberSau').setMaxTweets(1)
	tweet = got3.manager.TweetManager.getTweets(tweetCriteria)[0]
	
	printTweet("### # Örnek 1 - Kullanıcı adına göre arama", tweet)
	
	# Örnek 2 - Twite göre arama
	tweetCriteria = got3.manager.TweetCriteria().setQuerySearch('sakarya').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(1)
	tweet = got3.manager.TweetManager.getTweets(tweetCriteria)[0]
	
	printTweet("### # Örnek 2 - Twite göre arama [sakarya]", tweet)
	
	# Example 3 - Get tweets by username and bound dates
	tweetCriteria = got3.manager.TweetCriteria().setUsername("HaberSau").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	tweet = got3.manager.TweetManager.getTweets(tweetCriteria)[0]
	
	printTweet("### Örnek 3 - Bir kullanıcının belirli bir tarihteki twitleri", tweet)

if __name__ == '__main__':
	main()
	