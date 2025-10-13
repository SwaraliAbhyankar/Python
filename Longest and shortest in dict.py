dict1={'piece':'portion of an object or a material produced by cutting',
       'patch':'piece of cloth or material used to mend or strengthen the damaged part',
       'area':'a region or part of a town or a country or the world',
       'visit':'go to see and spend time with something or someone',
       'small':'less than normal'}

keys=list(dict1.keys())
values=list(dict1.values())
length=[len(x) for x in values]

max_len=max(length)
min_len=min(length)

max_index=length.index(max_len)
min_index=length.index(min_len)

print("Max:- ",keys[max_index], ':', values[max_index])
print('Min:- ',keys[min_index],':', values[min_index])
