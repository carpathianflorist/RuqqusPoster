import praw, time, feedparser, sys, twitter, requests, json, ous

reddit = praw.Reddit(user_agent='hey', client_id='PUT YOUR REDDIT CLIENT ID HERE', client_secret='PUT YOUR REDDIT CLIENT SECRET HERE',)
data={'client_id': 'PUT YOUR RUQQUS CLIENT ID HERE',
	'client_secret': 'PUT YOUR RUQQUS CLIENT SECRET HERE',
	'grant_type': 'refresh',
	'refresh_token': 'PUR YOUR RUQQUS REFERESH TOKEN HERE, GET IT FROM HERE https://ruqqus-auth.glitch.me'
}

directory = os.path.dirname(os.path.realpath(__file__))
urls = open(f'{directory}/urls.txt', encoding='utf8').read()
titles = open(f'{directory}/titles.txt', encoding='utf8').read()

subsandguilds = {
'prequelmemes': None,
'brawlhalla': None,
'therightcantmeme': None,
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
'stupidpol': None,
'marvel': None,
'virginvschad': None,
'starterpacks': None,
'Eyebleach': None,
'politicalcompassmemes': None,
'breakingbad': None,
'GameofThrones': None,
'apexlegends': None,
'overwatch': None,
'tf2': None,
'Valorant': None,
'csgo': None,
'dogs': None,
'deadbydaylight': None,
'ark': None,
'amongus': None,
'dota2': None,
'PUBG': None,
'Rainbow6': None,
'valheim': None,
'GTAV': None,
'warframe': None,
'music': None,
'cryptocurrency': None,
'showerthoughts': None,
'unpopularopinion': None,
'todayilearned': None,
'bitcoin': None,
'hobbydrama': None,
'GoldandBlack': 'PrincipledAggression',
'Catholicism': 'insanepeoplereddit',
'Christianity': 'insanepeoplereddit',
'crime': 'crimeandmystery',
'antifastonetoss': 'stonetoss',
'smugideologyman': 'smuggies',
'DestinyTheGame': 'Destiny',
'playrust': 'rust',
'FitToFat': 'fatpeoplehate',
'map_porn': 'mapporn',
'extrafabulouscomics': 'comics',
'transpassing': 'transcuties',
'againsthatesubreddits': 'thememery',
'politicalhumor': 'thememery',
'traaaaaaannnnnnnnnns': 'trans',
'worldevents': 'worldnews',
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
'facts': 'unpoplularfacts',
'internationalbusiness': 'business',
'internetdrama': 'deuxrama',
'boglememes': 'bogleheads',
'DankMemesFromSite19': 'okbuddyredacted',
'SCPMemes': 'okbuddyredacted',
'dankmeme': 'memes',
'dankmemes': 'memes',
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

memesubs = 'Anti_Meme+Meme_Battles+memesec+boottoobig+fakehistoryporn+bertstrips+yahooanswers+BikiniBottomTwitter+biomememes+FunnyandSad+sciencememes+chemistrymemes+physicsmemes+biologymemes+Imgoingtorockbottom+justgirlythings+ledootgeneration+MemeEconomy+ShittyQuotesPorn+teenagers+Teleshits+TrollCoping+WackyTicTacs+zuckmemes+seinfeldmemes+NotKenM+MemesOfTheGreatWar+smoobypost+vsaucememes+MemriTVmemes+dankjewishmemes+Jewdank+ExpandDong+bptcg+wholesomemes+patrig+dankcrusadememes+Spongebros+Minimalisticmemes+911fanart+NotTimAndEricPics+NapkinMemes+queenslandrail+WhatAWeeb+drugmemes+SadMemesForHipTeens+IncrediblesMemes+anthologymemes+privacymemes+billwurtzmemes+Demotivational+civmemes+me_ira+PornMemes+SFWporn+LabelMemes+interactivememes+FreshMemes+GoodFakeTexts+LegoGameMemes+specificmemes+Muttersunderbreath+SpideyMeme+TomAndJerryMemes+BPDmemes+DrakeAndJoshTwitter+waluigi+republicofdankmemes+dankmeme+raimimemes+virginvschad+schoolshootermemes+comedynecromancy+Memeconomy+Memes_Of_The_Dank+marvelmemes+meme+TheWaterLew+PornhubComments+SteamReviews+shittysteamreviews+NewVegasMemes+FalloutMemes+showsovergohome+SkyrimMemes+HolidaySpecialMemes+lotrmemes+MaymayZone+LegoSWmemes+WestworldMemes+GameOfThronesMemes+thronescomics+aSongOfMemesAndRage+blandmemesofreality+Overwatchmemes+dril+pokememes+pokemonmemes+NintendoMemes+norules+197+198+199+memecesspool+gamingmemes+MemeWorldWar+explicitmemes+darksoulsmemes+MassEffectmeme+MassEffectMemes+DisneyMemes'

feedsandguilds = {
'https://www.to-rss.xyz/wikipedia/current_events/': 'wikipedia',
'https://feeds.feedburner.com/DVDsReleaseDates': 'dvdsreleasedates',
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
'https://www.theonion.com/rss': 'satire',
'http://feeds.foxbusiness.com/foxbusiness/latest': 'personalrssfeed', 
'https://finance.yahoo.com/news/rssindex': 'personalrssfeed', 
'https://www.etf.com/home.feed/feed': 'personalrssfeed', 
'https://seekingalpha.com/listing/most-popular-articles.xml': 'personalrssfeed',
'https://seekingalpha.com/feed/etfs-and-funds': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/BUZZ.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/BRK.A.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/BRK.B.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/MSOS.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/TLT.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/AMC.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/GME.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/FAS.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/MOON.xml': 'personalrssfeed',
'https://seekingalpha.com/api/sa/combined/SPXL.xml': 'personalrssfeed'}

while True:
	accesstoken = json.loads(requests.post('https://ruqqus.com/oauth/grant', headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}, data = data).text)['access_token']
	headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 'Authorization': f'Bearer {accesstoken}'}

	print('Mirroring subreddits...')
	for sub, guild in subsandguilds.items():
		n = 0
		if guild == None: guild = sub
		for p in reddit.subreddit(sub).top('day'):
			if p.is_self and guild != 'personalrssfeed' and guild != 'hobbydrama': continue
			if p.over_18 or p.is_original_content or p.url in urls or p.title in titles or 'Hobby Scuffles' in p.title: continue
			c = 0
			for filter in ['gifv','gfycat', 'v.redd', 'reddit.com/gallery']:
				if filter in p.url:
					c = 1
					break
			for filter in ['i ', 'we ','my ', '[oc]', '(oc)', 'u/', 'r/', 'reddit', '?']:
				if f' {filter}' in p.title.lower() or p.title.lower().startswith(filter):
					c = 1
					break
			if c == 1: continue
			if p.is_self and guild == 'hobbydrama': requests.post('https://ruqqus.com/api/v1/submit', headers=headers, data={'body':p.selftext, 'title':p.title, 'board':guild})
			else: post = requests.post('https://ruqqus.com/api/v1/submit', headers=headers, data={'url':p.url, 'title':p.title, 'board':guild})
			urls += f'{p.url}\n'
			titles += f'{p.title}\n'
			try: postid = json.loads(post.text)['id']
			except Exception as e:
				if 'Expecting value: line 1 column 1 (char 0)' in str(e): print(e)
				else: print(post.text)
				continue
			print(f'ruqqus.com/post/{postid}')
			n += 1
			if n == 5:
				print('Sleeping...')
				time.sleep(360)
				break

	print('Mirroring r/drama...')
	for p in reddit.subreddit('drama').top('day'):
		if p.over_18 or p.is_self or p.url in urls or p.title in titles or 'u/' in p.title: continue
		title = p.title.replace('/r/drama', 'deux').replace('r/drama', 'deux').replace('/drama', 'deux')
		post = requests.post('https://ruqqus.com/api/v1/submit', headers=headers, data={'url':p.url, 'title':title, 'board':'deuxrama'})
		urls += f'{p.url}\n'
		titles += f'{p.title}\n'
		try: postid = json.loads(post.text)['id']
		except Exception as e:
			print(e)
			continue
		print(f'ruqqus.com/post/{postid}')
		
	print('Posting memes')
	for p in reddit.subreddit(memesubs).hot(limit=10):
		if p.over_18 or p.is_self or p.url in urls or p.title in titles or 'reddit.com/gallery' in p.url or 'v.redd' in p.url: continue
		post = requests.post('https://ruqqus.com/api/v1/submit', headers=headers, data={'url':p.url, 'title':p.title, 'board':'memes'})
		urls += f'{p.url}\n'
		titles += f'{p.title}\n'
		try: postid = json.loads(post.text)['id']
		except Exception as e:
			print(e)
			continue
		print(f'ruqqus.com/post/{postid}')
	
	print('Posting RSS feeds..')	
	for feed, guild in feedsandguilds.items():
		for item in feedparser.parse(feed).entries:
			if item.link in urls or item.title in titles: break
			if 'marketwatch' in item.link: continue
			post = requests.post('https://ruqqus.com/api/v1/submit', headers=headers, data={'url':item.link, 'title':item.title, 'board':guild})
			urls += f'{item.link}\n'
			titles += f'{item.title}\n'
			try: postid = json.loads(post.text)['id']
			except Exception as e:
				print(e)
				break
			print(f'ruqqus.com/post/{postid}')

	print('Posting tweets..')
	for user, guild in {'elonmusk': 'elonmusk', 'cathiedwood': 'arkinvest'}.items():
		for tweet in twitter.GetUserTimeline(screen_name=user):
			url = f'https://twitter.com/{user}/status/{tweet.id}'
			title = f'@{user}: {tweet.full_text}'
			if url in urls or title in titles: break
			post = requests.post('https://ruqqus.com/api/v1/submit', headers=headers, data={'url':url, 'title':title, 'board':guild})
			urls += f'{url}\n'
			titles += f'{title}\n'
			try: postid = json.loads(post.text)['id']
			except Exception as e:
				print(e)
				break
			print(f'ruqqus.com/post/{postid}')

	open(f'{directory}/urls.txt', encoding='utf-8', mode='w').write(urls)
	open(f'{directory}/titles.txt', encoding='utf-8', mode='w').write(titles)
