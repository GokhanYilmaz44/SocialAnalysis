# -*- coding: utf-8 -*-

import sys, getopt, got3, datetime, codecs, sqlite3

conn = sqlite3.connect('TweetAnalysis.db')
c = conn.cursor()

# CREATE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS
    Tweets (kullanıcıAd, tarih, retweet, favorite,tweet,konum,mention,hastag,link,tweetid,standart)""")


def main(argv):
    if len(argv) == 0:
        print('Parametre girmelisiniz. Lütfen \"-h\" parametresi ile yardım alın.')
        return

    if len(argv) == 1 and argv[0] == '-h':
        print("""\nTo use this jar, you can pass the folowing attributes:
    luşşs: Username of a specific twitter account (without @)
       since: The lower bound date (yyyy-mm-aa)
       until: The upper bound date (yyyy-mm-aa)
 querysearch: A query text to be matched
   maxtweets: The maximum number of tweets to retrieve

 \nExamples:
  # Örnek 1 - Kullanıcı adına göre arama
 python Exporter.py --username "HaberSau" --maxtweets 1\n

 # Örnek 2 - Twite göre arama
 python Exporter.py --querysearch "sakarya" --maxtweets 1\n

 # Örnek 3 - Bir kullanıcının belirli bir tarihteki twitleri
 python Exporter.py --username "HaberSau" --since 2015-09-10 --until 2015-09-12 --maxtweets 1\n
 
 # Örnek 4 - Bir kullanıcnın son belli twitleri
 python Exporter.py --username "HaberSau" --maxtweets 10 --toptweets\n""")
        return

    try:
        opts, args = getopt.getopt(argv, "", ("username=", "since=", "until=", "query=", "toptweets", "maxtweets="))

        tweetCriteria = got3.manager.TweetCriteria()

        for opt, arg in opts:
            if opt == '--username':
                tweetCriteria.username = arg

            elif opt == '--since':
                tweetCriteria.since = arg

            elif opt == '--until':
                tweetCriteria.until = arg

            elif opt == '--query':
                tweetCriteria.querySearch = arg

            elif opt == '--toptweets':
                tweetCriteria.topTweets = True

            elif opt == '--maxtweets':
                tweetCriteria.maxTweets = int(arg)

        print('Aranıyor...\n')
        userid=100
        def receiveBuffer(tweets):
            for t in tweets:
                paramsTweet = (
                t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions,
                t.hashtags, t.id, t.permalink)
                paramUser = (t.username,t.retweets,t.favorites)
                c.execute("INSERT INTO Tweets VALUES(?,?,?,?,?,?,?,?,?,?,NULL)", paramsTweet)
                c.execute("INSERT INTO Users VALUES(?,?,?,?)",paramUser)
                conn.commit()

            print('Veritabanına %d tweet daha kaydedildi...\n' % len(tweets))

        got3.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)


    except arg:
        print('Parametre hatası -h parametresi ile yardım görüntüleyin!' + arg)
    finally:
        print('Başarıyla "TweetAnalysis.db" veritabanına kayıt edildi.')
        conn.close()


if __name__ == '__main__':
    main(sys.argv[1:])
