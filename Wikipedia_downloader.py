#   https://dumps.wikimedia.org/itwiki/latest/
import wikipedia

with open('itwiki-latest-all-titles-in-ns0') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]


wikipedia.set_lang("it")
counter = 1
for article in content:
    print('{} out of {}'.format(counter, content.__len__()))
    try:
        article_text = wikipedia.page(article)
        with open("IT_Wikipedia.txt", "a") as myfile:
            myfile.write(article_text.content.replace("\n", "")+"\n")
    except:
        continue
    finally:
        counter = counter + 1


#ny = wikipedia.page("Italy")
#ny.content