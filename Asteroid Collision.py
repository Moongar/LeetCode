class Solution:
    def asteroidCollision(self, asteroids):
        ast = [asteroids[0]]
        for i in range(1, len(asteroids)):
            self.collision(ast, asteroids[i])
        return ast

    def collision(self, ast, asteroid):
        if len(ast) == 0:
            ast.append(asteroid)
        else:
            if ast[-1] > 0 and asteroid < 0:
                if ast[-1] == -asteroid:
                    ast.pop()
                elif ast[-1] < -asteroid:
                    ast.pop()
                    self.collision(ast, asteroid)
            else:
                ast.append(asteroid)


s = Solution()
print(s.asteroidCollision([1, -2, -2, -2]))
