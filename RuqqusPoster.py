import praw, ruqqus, time, feedparser, sys, twitter

reddit = praw.Reddit(user_agent='CUM', client_id='CUM', client_secret='CUM',)
ruqqus = ruqqus.RuqqusClient(client_id='CUM', client_secret='CUM', refresh_token='CUM')
twitter = twitter.Api(consumer_key='CUM', access_token_key='CUM', access_token_secret='CUM', tweet_mode='extended')

subsandguilds = {
'prequelmemes': None,
'brawlhalla': None,
'therightcantmeme': None,
'androidapps': None,
'androidgaming': None,
'bogleheads': None,
'business': None,
'dataisbeautiful': None,
'finance': None,
'gamingnews': None,
'infographics': None,
'investing': None,
'martinshkreli': None,
'oldnews': None,
'passive_income': None,
'pcgaming': None,
'pets': None,
'portfolios': None,
'reclassified': None,
'samsung': None,
'stopgaming': None,
'themotte': None,
'thetagang': None,
'thewallstreet': None,
'unpopularfacts': None,
'technology': None,
'okbuddyretard': None,
'okbuddyredacted': None,
'greentext': None,
'privacy': None,
'interestingasfuck': None,
'historymemes': None,
'science': None,
'degoogle': None,
'darknet': None,
'animemes': None,
'history': None,
'piracy': None,
'linux': None,
'steam': None,
'minecraft': None,
'television': None,
'movies': None,
'wot': None,
'4chan': None,
'rarepuppers': None,
'wikipedia': None,
'cats': None,
'mapporn': None,
'amadisasters': None,
'ape': None,
'arabfunny': None,
'map_porn': 'mapporn',
'extrafabulouscomics': 'comics',
'transpassing': 'transcuties',
'politics': 'realnews',
'againsthatesubreddits': 'thememery',
'politicalhumor': 'thememery',
'traaaaaaannnnnnnnnns': 'trans',
'worldevents': 'realnews',
'hydrohomies': 'waterniggas',
'nomanshigh': 'nomanssky',
'nmsgalactichub': 'nomanssky',
'nomansskythegame': 'nomanssky',
'classicgreentext': 'greentext',
'games': 'gaming',
'gamingnews': 'gaming',
'okhistoryretard': 'historymemes',
'okbuddyhistoretard': 'historymemes',
'historydoge': 'historymemes',
'hobbydrama': 'deuxrama',
'gme_meltdown': 'gamestop',
'facts': 'unpoplularfacts',
'internationalbusiness': 'business',
'internetdrama': 'deuxrama',
'boglememes': 'bogleheads',
'DankMemesFromSite19': 'okbuddyredacted',
'SCPMemes': 'okbuddyredacted',
'dankmeme': 'dankmemes',
'dankmemes': 'dankmemes',
'dataisugly': 'dataisbeautiful',
'wallstreetbetsOGs': 'investing',
'daytrading': 'investing',
'dividends': 'investing',
'etfs': 'investing',
'options': 'investing',
'ipo': 'investing',
'spacs': 'investing',
'thetagang': 'investing',
'StockOfferings': 'investing'}

memesubs = 'Anti_Meme+Meme_Battles+memesec+boottoobig+fakehistoryporn+bertstrips+yahooanswers+BikiniBottomTwitter+biomememes+FunnyandSad+sciencememes+chemistrymemes+physicsmemes+biologymemes+Imgoingtorockbottom+justgirlythings+ledootgeneration+MemeEconomy+MEOW_IRL+ShittyQuotesPorn+teenagers+Teleshits+TooMeIrlForMeIrl+TrollCoping+WackyTicTacs+zuckmemes+seinfeldmemes+NotKenM+MemesOfTheGreatWar+smoobypost+vsaucememes+MemriTVmemes+dankjewishmemes+Jewdank+ExpandDong+bptcg+wholesomemes+patrig+dankcrusadememes+Spongebros+Minimalisticmemes+911fanart+NotTimAndEricPics+NapkinMemes+queenslandrail+WhatAWeeb+drugmemes+SadMemesForHipTeens+IncrediblesMemes+anthologymemes+privacymemes+billwurtzmemes+Demotivational+civmemes+me_ira+PornMemes+SFWporn+LabelMemes+interactivememes+FreshMemes+GoodFakeTexts+LegoGameMemes+specificmemes+Muttersunderbreath+SpideyMeme+TomAndJerryMemes+BPDmemes+DrakeAndJoshTwitter+waluigi+republicofdankmemes+dankmeme+raimimemes+virginvschad+schoolshootermemes+comedynecromancy+Memeconomy+Memes_Of_The_Dank+marvelmemes+meme+TheWaterLew+PornhubComments+SteamReviews+shittysteamreviews+NewVegasMemes+FalloutMemes+showsovergohome+SkyrimMemes+HolidaySpecialMemes+lotrmemes+MaymayZone+LegoSWmemes+WestworldMemes+GameOfThronesMemes+thronescomics+aSongOfMemesAndRage+blandmemesofreality+Overwatchmemes+dril+pokememes+pokemonmemes+NintendoMemes+rarepuppers+gamingmemes+MemeWorldWar+explicitmemes+darksoulsmemes+MassEffectmeme+MassEffectMemes+DisneyMemes'

feedsandguilds = {
'https://www.to-rss.xyz/wikipedia/current_events/': 'wikipedia',
'https://feeds.feedburner.com/DVDsReleaseDates': 'dvdsreleasedates',
'http://fetchrss.com/rss/5fab4317e88c9b130f62978260332c13300e6b01fa363952.xml': 'steam',
'https://store.steampowered.com/feeds/newshub/app/730/?cc=AR&l=english&snr=1_2108_9__1601': 'csgo',
'https://store.steampowered.com/feeds/newshub/app/334230/?cc=AR&l=english&snr=1_2108_9__1601': 'townofsalem',
'https://store.steampowered.com/feeds/newshub/app/629760/?cc=AR&l=english&snr=1_2108_9__1601': 'mordhau',
'https://store.steampowered.com/feeds/newshub/app/291550/?cc=AR&l=english&snr=1_2108_9__1601': 'brawlhalla',
'https://www.factcheck.org/rss': 'factcheck', 
'https://www.youtube.com/feeds/videos.xml?channel_id=UCVpankR4HtoAVtYnFDUieYA': 'videos', 
'https://www.youtube.com/feeds/videos.xml?channel_id=UC3M9CX5HWSw25k5QL3FkDEA': 'music', 
'https://www.youtube.com/feeds/videos.xml?channel_id=UCE48xWPBV59NFsnrK5bmykw': 'music', 
'https://www.youtube.com/feeds/videos.xml?channel_id=UCx-dJoP9hFCBloY9qodykvw': 'history', 
'https://www.youtube.com/feeds/videos.xml?channel_id=UCv_vLHiWVBh_FR9vbeuiY-A': 'history', 
'https://www.youtube.com/feeds/videos.xml?channel_id=UC8MX9ECowgDMTOnFTE8EUJw': 'history', 
'https://www.youtube.com/feeds/videos.xml?channel_id=UCMmaBzfCCwZ2KqaBJjkj0fw': 'history', 
'https://babylonbee.com/feed': 'satire',
'https://thehardtimes.net/feed/': 'satire',
'https://reductress.com/feed/': 'satire',
'https://www.theonion.com/rss': 'satire',
'http://feeds.foxbusiness.com/foxbusiness/latest': 'investing', 
'https://finance.yahoo.com/news/rssindex': 'investing', 
'https://www.etf.com/home.feed/feed': 'investing', 
'https://seekingalpha.com/listing/most-popular-articles.xml': 'investing',
'https://seekingalpha.com/feed/etfs-and-funds': 'investing',
'https://seekingalpha.com/api/sa/combined/BUZZ.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/BRK.A.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/BRK.B.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/MSOS.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/TLT.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/AMC.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/GME.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/FAS.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/MOON.xml': 'investing',
'https://seekingalpha.com/api/sa/combined/SPXL.xml': 'investing'}

while True:
	print('Mirroring subreddits...')
	for sub, guild in subsandguilds.items():
		n = 0
		if guild == None: guild = sub
		for p in reddit.subreddit(sub).top('day', limit=5):
			if p.is_self or 'reddit.com/gallery' in p.url or 'v.redd' in p.url or 'u/' in p.title or 'r/' in p.title or 'reddit' in p.title: continue
			try:
				post = ruqqus.submit_post(guild=guild, url=p.url, title=p.title)['permalink']
				print(f"ruqqus.com{post}")
			except Exception as e: print(e)

	print('Mirroring r/drama...')
	for p in reddit.subreddit('drama').top('day'):
		if p.is_self: continue
		try:
			post = ruqqus.submit_post(guild='deuxrama', url=p.url, title=p.title.replace('/r/drama', 'deux').replace('r/drama', 'deux').replace('/drama', 'deux'))['permalink']
			print(f"ruqqus.com{post}")
		except Exception as e: print(e)
		
	print('Posting memes')
	for p in reddit.subreddit(memesubs).hot(limit=3):
		if p.is_self or 'reddit.com/gallery' in p.url or 'v.redd' in p.url or 'u/' in p.title or 'r/' in p.title or 'reddit' in p.title: continue
		try:
			post = ruqqus.submit_post(guild='dankmemes', url=p.url, title=p.title)['permalink']
			print(f"ruqqus.com{post}")
		except Exception as e: print(e)
	
	print('Posting RSS feeds..')	
	for feed, guild in feedsandguilds.items():
		for item in feedparser.parse(feed).entries:
			try: 
				post = ruqqus.submit_post(guild=guild, url=item.link, title=item.title)['permalink']
				print(f"ruqqus.com{post}")
			except Exception as e: 
				print(e)
				break
				
	print('Posting tweets..')
	for user, guild in {'elonmusk': 'elonmusk', 'cathiedwood': 'personalrssfeed'}.items():
		for tweet in twitter.GetUserTimeline(screen_name=user):
			try: 
				post = ruqqus.submit_post(guild=guild, url=f'https://twitter.com/{user}/status/{tweet.id}', title=f'@{user}: {tweet.full_text}')['permalink']
				print(f'ruqqus.com{post}')
			except Exception as e:
				print(e)
				break

	print('Sleeping...')
	time.sleep(600)
