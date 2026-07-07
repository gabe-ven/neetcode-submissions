class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        # use a dict to track same letter words
        # loop through all words in strs

        # hat
        # sort it -> 'aht' -> put in result
        # if another one is like that put it in result

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
            
        result = list(groups.values())
        return result
