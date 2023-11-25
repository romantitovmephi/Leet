rowIndex = 3


class Solution:
    def getRow(self, rowIndex):
        empty_list = []
        list1 = [1]

        # создаем rowIndex+1 (фактически) кол-во списков с 1
        for n in range(1, rowIndex+2):
            empty_list.append(n*list1)

        # меняем 1 на значения по принципу треугольника Паскаля
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                empty_list[i][j] = empty_list[i-1][j-1] + empty_list[i-1][j]
        pascal_list = empty_list
        # вернуть нужный ряд
        return pascal_list[rowIndex]


pascal_rows = Solution()
print(pascal_rows.getRow(rowIndex))
