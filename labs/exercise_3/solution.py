import csv

csvfile = open( 'rock.csv' )
reader  = csv.DictReader( csvfile ) # not a list, an iterable
rows    = [row for row in reader] # npa: look up list comprehension

# How many songs were released in 1981?
released_1981 = 0
for row in rows:
    if row['Release Year'] == '1981':
        released_1981 += 1

# npa: this needs at least 2 spaces or it will throw an error in console
print released_1981
# 61 songs 




# What are the top 20 songs by playcount?
sorted_playcounts = sorted( rows, 
                            key = lambda row: int( row['PlayCount'] ), 
                            reverse = True )
top_20 = sorted_playcounts[0:19]
print top_20
