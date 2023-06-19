from Texo.Sentimental.Analysis import Sentitweeten
from Texo.Sentimental.Analysis import Sentitweethn
from Texo.Sentimental.Analysis import Sentitweetsp
from Texo.Sentimental.Analysis import Sentitweetgn
from Texo.Sentimental.Analysis import Sentitweetkn
from Texo.Word.texo import tex


x = tex()

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla at ligula diam. " \
       "Sed vel nibh ut purus sagittis tincidunt. Sed non lectus posuere, ullamcorper arcu nec, " \
       "elementum ipsum. Phasellus ut aliquam ligula. Duis sed tellus eget massa pulvinar " \
       "eleifend eu et augue. Nam pretium, tortor ac gravida malesuada, quam mauris tempor est, " \
       "et eleifend tortor mauris in dui. Vivamus ut pulvinar mauris, eget fermentum metus. " \
       "Cras nec varius ipsum. Sed sed neque vel ante vulputate gravida id a nisl. " \
       "Praesent facilisis imperdiet elit at rhoncus. Morbi ac scelerisque risus."

summary = x.summary(text, num_bullet_points=10)
print(summary)
