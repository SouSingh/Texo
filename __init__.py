from Texo.Sentimental.Analysis import Sentitweeten
from Texo.Sentimental.Analysis import Sentitweethn
from Texo.Sentimental.Analysis import Sentitweetsp
from Texo.Sentimental.Analysis import Sentitweetgn
from Texo.Sentimental.Analysis import Sentitweetkn
from Texo.Word.texo import tex


x = tex()

text = "In literary theory, a text is any object that can be  whether this object is a work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing. " \
       "It is a coherent set of signs that transmits some kind of informative message." \
       "This set of signs is considered in terms of the informative message's content, rather than in terms of its physical form or the medium in which it is represented.  " \
       "Within the field of literary criticism, also refers to the original information content of a particular piece of writing; that is, the "text" of a work is that primal symbolic arrangement of letters as originally composed, apart from later alterations, deterioration, commentary, translations, paratext, etc." \
       "et eleifend tortor mauris in dui. Vivamus ut pulvinar mauris, eget fermentum metus. " \
       "Cras nec varius ipsum. Sed sed neque vel ante vulputate gravida id a nisl. " \
       "Praesent facilisis imperdiet elit at rhoncus. Morbi ac scelerisque risus."

summary = x.summary(text, num_bullet_points=10)
print(summary)
