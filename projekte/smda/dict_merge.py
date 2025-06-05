#print(result)

lon= 99
lat = 'l2'


tags = {'name':'sven'}
tags = {**tags, **{'lon':lon, 'lon':lat}} # Python >=3.5

print (tags)


foo = {'lon':lon, 'lon':lat}
bar = {'name': 'Teddy R.'}

print(foo|bar) # Python >=3.9

print(tags.items())