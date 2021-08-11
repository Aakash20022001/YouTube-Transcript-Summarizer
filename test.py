import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest


nlp = spacy.load("en_core_web_sm")

doc = '''This program is brought to you by Stanford University.Please visit us at stanford.eduThank You. I am honored to be with you today at your commencementfrom one
of the finest universities in the world.Truth be told I never graduated from collegeand this is the closest I've ever gotten to a college graduation.Today I want to tell you three stories from my life. That's it.No big deal. Just three stories.The first story is about connecting the dots.I dropped out of Reed College after the first 6 months,but then stayed around as a drop-infor another 18 months or so before I really quit.So why did I drop out?It started before I was born.My biological mother was a young, unwed graduate student,and she decided to put me up for adoption.She felt very strongly that I should be adopted by college graduates,so everything was all set for me tobe adopted at birth by a lawyer and his wife.Except that when I popped out they decidedat the last minute that they really wanted a girl.So my parents, who were on a waiting list,got a call in the middle of the night asking: "We have an unexpectedbaby boy; do you want him?"They said: "Of course." My biological mother later found out thatmy mother had never graduated from collegeand that my father had never graduated from high school.She refused to sign the final adoption papers.She only relented a few months later whenmy parents promised that I would go to college. This was the start in my life.And 17 years later I did go to college. But I naively chose a collegethat was almost as expensive as Stanford,and all of my working-class parents'savings were being spent on my college tuition.After six months, I couldn't see the value in it.I had no idea what I wanted to do with my lifeand no idea how college was going to help me figure it out.And here I was spending all of the money my parents had savedtheir entire life.So I decided to drop out and trust that it would all work out OK.It was pretty scary at the time,but looking back it was one of the best decisions I ever made.The minute I dropped out I could stoptaking the required classes that didn't interest me,and begin dropping in on the ones that looked interesting.It wasn't all romantic. I didn't have a dorm room,so I slept on the floor in friends' rooms,I returned coke bottles for the 5 cent deposits to buy food with,and I would walk the 7 miles across town every Sundaynight to get one good meal a week at the Hare Krishnatemple. I loved it.And much of what I stumbled into by followingmy curiosity and intuition turned out to be priceless later on.Let me give you one example: Reed College at thattime offered perhaps the best calligraphy instruction in the country.Throughout the campus every poster, every label on every drawer,was beautifully hand calligraphed.Because I had dropped out and didn't have to take the normal classes,I decided to take a calligraphy class to learn how to do this.I learned about serif and san serif typefaces,about varying the amount of spacebetween different letter combinations,about what makes great typography great.It was beautiful, historical,artistically subtle in a way that science can't capture,and I found it fascinating.None of this had even a hope of any practical application in my life.But ten years later,when we were designing the first Macintosh computer,it all came back
to me. And we designed it all into the Mac.It was the first computer with beautiful typography.If I had never dropped in on that single course in college,the Mac would have never had multipletypefaces or proportionally spaced fonts.And since Windows just copied the Mac,it's likely that no personal computer would have them.If I had never dropped out,I would have never dropped in on this calligraphy class,and personal computers might not have the wonderful typographythat they do. Of course it was impossible to connectthe dots looking forward when I was in college.But it was very, very clear looking backwards ten years later.Again, you can't connect the dots looking forward;you can only connect them looking backwards.So you have to trust that the dots will somehow connectin your future.You have to trust in something, your gut, destiny, life, karma,whatever.Beleiveing that the dots will connect down the road will give you the confidence to follow your heartEven when it leads you off the well worn path, and that will make all the difference.My second story is about love and loss.I was lucky I found what I loved to do early in life.Woz and I started Apple in my parents garage when I was 20.We worked hard, and in 10 years Apple had grown from just the two ofus in a garage into a $2 billion company with over 4000 employees.We had just released our finest creation the Macintosha year earlier, and I had just turned 30.And then I got fired.How can you get fired from a company you started?Well, as Apple grew we hired someone who I thoughtwas very talented to run the company with me,and for the first year or so things went well.But then our visions of the future beganto diverge and eventually we had a falling out.When we did, our Board of Directors sided with him.So at 30 I was out. And very publicly out.What had been the focus of my entire adult life was gone,and it was devastating.I really didn't know what to do for a few months.I felt that I had let the previous generation of entrepreneursdown - that I had dropped the baton as it was being passed to me.I met with David Packard and Bob Noyceand tried to apologize for screwing up so badly.I was a very public failure,and I even thought about running
away from the valley.But something slowly began to dawn on me I still loved what I did.The turn of events at Apple had not changed that one bit.I had been rejected, but I was still in love.And so I decided to start over.I didn't see it then, but it turned out that getting fired fromApple was the best thing that could have ever happened to me.The heaviness of being successful wasreplaced by the lightness of being a beginner again,less sure about everything.It freed me to enter one of the most creative periods of my life.During the next five years, I started a company named NeXT,another company named Pixar,and fell in love with an amazing woman who would become my wife.Pixar went on to create the worlds first computer animated featurefilm, Toy Story,and is now the most successful animation studio in the world.In a remarkable turn of events, Apple bought NeXT,I returned to Apple, and the technology we developed atNeXT is at the heart of Apple's current renaissance.And Laurene and I have a wonderful family together.I'm pretty sure none of this wouldhave happened if I hadn't been fired from Apple.It was awful tasting medicine, but I guess the patient needed it.Sometimes life hits you in the head with a brick. Don't lose faith.I'm convinced that the only thing that kept me going was that I lovedwhat I did. You've got to find what you love.And that is as true for your work as it is for your lovers.Your work is going to fill a large part of your life,and the only way to be truly satisfiedis to do what you believe is great work.And the only way to do great work is to love
what you do.If you haven't found it yet, keep looking. Don't settle.As with all matters of the heart, you'll know when you find it.And, like any great relationship,it just gets better and better as the years roll on.So keep looking. Don't settle.My third story is about death.When I was 17, I read a quote that went something like:"If you live each day as if it was your last,someday you'll most certainly be right."It made an impression on me, and since then, for the past 33
years,I have looked in the mirror every morningand asked myself: "If today were the last day of my life,would I want to do what I am about to do today?"And whenever the answer has been "No" for too many days in a row,I know I need to change something.Remembering that I'll be dead soon is the most importanttool I've ever encountered to help me make the big choices in life.Because almost everything all external expectations, all pride,all fear of embarrassment or failure -these things just fall away in the face of death,leaving only what is truly important.Remembering that you are going to die is the bestway I know to avoid the trap of thinking you have something to lose.You are already naked. There is no reason not to follow your heart.About a year ago I was diagnosed with cancer.I had a scan at 7:30 in the morning,and it clearly showed a tumor on my pancreas.I didn't even know what a pancreas was.The doctors told me this was almostcertainly a type of cancer that is incurable,and that I should expect to live no longer than three to six months.My doctor advised me to go home and get my affairs in order,which is doctor's code for prepare to die.It means to try to tell your kids everything you thoughtyou'd have the next 10 years to tell them in just a few
months.It means to make sure everything is buttonedup so that it will be as easy as possible for your family.It means to say your goodbyes.I lived with that diagnosis all day.Later that evening I had a biopsy,where they stuck an endoscope down my throat,through my stomach and into my intestines,put a needle into my pancreas and got a few cells from the tumor.I was sedated, but my wife, who was there,told me that when they viewed the cells under a microscopethe doctors started crying because it turned out to bea very rare form of pancreatic cancer that is curable with surgery.I had the surgery and thankfully I'm fine now.This was the closest I've been to facing death,and I hope its the closest I get for a few more decades.Having lived through it,I can now say this to you with a bit more certainty than whendeath was a useful but purely intellectual concept:No one wants to die.Even people who want to go to heaven don't want to die to get there.And yet death is the destination we all share.No one has ever escaped it. And that is as it should be,because Death is very likely the single best invention of Life.It is Life's change agent.It clears out the old to make way for the new.Right now the new is you, but someday not too long from now,you will gradually become the old and be cleared away.Sorry to be so dramatic, but it is quite true.Your time is limited, so don't waste it living someone else's life.Don't be trapped by dogma which is livingwith the results of other people's thinking.Don't let the noise of others' opinions drown out your own innervoice. And most important,have the courage to follow your heart and intuition.They somehow already know what you truly want to become.Everything else is secondary.When I was young,there was an amazing publication called The Whole Earth Catalog,which was one of the bibles of my generation.It was created by a fellow named Stewart Brand not
far from herein Menlo Park, and he brought it to life with his poetic touch.This was in the late 1960's,before personal computers and desktop publishing,so it
was all made with typewriters, scissors, and polaroid cameras.It was sort of like Google in paperback form,35 years before Google came along: it was idealistic,overflowing with neat tools, and great notions.Stewart and his team put out severalissues of The Whole Earth Catalog,and then when it had run its course, they put out a final issue.It was the mid-1970s, and I was your age.On the back cover of their final issuewas a photograph of an early morning country road,the kind you might find yourselfhitchhiking on if you were so adventurous.Beneath it were the words: "Stay Hungry. Stay Foolish."It was their farewell message as they signed off. Stay Hungry.Stay Foolish. And I have always wished that for myself.And now, as you graduate to begin anew, I wish that for you.Stay Hungry. Stay Foolish.Thank you all very much.The preceding program is copyrighted by Stanford University.Please visit us at stanford.edu'''


doc = nlp(doc)

#print(doc)

print(len(list(doc.sents)))

keyword = []

stopwords = list(STOP_WORDS)

#print(stopwords)

pos_tag = ["PROPN","ADJ","NOUN","VERB"]

for token in doc:
    if (token.text in stopwords or token.text in punctuation):
        continue

    if (token.pos_ in pos_tag):
        keyword.append(token.text)

#print(keyword)

freq_word = Counter(keyword)
#print(freq_word.most_common(10))

max_freq = Counter(keyword).most_common(1)[0][1]

for word in freq_word.keys():
    freq_word[word] = (freq_word[word]/max_freq)

#print(freq_word.most_common(5))

sent_strength = {}
for sent in doc.sents:
    for word in sent:
        if word.text in freq_word.keys():
            if sent in sent_strength.keys():
                sent_strength[sent]+=freq_word[word.text]
            else:
                sent_strength[sent] = freq_word[word.text]

#print(sent_strength)

summarized_sentences = nlargest(3,sent_strength,key = sent_strength.get)
print(summarized_sentences)
