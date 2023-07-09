


class tex():

    def __init__(self):
        self.x = 10
        self.stop_words = {
    'a', 'an', 'and', 'the', 'in', 'on', 'is', 'are', 'it', 'of', 'to', 'that', 'this', 'with',
    'for', 'as', 'at', 'by', 'from', 'or', 'not', 'but', 'be', 'was', 'were', 'am', 'has', 'have',
    'had', 'can', 'could', 'will', 'would', 'should', 'you', 'he', 'she', 'they', 'we', 'your', 'their',
    'our', 'my', 'his', 'her', 'its', 'there', 'here',
    'about', 'above', 'after', 'again', 'against', 'all', 'also', 'anew', 'any', 'away', 'back', 'backward',
    'because', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond', 'both', 'but', 'come',
    'down', 'during', 'each', 'end', 'few', 'first', 'forward', 'further', 'get', 'go', 'good', 'great',
    'had', 'has', 'having', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'into',
    'itself', 'last', 'like', 'many', 'me', 'more', 'most', 'much', 'myself', 'near', 'need', 'new', 'next',
    'no', 'not', 'now', 'now', 'onward', 'or', 'other', 'our', 'ours', 'out', 'over', 'own', 'same',
    'shall', 'she', 'should', 'since', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'them',
    'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'toward', 'under', 'until', 'up',
    'upon', 'us', 'very', 'we', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'whose', 'why',
    'will', 'with', 'within', 'without', 'would', 'yes', 'you', 'your',
    'able', 'across', 'actually', 'afterwards', 'almost', 'already', 'although', 'always', 'among',
    'amongst', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'because', 'become', 'becomes',
    'becoming', 'been', 'beforehand', 'behind', 'being', 'besides', 'beyond', 'certain', 'clearly',
    'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains',
    'corresponding', 'course', 'currently', 'definitely', 'despite', 'downwards', 'during', 'elsewhere',
    'entirely', 'especially', 'et', 'etc', 'everybody', 'everyone', 'everything', 'everywhere', 'exactly',
    'example', 'except', 'far', 'fifth', 'finally', 'followed', 'following', 'follows', 'former', 'formerly',
    'forth', 'four', 'furthermore', 'hence', 'hereafter', 'hereby', 'herein', 'hereupon', 'herself',
    'himself', 'hither', 'hopefully', 'however', 'i.e.', 'ie', 'ignored', 'immediate', 'inasmuch', 'indeed',
    'indicate', 'indicated', 'indicates', 'inner', 'insofar', 'itself', 'kept', 'lately', 'later', 'latter',
    'latterly', 'lest', 'liked', 'likewise', 'longer', 'meanwhile', 'merely', 'moreover', 'myself', 'namely',
    'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'next', 'nine', 'nobody', 'none',
    'nonetheless', 'nothing', 'nowhere', 'obviously', 'often', 'okay', 'once', 'onto', 'otherwise', 'ought',
    'ourselves', 'out', 'outside', 'over', 'particular', 'particularly', 'please', 'plus', 'possible',
    'presumably', 'probably', 'quite', 'rather', 'regarding', 'right', 'second', 'seem', 'seemed', 'seeming',
    'seems', 'seen', 'self', 'selves', 'several', 'shall', 'sincere', 'six', 'someone', 'something',
    'sometimes', 'somewhat', 'somewhere', 'specified', 'specify', 'specifying', 'still', 'sub', 'such',
    'suppose', 'supposed', 'supposes', 'sure', 'take', 'taken', 'tell', 'tends', 'th', 'thank', 'thanks',
    'thanx', 'that', 'thats', 'theirs', 'themselves', 'then', 'thence', 'thereafter', 'thereby', 'therefore',
    'therein', 'theres', 'thereupon', 'theyd', 'theyre', 'third', 'thorough', 'thoroughly', 'those', 'though',
    'throughout', 'thru', 'thus', 'together', 'too', 'toward', 'towards', 'truly', 'try', 'trying', 'twice',
    'two', 'underneath', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'upon', 'useful',
    'usefully', 'usefulness', 'usually', 'various', 'via', 'want', 'wants', 'wasnt', 'way', 'wed',
    'welcome', 'well', 'went', 'were', 'werent', 'what', 'whats', 'whatever', 'when', 'whence',
    'whenever', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether',
    'which', 'whichever', 'while', 'whither', 'whoever', 'whos', 'whose', 'why', 'whys', 'widely',
    'willing', 'wish', 'within', 'without', 'whom', 'whoever', 'wouldnt', 'yes', 'yet', 'youre', 'yours',
    'yourself', 'yourselves',
    'un', 'under', 'until', 'unto', 'up', 'upon', 'us', 'very', 'via', 'viz',
    'want', 'wants', 'was', 'wasn', 'wasnt', 'way', 'we', 'wed', 'welcome', 'well', 'went', 'were',
    'weren', 'werent', 'what', 'whats', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter',
    'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither',
    'who', 'whoever', 'whole', 'whom', 'whomever', 'whose', 'why', 'will', 'willing', 'wish', 'with',
    'within', 'without', 'wont', 'would', 'wouldn', 'wouldnt', 'yes', 'yet', 'you', 'youd', 'youll',
    'youre', 'youve', 'your', 'yours', 'yourself', 'yourselves', 'zero'
       }
    
    def stop_words(self, text):
          # Define a set of stop words
        # Split the text into words
       words = text.lower().split()
       # Find stop words in the text
       stop_words_found = [word for word in words if word in self.stop_words]

       return stop_words_found


    def summary(self,text, num_bullet_points=3):
    # Split the text into sentences
      sentences = text.split('. ')
    
    # Calculate the importance score for each sentence
      sentence_scores = []
      for sentence in sentences:
        # Calculate the score based on the length of the sentence
        score = len(sentence.split())
        sentence_scores.append(score)  
       # Sort the sentences based on their scores in descending order
      sorted_sentences = [sentence for _, sentence in sorted(zip(sentence_scores, sentences), reverse=True)]
    
    # Generate the summary with bullet points
      summary = ""
      for i in range(num_bullet_points):
         if i >= len(sorted_sentences):
            break
         summary += f"\u2022 {sorted_sentences[i]}\n"  # Add a bullet point to the sentence
    
      return summary

    def tokenize(self, text):
      tokens = []
      
      current_token = ""
      for char in text:
          if char.isalnum():
            current_token += char
          elif current_token:
            tokens.append(current_token)
            current_token = ""
      if current_token:
             tokens.append(current_token)
      return tokens
   
    def tokenize_stopwords(self, text):  # Example list of stop words
       tokens = []
       current_token = ""
       for char in text:
         if char.isalnum():
            current_token += char
         elif current_token:
            if current_token.lower() not in self.stop_words:  # Check if token is not a stop word
                tokens.append(current_token)
            current_token = ""
       if current_token:
         if current_token.lower() not in self.stop_words:
            tokens.append(current_token)
       return tokens

    def pos_tag(tokens):
     pos_tags = {}
    
     for token in tokens:
        # Define your rules or logic to assign POS tags here
        if token.endswith("ing"):
            pos_tags[token] = "VERB"
        elif token.endswith("ed"):
            pos_tags[token] = "VERB"
        elif token.endswith("s") or token.endswith("es"):
            pos_tags[token] = "NOUN"
        elif token.isnumeric():
            pos_tags[token] = "NUM"
        else:
            pos_tags[token] = "NOUN"
    
     return pos_tags

    


