import graphlab as gl

# Load the data
songs = gl.SFrame.read_csv("http://s3.amazonaws.com/dato-datasets/millionsong/song_data.csv")

usage_data = gl.SFrame.read_csv("http://s3.amazonaws.com/dato-datasets/millionsong/10000.txt",
                                header=False,
                                delimiter='\t',
                                column_type_hints={'X3':int})

usage_data.rename({'X1':'user_id', 'X2':'song_id', 'X3':'listen_count'})
usage_data.save('./music_usage_data')
same_usage_data = gl.load_sframe('./music_usage_data')

songs['year'] = songs['year'].apply(lambda x: None if x == 0 else x)
songs.head(5)

songs['love_count'] = songs[['title', 'artist_name']].apply(
    lambda row: sum(x.lower().split(' ').count('love') for x in row.values()))
songs.topk('love_count', k=5)

songs['year'].sketch_summary()

songs['year'].show()