class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chrsDict=collections.Counter(chars)
        FormAWord=False
        total=""
        #print(chrsDict)
        for word in words:
            FormAWord=True
            givenWords=collections.Counter(word)
            #print(givenWords)
            for c in givenWords:
                if(givenWords[c]>chrsDict[c]):
                    FormAWord=False
            if FormAWord:
                total+=word
        return(len(total))
      
      
      
#  Leet code
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
