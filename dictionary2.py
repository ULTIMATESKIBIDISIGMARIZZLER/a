e=input("type")
words=e.lower().split()
words_count={}

for word in words:
    if word in words_count:
        words_count[word]+=1
    else:
        words_count[word]=1

sort=list(words_count.items())

for i in range(len(sort)):
    for j in range(0, len(sort)-i-1):
        if sort[j][1]<sort[j+1][1]:    
           sort[j],sort[j+1]=sort[j+1],sort[j]
#top 100           
top1=sort[:1]
top10=sort[:10]           
top20=sort[:20]
top30=sort[:30]
top40=sort[:40]
top50=sort[:50]
top60=sort[:60]
top70=sort[:70]           
top80=sort[:80]
top90=sort[:90]
top100=sort[:100]

print("top 1 word", top1)
print("top 10 words", top10)
print("top 20 words", top20)
print("top 30 words", top30)
print("top 40 words", top40)
print("top 50 words", top50)
print("top 60 words", top60)
print("top 70 words", top70)
print("top 80 words", top80)
print("top 90 words", top90)
print("top 100 words", top100)