class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        starting = image[sr][sc]

        self.dfs(image, sr, sc, color, starting)

        return image

    def dfs(self, image, sr, sc, color, starting):

        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] == color or image[sr][sc] != starting:
            return

        image[sr][sc] = color

        self.dfs(image, sr + 1, sc, color, starting)
        self.dfs(image, sr - 1, sc, color, starting)
        self.dfs(image, sr, sc + 1, color, starting)
        self.dfs(image, sr, sc - 1, color, starting)