from os import read
import regex

attempt = "12"

readfile = open("brown-tagged-part1.txt")
writefile = open("brown-neutralized-part1_" + attempt + ".txt", "w+")

text = readfile.read()

text = regex.sub("\\b([Hh]e|[Ss]he)_PPS\\b", "they_PPS", text)
text = regex.sub("\\b([Hh]e's|[Ss]he's)_PPS\\+BEZ\\b", "they're_PPS+BER", text)
text = regex.sub("\\b([Hh]e's|[Ss]he's)_PPS\\+HVZ\\b", "they've_PPS+HV", text)
text = regex.sub("\\b([Hh]e'll|[Ss]he'll)_PPS\\+MD\\b", "they'll_PPS+MD", text)

text = regex.sub("\\b([Hh]im|[Hh]er)_PPO\\b", "them_PPO", text)
text = regex.sub("\\b([Hh]is|[Hh]ers)_PP\\$\\$\\B", "theirs_PP$$", text)
text = regex.sub("\\b([Hh]is|[Hh]er)_PP\\$\\B", "their_PP$", text)
text = regex.sub("\\b([Hh]imself|[Hh]erself)_PPL\\b", "themself_PPL", text)

text = regex.sub("([Ww]oman|(?<![Hh]u)[Mm]an)(?=('s)?_(?!NP))", "person", text)
text = regex.sub("([Ww]omen|[Mm]en)(?=('s)?_(NNS|NPS))", "people", text)

text = regex.sub("([Gg]irl|[Bb]oy)(?=_(NN))", "child", text)
text = regex.sub("([Gg]irls|[Bb]oys)(?=_(NNS))", "children", text)
text = regex.sub("([Gg]irls'|[Bb]oys')(?=_(NNS\\$))", "children's", text)

writefile.write(text)