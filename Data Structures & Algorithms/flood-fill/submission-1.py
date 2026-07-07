class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        def dfs(image, sr, sc, color, starting):

            if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] == color or image[sr][sc] != starting:
                return

            image[sr][sc] = color

            dfs(image, sr + 1, sc, color, starting)
            dfs(image, sr - 1, sc, color, starting)
            dfs(image, sr, sc + 1, color, starting)
            dfs(image, sr, sc - 1, color, starting)

        starting = image[sr][sc]

        dfs(image, sr, sc, color, starting)

        return image